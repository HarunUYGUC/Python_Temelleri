import pymongo
from bson.objectid import ObjectId

myclient = pymongo.MongoClient("mongodb://localhost:27017")

mydb = myclient["node-app"]
mycollection = mydb["products"]

for i in mycollection.find():
    print(i)

print("-----------------")

# delete_one() dediğimiz için sadece ilk başta olanı siler. 
mycollection.delete_one({"name": "Samsung S10"})

for i in mycollection.find():
    print(i)

print("-----------------")

# S ile başlayan bütün veriler silinir.
mycollection.delete_many({"name": {"$regex": "^S"}})

for i in mycollection.find():
    print(i)

# result = mycollection.delete_many()
# dersek bütün kayıtlar silinir.
# print(f"result.deleted_count" adet kayıt silindi.)
