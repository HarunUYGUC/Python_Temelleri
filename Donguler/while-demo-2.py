# Kullanıcıdan alacağınız sınırsız ürün bilgisini urunler listesi içinde saklayınız.
#   ** ürün sayısını kullanıcıya sorun.
#   ** dictionary listesi yapısı (urunAdi, fiyat) şeklinde olsun.
#   ** ürün ekleme işlemi bittiğinde ürünleri ekranda while ile listeleyin.

urunSayisi = int(input("Kaç tane ürün-fiyat bilgisi gireceksiniz?: "))
urunAdlari = []
urunFiyatlari = []
i = 1

while (i <= urunSayisi):
    ad = input(f"{i}. ürün adını giriniz: ")
    urunAdlari.append(ad.capitalize())
    
    fiyat = input(f"{i}. ürün fiyatını giriniz: ")
    urunFiyatlari.append(fiyat)
    i += 1

i = 0

while (i < urunSayisi):
    print(f"Ürün adı: {urunAdlari[i]}, Ürün Fiyatı: {urunFiyatlari[i]}")
    i += 1


# 2. Yöntem (Daha Mantıklı):

urunSayisi = int(input("Kaç tane ürün-fiyat bilgisi gireceksiniz?: "))
urunler = []
i = 1

while (i <= urunSayisi):
    urunAdi = input("Ürün adını giriniz: ")
    urunFiyati = input("Ürün fiyatını giriniz: ")
    urunler.append({
        "urunAdi": urunAdi.title(),
        "urunFiyati": urunFiyati.title()
    })
    i += 1

for urun in urunler:
    print(f"Ürün Adı: {urun['urunAdi']}, Ürün Fiyatı: {urun['urunFiyati']}")

