import json
import sys

filename = sys.argv[1]
with open(filename, "r") as file:
    orders = json.load(file)

customers = {}
items = {}

for order in orders:
    customers[order["phone"]] = order["name"]

    for item in order["items"]:
        if item["name"] in items:
            items[item["name"]]["orders"] += 1
        else:
            items[item["name"]] = {"price": item["price"], "orders": 1}
with open("customers.json", "w") as file:
    json.dump(customers, file, indent=4)

with open("items.json", "w") as file:
    json.dump(items, file, indent=4)
