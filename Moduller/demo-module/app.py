"""
    module1 (db)        : urunler
    module2 (methods)   : urunEkle(), urunGuncelle(), urunleriGetir()
    module3 (app)       : 

            yeni ürün ekleme  => urunEkle("iphone 11 pro", 7500)
            ürün güncelle     => urunGuncelle(1, "iphone 12 pro", 8000)
            ürünleri listele  => urunleriGetir()
"""


from methods import *

urunleriGetir()

print("*" * 10)

urunEkle("iphone 11 pro", 7500)
urunEkle("iphone 7s", 4500)

urunleriGetir()

print("*" * 10)

urunGuncelle(6, "iphone 8s", 5500)

urunleriGetir()
