liste = [1,2,3,5,6]
sayilar = []

for item in liste:
    if (item < 4):
        sayilar.append(item)   

print(sayilar)


# [expression for item in liste if koşul]
liste = [1,2,3,5,6]

sonuc = [sayi for sayi in liste if (sayi < 4)]
print(sonuc)


liste = [1,2,3,5,6]

sonuc = [sayi if (sayi % 2 == 0) else "Tek Sayı" for sayi in liste]
print(sonuc)


fiyatlar = [1000,3000,5000,0,4000]
vergiler = []

for fiyat in fiyatlar:
    if (fiyat > 0):
        vergiler.append(fiyat * 1.18)

print(vergiler)


fiyatlar = [1000,3000,5000,0,4000]

vergilerimiz = [(fiyat * 1.18) for fiyat in fiyatlar if (fiyat > 0)]
print(vergilerimiz)


fiyatlar = [1000,3000,5000,0,4000]

vergilerr = [(fiyat * 1.18) if (fiyat > 0) else "Vergi Hesaplanmadı" for fiyat in fiyatlar]
print(vergilerr)


sonuc = []

for x in range(3):
    for y in range(3):
        sonuc.append((x,y))

print(sonuc)


sonuc = [(x,y) for x in range(3) for y in range(3)]
print(sonuc)
