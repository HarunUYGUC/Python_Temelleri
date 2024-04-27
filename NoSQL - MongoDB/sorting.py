import pymongo
from bson.objectid import ObjectId

myclient = pymongo.MongoClient("mongodb://localhost:27017")

mydb = myclient["node-app"]
mycollection = mydb["products"]

# ("name", 1) yazarsak da aşağıdaki ile aynı sonucu alırız.
result = mycollection.find().sort("name")

for i in result:
    print(i)

print("--------------")

# -1 yukarıdakinin tersi olur.
result = mycollection.find().sort("name", -1)

for i in result:
    print(i)

print("--------------")

# Küçükten büyüğe doğru fiyat sıralaması yapar.
# ("price", -1) dersek ise büyükten küçüğe doğru olur.
result = mycollection.find().sort("price")

for i in result:
    print(i)

print("--------------")

# Birden fazla filtremiz olursa.
result = mycollection.find().sort([("name"), ("price", -1)])

for i in result:
    print(i)
