import pymongo
from bson.objectid import ObjectId

myclient = pymongo.MongoClient("mongodb://localhost:27017")

mydb = myclient["node-app"]
mycollection = mydb["products"]

# result = mycollection.find_one
# print(result)

# Bütün kayıtları tüm bilgileriyle birlikte getirir.
for i in mycollection.find():
    print(i)

print("-----------------------")

# ilk {} bütün kolonları getir, ikinci {} ise bunları getir bunları getirme demek yani filtrelemek.
# 0, istemiyoruz; 1 istiyoruz demek.
for i in mycollection.find({}, {"_id": 0, "name": 1, "price": 1}):
    print(i)

print("-----------------------")

# 0'ları yazıp 1'leri yazmazsak 0'lar hariç diğer kolonların hepsi gelir.
for i in mycollection.find({}, {"_id": 0, "name": 0}):
    print(i)

print("-----------------------")

# 1 yazılanlar gelir. Ayrıca id bilgisi de gelir.
for i in mycollection.find({}, {"name": 1}):
    print(i)
