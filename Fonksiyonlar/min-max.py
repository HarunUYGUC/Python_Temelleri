sayilar = [1, 5, 7, 45, 25, 89]

sonuc = min(sayilar)

print(sonuc)


sayilar = [1, 5, 7, 45, 25, 89]

sonuc = max(sayilar)

print(sonuc)


harfler = ["a", "v", "h", "s"]

sonuc = min(harfler)

print(sonuc)


harfler = ["a", "v", "h", "s"]

sonuc = max(harfler)

print(sonuc)


isimler = ["ahmet", "ismail", "ada", "sena"]

sonuc = min(isimler)

print(sonuc)


isimler = ["ahmet", "ismail", "ada", "sena", "sadık"]

sonuc = max(isimler)

print(sonuc)


isimler = ["ahmet", "ismail", "ada", "sena", "sadık"]

sonuc = [len(isim) for isim in isimler]

print(sonuc)


isimler = ["ahmet", "ismail", "ada", "sena", "sadık"]

sonuc = min([len(isim) for isim in isimler])

print(sonuc)


isimler = ["ahmet", "ismail", "ada", "sena", "sadık"]

sonuc = max([len(isim) for isim in isimler])

print(sonuc)


isimler = ["ahmet", "ismail", "ada", "sena", "sadık"]

sonuc = max(isimler, key=lambda isim: len(isim))

print(sonuc)


urunler = [
    {"title": "iphone x", "price": "5000"},
    {"title": "iphone xr", "price": "6000"},
    {"title": "iphone 11", "price": "7000"}
]

sonuc = min(urunler, key=lambda urun: urun["price"])

print(sonuc)

sonuc = min(urunler, key=lambda urun: urun["price"])["title"]
print(sonuc)


max = 0

for urun in urunler:
    if (int(urun["price"]) > max):
        max = int(urun["price"])

print(max)
