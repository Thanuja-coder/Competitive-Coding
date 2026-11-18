data = {
    "type": "ecom_data",
    "data": {
        "products": [
            {"product": "iphone", "qty": 10, "price": 45000, "ratings": [4.5, 4, 9, 4, 2]},
            {"product": "Nothing", "qty": 15, "price": 25000, "ratings": [4.1, 4.5, 3.2]},
            {"product": "Galaxy Phone", "qty": 21, "price": 35000, "ratings": [4.1, 3.2, 3.9]}
        ]
    }
}

highest_avg = 0
product_name = ""

for product in data["data"]["products"]:

    avg = sum(product["ratings"]) / len(product["ratings"])

    if avg > highest_avg:
        highest_avg = avg
        product_name = product["product"]

print("Product:", product_name)
print("Highest Average Rating:", highest_avg)

#print total value sold from the stock
total = 0

for product in data["data"]["products"]:
    value = product["qty"] * product["price"]
    total = total + value

print("Total stock value:", total)