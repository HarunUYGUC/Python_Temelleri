# class

class Ogrenci:
    # method (fonksiyona karşılık gelir)
    # attribute (özellik) (değişkene karşılık gelir)
    pass


# instance (object)

ogrenci = Ogrenci()
print(type(ogrenci))
print(ogrenci)

class Product:
    pass

p1 = Product() # Samsung S10
p2 = Product() # Iphone 12
print(p1, p2)

products = [p1, p2]

for p in products:
    print(p)
    print(type(p))
