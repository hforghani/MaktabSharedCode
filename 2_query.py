import datetime

from bson import ObjectId
from pymongo import MongoClient

client = MongoClient('localhost', 27017)
db = client.test_database

# Get a single document:
print('post:')
print(db.posts.find_one())

# querying on specific elements:
res_post = db.posts.find_one({"author": "Mike"})
print('found post:')
print(res_post)

db.posts.find_one({"_id": ObjectId('5fd9a9e57185ea4f89e005cc')})

# Querying for More Than One Document

print('all posts:')
for post in db.posts.find():
    print(post)

# Counting
print(db.posts.count_documents({}))
print(db.posts.count_documents({"author": "Mike"}))

# Range Queries
d = datetime.datetime(2021, 11, 12, 12)
print('posts before 11/12/2021 12:00 :')
for post in db.posts.find({"date": {"$lt": d}}).sort("author"):
    print(post)
