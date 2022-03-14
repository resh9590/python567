products = {"a" : {"rank": 1, "sales":100},"b" : {"rank": 2, "sales":200, "c" : {"rank": 3, "sales":300}}}

products_value = {"rank": 1, "sales":400}
products["d"] = products_value

print(products)