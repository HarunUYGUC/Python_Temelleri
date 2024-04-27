import pymongo
from bson.objectid import ObjectId

myclient = pymongo.MongoClient("mongodb://localhost:27017")

mydb = myclient["node-app"]
mycollection = mydb["products"]

for i in mycollection.find():
    print(i)

print("---------------")

mycollection.update_one(
    {"name": "Samsung S6"},
    {"$set": {
        "name": "Iphone 7",
        "price": 5000
    }}
)

for i in mycollection.find():
    print(i)

print("---------------")

mycollection.update_many(
    {"name": "Samsung S5"},
    {"$set": {
        "name": "Iphone 5",
        "price": 4000
    }}
)

for i in mycollection.find():
    print(i)

print("---------------")

query = {"name": "Samsung S7"}
newvalues = {"$set": {
                "name": "Iphone 8",
                "price": 7000
            }}

mycollection.update_many(query, newvalues)

for i in mycollection.find():
    print(i)

print("---------------")

query = {"name": "Samsung S11"}
newvalues = {"$set": {
                "name": "Iphone X",
                "price": 10000
            }}

result = mycollection.update_many(query, newvalues)

print(f"{result.modified_count} adet kayıt güncellendi.")

for i in mycollection.find():
    print(i)
