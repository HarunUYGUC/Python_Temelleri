# 1- 3 ürün bilgisini (id, ad, fiyat) kullanicıdan aldığınız bilgilerle dictionary içinde saklayın1z.

id1 = input("1. ürünün ID bilgisini giriniz : ")
ad1 = input("1. ürünün AD bilgisini giriniz : ")
fiyat1 = input("1. ürünün FİYAT bilgisini giriniz : ")

id2 = input("2. ürünün ID bilgisini giriniz : ")
ad2 = input("2. ürünün AD bilgisini giriniz : ")
fiyat2 = input("2. ürünün FİYAT bilgisini giriniz : ")


id3 = input("3. ürünün ID bilgisini giriniz : ")
ad3 = input("3. ürünün AD bilgisini giriniz : ")
fiyat3 = input("3. ürünün FİYAT bilgisini giriniz : ")

urunler = {
    "1. Ürün": {
        "ID": id1,
        "Ad": ad1,
        "Fiyat": fiyat1
    },
    "2. Ürün": {
        "ID": id2,
        "Ad": ad2,
        "Fiyat": fiyat2   
    },
    "3. Ürün": {
        "ID": id3,
        "Ad": ad3,
        "Fiyat": fiyat3
    }
}

print(urunler)

print(urunler["1. Ürün"])

print(urunler["1. Ürün"]["ID"])


# 2- Ürün id bilgisini kullanicıdan alıp ilgili ürün bilgisini gösterin.

urunler = {
    id1: {
        "Ad": ad1,
        "Fiyat": fiyat1
    },
    id2: {
        "Ad": ad2,
        "Fiyat": fiyat2   
    },
    id3: {
        "Ad": ad3,
        "Fiyat": fiyat3
    }
}


cevap = input("ID bilgisini giriniz / 21-22-23 girebilirsiniz! : ")

print(urunler[cevap])


cevap = input("ID bilgisini giriniz / 21-22-23 girebilirsiniz! : ")

print(f"Ürün ID: {cevap} - Ürün Adı: {urunler[cevap]['Ad']} - Ürün Fiyatı: {urunler[cevap]['Fiyat']}")