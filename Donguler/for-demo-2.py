urunler = [
    {'name': 'iphone 8', 'price': '4000'},
    {'name': 'iphone 8 Plus', 'price': '5000'},
    {'name': 'iphone X', 'price': '6000'},
    {'name': 'iphone XR', 'price': '7000'},
    {'name':'iphone 11', 'price': '8000'},
    {'name': 'samsung s10', 'price': '6000'},
]

# 1- Tüm ürün bilgilerini listeleyiniz.
for urun in urunler:
    print(f"Ürün adı: {urun['name']}, Ürün fiyatı: {urun['price']} TL")


# 2- Ürünlerin fiyatları toplamı nedir?
toplam = 0

for urun in urunler:
    toplam = toplam + int(urun["price"])

print("Ürünlerin fiyat toplamı:", toplam, "TL")


# 3- Ürünlerden fiyatı en fazla 6000 olan ürünleri gösteriniz?
for urun in urunler:
    if (int(urun["price"]) <= 6000):
        print(f"--{urun['name']}-- adlı ürün 6000 TL'den ucuzdur.")


# 4- Kullanıcıdan alınan anahtar kelimeyi içeren ürünleri bulunuz.
kelime = input("Hangi telefon markasının ürünlerini bakmak istersiniz?: ")
flag = -1

for urun in urunler:
    if (urun["name"].find(kelime.lower()) > -1):
        print(f"Ürün adı: {urun['name']}, Ürün fiyatı: {urun['price']} TL")
        flag = 0

if (flag == -1):
    print(f"'{kelime.upper()}' adlı ürün depolarımızda yoktur.")

