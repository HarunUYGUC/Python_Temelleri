# Yaş 18 ve (mezuniyet == "lise" ya da mezuniyet == "üniversite")

# and (ve) operatörü:.....
x = 10
sonuc = 5 < x < 15
print(sonuc)


x = 10
sonuc = (x > 5) and (x < 15)
print(sonuc)


"""
and operatöründe 

True ve True => True
True ve False => False
False ve False => False

idir.
Yani and operatöründe sonucun True çıkması için her iki sonucun da True olması lazımdır.
"""

hak = 3
devam = "evet"

sonuc = (hak > 0) and (devam == "evet")

print(sonuc)


# or (veya) operatörü:.....

x = 11

sonuc = (x > 0) and (x % 2 == 0)

print(sonuc)


x = 11

sonuc = (x > 0) or (x % 2 == 0)

print(sonuc)


"""
or operatöründe

True veya True => True
True veya False => True
False veya False => False

idir.
Yani or operatöründe bir sonucun True olması işlemin sonucunun True olması için gereklidir.
"""
# x, 5 ve 10 arasında bir çift sayı mıdır?
# Önemli: Hem 5 ve 10 arasında olmalı hem de çift sayı olmalı!!!

x = 8

sonuc = ((x > 5) and (x < 10)) and (x % 2 == 0)
 
print(sonuc)


x = -8

sonuc = ((x > 5) and (x < 10)) and (x % 2 == 0)
 
print(sonuc)