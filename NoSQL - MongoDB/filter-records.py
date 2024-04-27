import pymongo
from bson.objectid import ObjectId # string bilgiyi ObjectId'ye çevirmek için.

myclient = pymongo.MongoClient("mongodb://localhost:27017")

mydb = myclient["node-app"]
mycollection = mydb["products"]

filter = {"name": "Samsung S5"}

result = mycollection.find(filter)

for i in result:
    print(i)

print("----------------")

# Filtreye uygun ilk kaydı getirir.
result = mycollection.find_one(filter)
print(result)

print("----------------")

# Bu şekilde "_id" bilgisini string olarak gönderirsek hata alırız çünkü 
# database'de bu bilgi "ObjectId" olarak tutuluyor. Yani bizim de bu string 
# bilgiyi ObjectId'ye çevirmemiz gerekiyor.
result = mycollection.find_one({"_id": ObjectId("662cd27f91eed8b995fd9f36")})
print(result)

print("----------------")

result = mycollection.find({
    "name": {
        "$in": ["Samsung S5", "Samsung S6"] # Liste içerisindeki elemanlardan herhangi birisi 
        # "name" alanında bulunuyorsa result olarak sonuç verecek.
    }
})

for i in result:
    print(i)

print("----------------")

result = mycollection.find({
    "price": {
        "$gt": 2000 # gt = greater than
        # gte = greater than equal
        # eq = equal
        # lt = less than
        # lte = less than equal
        # Bunlara "MongoDB Operators" deniyor.
    }
})

for i in result:
    print(i)

print("----------------")

result = mycollection.find({
    "name": {"$regex": "^S"} # regex = regular expression
    # name alanı S ile başlayan kayıtları getir.
})
