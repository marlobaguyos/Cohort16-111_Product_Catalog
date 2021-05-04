#!/user/bin/env python3
#-*- coding: utf8 -*-
"""Route definitions"""

from flask import (
      render_template,
      request, redirect,
      url_for,
      flash)
import sys
from app import app, db
from datetime import date, datetime
from app.database import Product
from app.forms.products import ProductForm

@app.route("/")
def index():
  """Simple index view that displays version info and server time"""
  version = {
    "ok" : True,
    "message" : "success",
    "version" : "1.0.0",
    "server time" : datetime.now().strftime("%F %H:%H:%S")
  }
  return render_template("index.html", version=version)

@app.route("/products")
def get_products():
    """Retrieve and display all products"""
    products = Product.query.all()
    return render_template("products.html", product_list=products)

@app.route("/products", methods=["POST"])
def create_product():
    """Create a new product"""
    form = ProductForm(request.form)
    if form.validate():
        product = Product()
        product.name = form.name.data
        product.price = form.price.data
        product.quantity = form.quantity.data
        product.description = form.description.data
        db.session.add(product)
        db.session.commit()
        flash("Product created!")
        return redirect(url_for('get_products'))
    flash("Invalid data")
    return redirect(url_for('get_products'))

@app.route("/products/<int:pid>", methods=["POST"])
def update_product(pid):
    """Updates a single product"""
    form = ProductForm(request.form)
    if form.validate():
        product = Product.query.filter_by(id=pid).first()
        product.name = form.name.data
        product.price = form.price.data
        product.quantity = form.quantity.data
        product.description = form.description.data
        db.session.commit()
        flash("Product updated!")
        return redirect(url_for('get_products'))
    flash("Invalid data")
    return redirect(url_for('get_products'))

@app.route("/products/registrations")
def create_product_form():
    """Renders the create product form"""
    prod_form = ProductForm()
    return render_template("create_form.html", form=prod_form)

@app.route("/products/modifications/<int:pid>")
def update_product_form(pid):
    """Renders the update product form, which populates each form
        field with product data for a given product id.
    """
    form = ProductForm()
    product = Product.query.filter_by(id=pid).first()
    return render_template("update_form.html", form=form, product=product)


@app.route("/products/eliminations/<int:pid>")
def delete_product(pid):
    """Hard delete a single product"""
    product = Product.query.filter_by(id=pid).first()
    db.session.delete(product)
    db.session.commit()
    flash("Product deleted!")
    return redirect(url_for('get_products'))


@app.errorhandler(404)
def page_not_found(e):
    return render_template("404.html"), 404

# @app.route("/products/<int:pid>")
# def get_product_details(pid):
#   """Retrieve a single product"""
#   return render_template("product_detail.html", product=product)

# @app.route("/products/<int:pid>", methods=["PUT"])
# def update_product(pid):
#   """Update a single product"""
#   return "Single product update"



# app.route("/products/<int:pid>", method=["DELETE"])
# def delete_product(pid):
#   """soft deleteelete a single product"""
#   return "Soft delete a product"
