import pymongo
from pymongo import MongoClient

client = MongoClient('localhost', 27017)
db = client.test_database

# Create a unique index on field 'user_id' of collection 'profiles':
result = db.profiles.create_index([('user_id', pymongo.ASCENDING)], unique=True)
print(f'result of create_index: {result}')

# Get list of indexes:
print('list of indexes:')
print(sorted(list(db.profiles.index_information())))

# Let’s set up some user profiles
user_profiles = [
    {'user_id': 211, 'name': 'Luke'},
    {'user_id': 212, 'name': 'Ziltoid'}
]
result = db.profiles.insert_many(user_profiles)
print(result)

# The index prevents us from inserting a document whose user_id is already in the collection:
new_profile = {'user_id': 213, 'name': 'Drew'}
duplicate_profile = {'user_id': 212, 'name': 'Tommy'}
result = db.profiles.insert_one(new_profile)  # This is fine.
print(result)
db.profiles.insert_one(duplicate_profile)

# See also: create_indexes, drop_index, drop_indexes, reindex, list_indexes
