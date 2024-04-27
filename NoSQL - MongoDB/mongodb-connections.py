import pymongo

myclient = pymongo.MongoClient("mongodb://localhost:27017")

mydb = myclient["node-app"] # Collection Name'i de belirtmezsek Database oluşturamayız
# veya olan zaten var olan Database'i çağıramayız.

print(myclient.list_database_names())
