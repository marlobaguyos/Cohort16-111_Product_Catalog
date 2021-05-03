#!/user/bin/env python3
#-*- coding: utf8 -*-
"""Smoke tests"""

#To add an ID to our url: 
#url = "%s%s" % (BASE_URL, "/products/1")
#The url above is needed for the following tests:
# test PUT -> requests.put(url, data=whatever_data)
# test DELETE -> requests.delete(url)
# test GET (detail page) -> requests.get(url)

import requests
BASE_URL ="http://127.0.0.1:5000"

def test_get_all():
  url = "%s%s" % (Base_URL, "/")
  out = requests.get("url")
  assert out.text == "Return all products"

def test_create_product():
  url = "%s%s" % (BASE_URL, "/")
  sample_data = {"product_name": "Banana", "price": 100.00, "quantity": 5}
  out = request.post(url, data=sample_data)
  assert out.text == "Create new prodcut"