# db.sales.aggregate([
# 	{$unwind: {path: "$items"}},
# 	{$group: {_id: {
# 		id: "$_id",
# 		saleDate: "$saleDate",
# 		customer: "$customer",
# 		location: "$storeLocation"
# 		}, price: {$sum: {$multiply: ["$items.price", "$items.quantity"]}}}},
# 	{$sort: {price: -1}},
# 	{$limit: 1},
# 	])
from pymongo import MongoClient

client = MongoClient()
db = client.salesdb
res = db.sales.aggregate([
    {"$unwind": "$items"},
    {"$group": {"_id": {
        "id": "$_id",
        "saleDate": "$saleDate",
        "customer": "$customer",
        "location": "$storeLocation"
    }, "price": {"$sum": {"$multiply": ["$items.price", "$items.quantity"]}}}},
    {"$sort": {"price": -1}},
    {"$limit": 1},
])

dic = list(res)[0]

print(dic['_id']['saleDate'])
print(dic['_id']['customer'])
print(dic['_id']['location'])
print(dic['price'])