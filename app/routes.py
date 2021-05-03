#!/user/bin/env python3
#-*- coding: utf8 -*-
"""Route definitions"""

from app import app

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
  """Update a single product"""

app.route("/products", methods=["POST"])
  """Create a new product"""
  pass

app.route("/products/<int:pid>", method=["DELETE"])
  """soft deleteelete a single product"""
  pass
