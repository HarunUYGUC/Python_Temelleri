class Product:
    def __init__(self):
        self.name = "Samsung S10"
        self.price = 2000
        print("product nesnesi oluşturuldu")

p1 = Product()
print(p1.name, p1.price)


class Product:
    def __init__(self, name, price, isActive):
        self.name = name
        self.price = price
        self.isActive = isActive
        print("product nesnesi oluşturuldu")

p1 = Product("Samsung S10", 5000, True)
p2 = Product("Iphone 12", 8000, False)

print(p1.name, p1.price, p1.isActive)
print(p2.name, p2.price, p2.isActive)
