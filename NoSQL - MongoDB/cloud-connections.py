import pymongo

myclient = pymongo.MongoClient("mongodb+srv://harunuyguc:<password>@cluster0.uhw7f7k.mongodb.net/")

mydb = myclient["node-app"] # Collection Name'i de belirtmezsek Database oluşturamayız
# veya olan zaten var olan Database'i çağıramayız.

print(myclient.list_database_names())
