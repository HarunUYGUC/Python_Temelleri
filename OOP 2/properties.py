""" Sınıf içerisinde tanımlamış olduğumuz Properties'lere (Mülk) yani Attribute'lara (Özellik) 
istediğimiz bir özelliği atayamamamız gerekmektedir. Örneğin, buradaki gibi 4000 yerine -4000 
gibi bir değer girememeliyiz. Bunun için if-else mantığını kullanabiliriz."""

""" Private bir özellik oluşturmak istediğimiz zaman o özelliği self.price = _price olarak kayıt etmek yerine
self._price = _price olarak kaydedebiliriz. Bu self._price mantığındaki alt çizgi sayesinde o nesnenin 
ait olduğu sınıfın dışından ulaşılmaması gerektiğini söyleriz. """

class Product:
    def __init__(self, _name, _price):
        self.name = _name
        if (_price >= 0):
            self._price = _price
        else:
            self._price = 0
            # raise ValueError("Fiyat için negatif değer ataması yapılamaz.")

    def set_price(self, _value):
        if (_value >= 0):
            self._price += _value
        else:
            self._price += 0

    def get_price(self):
        return self._price
    
p = Product("Xiaomi Mi Note 10 Lite", 4000)

print(p._price)
print(p.get_price())

p.set_price(1250)
print(p.get_price())

p.set_price(-2200)
print(p.get_price())

p = Product("Xiaomi Mi Note 10 Lite", -4000)
print(p._price)

# p.price = -4000
# print(p.price)



print("*" * 10)
# Property aslında bizim için bir Decorator'dur ama hazır Decorator'dur.

class Product:
    def __init__(self, _name, _price, _description):
        self.name = _name
        self.description = _description
        if (_price >= 0):
            self._price = _price
        else:
            self._price = 0 
        
    @property # Fiyat özelliğinin sınıf dışından ulaşılmasını istersek @property
    def price(self): # Attribute'ünü kullanarak aslında metot olan fonksiyonu bir özelliğe dönüştürdük.
        return self._price
    
    @price.setter
    def price(self, _value):
        if (_value >= 0):
            self._price += _value
        else:
            raise ValueError("Fiyat için negatif değer ataması yapılamaz.")
    
    @property
    def short_description(self):
        return self.description[:10]

p = Product("Mi Note 10 Lite", 4000, ".....")
print(p.price)

p2 = Product("Iphone 12", 9000, "Iphone 12 Apple'ın çıkardığı en yeni üründür.")
print(p2.short_description)

p.price = -9000
print(p.price)
