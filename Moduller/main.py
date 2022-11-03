import module

sonuc = module.sayi
print(sonuc)

sonuc = module.sayilar
print(sonuc)

sonuc = module.ogrenci
print(sonuc)

sonuc = module.ogrenci["ad"]
print(sonuc)

sonuc = module.ogrenci["notlar"]
print(sonuc)

sonuc = module.topla(10,20)
print(sonuc)


import module as m

sonuc = m.ogrenci
print(sonuc)


from module import ogrenci

sonuc = ogrenci
print(sonuc)

from module import ogrenci, topla

sonuc = ogrenci
print(sonuc)

sonuc = topla(10, 20)
print(sonuc)


from module import *

sonuc = sayi
print(sayi)

sonuc = ogrenci
print(ogrenci)
