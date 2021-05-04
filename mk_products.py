#!/user/bin/env python3
#-*- coding: utf8 -*-
"""Sample python code that creates products and displays them."""

from app import db
from app.database import Product

def create_my_product(name, price, quantity):
  """Simple user creation function"""
  db.session.add(
    Product(
      name=name,
      price=price,
      quantity=quantity
      )
    )
  db.session.commit()

if __name__ == "__main__":
  create_my_product("BitCoin", 10.00, 10)
  products = Product.query.all()
  print(products)
  create_my_product("Dodgecoin", 12.00, 20)
  
