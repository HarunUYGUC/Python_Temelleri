# urunAdi, fiyat, satistami ve kategori bilgilerini alarak json veri
# türünde kayıt yapan fonksiyon.
# ürün bilgilerini getiren fonksiyon.

def urunEkle(urunAdi, fiyat, satistami, kategoriler):
    urun = {
        "urunAdi": urunAdi,
        "fiyat": fiyat,
        "satistami": satistami,
        "kategoriler": kategoriler
    }

    import json

    with open(r"C:\Users\Harun\Desktop\Python_Temelleri\JSON ile Dosya İşlemleri\urunler.json", "w") as file:
        json.dump(urun, file, ensure_ascii=False)

urunEkle("Iphone 12", 8000, True, ["Telefon", "Elektronik"])

def urunleriGetir():
    import json

    with open(r"C:\Users\Harun\Desktop\Python_Temelleri\JSON ile Dosya İşlemleri\urunler.json") as file:
        urun = json.load(file)

    kategoriler = ", ".join([kategori for kategori in urun["kategoriler"]])
    print(f"Ürün Adı: {urun["urunAdi"]} - Fiyat: {urun["fiyat"]} - Kategori: {kategoriler}")

urunleriGetir()
