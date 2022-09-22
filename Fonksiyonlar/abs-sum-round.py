sayilar = [34, 2, 5, 7, 98]

sonuc = sum(sayilar)
print(sonuc)

sonuc = sum(sayilar, 10)
print(sonuc)


urunler = [
    {"title": "iphone x", "price": 5000},
    {"title": "iphone xr", "price": 6000},
    {"title": "iphone 11", "price": 7000}
]

sonuc = sum([urun["price"] for urun in urunler])
print(sonuc)


sonuc = round(10.2)
print(sonuc)

sonuc = round(10.6)
print(sonuc)

sonuc = round(10.5)
print(sonuc)

sonuc = round(11.5)
print(sonuc)

sonuc = round(1.424242)
print(sonuc)

sonuc = round(1.424242, 2)
print(sonuc)

sonuc = round(1.426242, 2)
print(sonuc)


sonuc = abs(-1.5)
print(sonuc)

sonuc = abs(-5)
print(sonuc)
