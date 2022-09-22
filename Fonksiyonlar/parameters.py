def selamla(isim):
    return f"Merhaba, {isim}"

sonuc = selamla("Sadık")
print(sonuc)


def toplam(a, b):
    return a + b

sonuc = toplam(10,20)
print(sonuc)


def yasHesapla(dogumYili):
    return 2021 - dogumYili

sonuc = yasHesapla(1984)
print(sonuc)


def emekliligeKacYilKaldi(dogumYili, isim):
    yas = yasHesapla(dogumYili)
    
    kalanSure = 65 - yas

    if (kalanSure > 0):
        print(f"{isim}, emekliliğinize {kalanSure} yıl kaldı.")
    else:
        print(f"{isim}, zaten {abs(kalanSure)} yıl önce emekli oldunuz.")

emekliligeKacYilKaldi(1983, "Sadık")
emekliligeKacYilKaldi(1950, "Ali")

