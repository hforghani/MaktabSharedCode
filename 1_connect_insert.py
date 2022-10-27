import datetime

from pymongo import MongoClient

# to connect to default host and port:
# client = MongoClient()

# You can specify the host and port explicitly:
client = MongoClient('localhost', 27017)

# or you can use the MongoDB URI format:
# client = MongoClient('mongodb://localhost:27017/')

# using attribute style access:
db = client.test_database

# If your database name is for example 'test-database', you can use dictionary style access instead:
# db = client['test-database']

# getting collection using attribute style access, or dictionary style access:
collection = db.test_collection
# collection = db['test-collection']

# ================ Inserting a Document

post = {"author": "Mike",
        "text": "My first blog post!",
        "tags": ["mongodb", "python", "pymongo"],
        "date": datetime.datetime.utcnow()}

# This returns an instance of InsertOneResult
res = db.posts.insert_one(post)
print(f'res = {res}')
print(f'post id = {res.inserted_id}')

# Also insert_many
