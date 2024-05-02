class Product:
    def __init__(self, name, price):
        self.name = name
        self.price = price
    
p1 = Product("Samsung S10", 5000)
p2 = Product("Samsung S11", 6000)

# print(p1)
# print(type(p1))

products = [p1.__dict__, p2.__dict__]

# products = {
#     p1.id: 
#         p1.__dict__, 
#     p2.id: 
#         p2.__dict__
# }

print(products)

import json

# print(p1.__dict__)

with open(r"C:\Users\Harun\Desktop\Python_Temelleri\JSON ile Dosya İşlemleri\urunler-2.json", "w") as file:
    json.dump(products, file)

with open(r"C:\Users\Harun\Desktop\Python_Temelleri\JSON ile Dosya İşlemleri\urunler-2.json") as file:
    data = json.load(file)

print(data)

urunler = []

for p in data:
    urunler.append(Product(p["name"], p["price"]))

print(urunler)
print(urunler[0].name)

# for key, value in data.items():
#     pass
