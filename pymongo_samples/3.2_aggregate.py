from pymongo import MongoClient

client = MongoClient()
db = client.salesdb
# res = db.sales.aggregate([
#     {'$unwind': "$items"},
#     {'$sort': {"items.price": -1}},
#     {'$limit': 1},
#     {'$project': {"items.name": 1, "items.price": 1, '_id': 0}}
# ])

res = db.sales.aggregate([
    {'$unwind': "$items"},
    {'$group': {'_id': None, 'max': {'$max': '$items.price'}}},
])

max_price = list(res)[0]['max']

# res = db.sales.find({'items.price': max_price})
# print(res.count())
# for sale in res:
#     for item in sale['items']:
#         if item['price'] == max_price:
#             print(item['name'])

res = db.sales.aggregate([
    {'$unwind': '$items'},
    {'$match': {'items.price': max_price}},
    {'$project': {'name': '$items.name', 'price': '$items.price', '_id': 0}}
])

print(list(res))
