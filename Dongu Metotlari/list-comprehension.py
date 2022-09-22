sayilar = []

for i in range(10):
    sayilar.append(i)

print(sayilar)

# [expression for item in list]

sayilar = [i for i in range(10)]
print(sayilar)

sayilar = [i*i for i in range(10)]
print(sayilar)



liste = [10,4,7,9,70]
sayilar = []

for i in liste:
    i *= 2
    sayilar.append(i)

print(sayilar)


sayilar = []

for i in liste:
    sayilar.append(i*2)

print(sayilar)


isim = "Ahmet"

sonuc = [c.upper() for c in isim]
print(sonuc)


sonuc = [str(sayi) for sayi in liste]
print(sonuc)


isimler = ["AhMEt","HarUN","meHMeT","kAyA"]
sonuc = [name.capitalize() for name in isimler]
print(sonuc)
