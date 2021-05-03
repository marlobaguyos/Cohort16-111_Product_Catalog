#!/user/bin/env python3
#-*- coding: utf8 -*-
"""Route definitions"""

from flask import render_template
from app import app
import sys
from datetime import date, datetime

@app.route("/version")
def version():
  return{
    "ok" : True,
    "message": "success",
    "version": "1.0.0",
    "server time": datetime.now().strftime("%F %H:%H:%S")
  }

@app.route("/")
def index():
  return render_template("index.html")

@app.route("/products")
def get_products():
  """Retrieve all products"""
  return "Return all product"

@app.route("/products/<int:pid>")
def get_product_details(pid):
  """Retrieve a single product"""
  return "Single product detail"

@app.route("/products/<int:pid>", methods=["PUT"])
def update_product(pid):
  """Update a single product"""
  return "Single product update"

app.route("/products", methods=["POST"])
def create_products(pid):
  """Create a new product"""
  return "Create new product"

app.route("/products/<int:pid>", method=["DELETE"])
def delete_product(pid):
  """soft deleteelete a single product"""
  return "Soft delete a product"
