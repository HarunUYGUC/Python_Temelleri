BankaHesaplari = {
    "13245678": {
        "ad": "Sadık Turan",
        "hesapNo": "13245678",
        "bakiye": 3000,
        "ekHesap": 2000
    },
    "12345678": {    
        "ad": "Ali Turan",
        "hesapNo": "12345678",
        "bakiye": 2000,
        "ekHesap": 1000
    }
}

def bankamatik(ad, hesapNo):
    if hesapNo in BankaHesaplari:
        if (hesapNo == BankaHesaplari[hesapNo]["hesapNo"] and ad == BankaHesaplari[hesapNo]["ad"]):
            neKadar = float(input(f"Merhaba {hesapNo}'lu kullanıcı, {ad}. Ne kadar para çekmek istersiniz: "))
            if (neKadar <= BankaHesaplari[hesapNo]["bakiye"]):
                cevap1 = input(f"Bakiyeniz yeterli. {BankaHesaplari[hesapNo]['bakiye']} TL paranız bulunmaktadır. Evet / Hayır?: ")
                if (cevap1 == "Evet"):
                    print(f"{neKadar} TL para çektiniz.")
                    BankaHesaplari[hesapNo]["bakiye"] = BankaHesaplari[hesapNo]["bakiye"] - neKadar
                    print(f"Ana Hesabınızda Kalan Miktar: {BankaHesaplari[hesapNo]['bakiye']} TL.")
                else:
                    print(f"{neKadar} TL para çekme işleminiz iptal edildi!")
            else:
                cevap2 = input("Bakiyeniz yeterli değil. Ek Hesap'tan veya ikisi birlikte para çekmek ister misiniz? Evet / Hayır?: ")
                if (cevap2 == "Evet"):
                    if (neKadar <= BankaHesaplari[hesapNo]["ekHesap"]):
                        print(f"{neKadar} TL para çekme işleminiz gerçekleştirildi.")
                        BankaHesaplari[hesapNo]["ekHesap"] = BankaHesaplari[hesapNo]["ekHesap"] - artanMiktar
                        print(f"Ek Hesabınızda Kalan Miktar: {BankaHesaplari[hesapNo]['ekHesap']} TL.")
                    else:
                        if (neKadar <= BankaHesaplari[hesapNo]["ekHesap"] + BankaHesaplari[hesapNo]["bakiye"]):
                            artanMiktar = neKadar - BankaHesaplari[hesapNo]["bakiye"]
                            BankaHesaplari[hesapNo]["bakiye"] = 0
                            BankaHesaplari[hesapNo]["ekHesap"] = BankaHesaplari[hesapNo]["ekHesap"] - artanMiktar
                            print(f"Ana Hesabınızda Kalan Miktar: {BankaHesaplari[hesapNo]['bakiye']} TL.")
                            print(f"Ek Hesabınızda Kalan Miktar: {BankaHesaplari[hesapNo]['ekHesap']} TL.")
                        else:
                            print(f"{neKadar} TL para çekme işleminiz için bakiyeniz yeterli değildir!")

                else:
                    print(f"Para çekme işleminiz her iki hesaptan da olmayacaktır!")
        else:
            print("Bilgilerinizde bir yanlışlık olmalı.")
    else:
        print(f"{hesapNo} şeklinde bir hesap numaramız yoktur!")

ad = input("Adınızı Giriniz: ")
hesapNo = input("Hesap Numaranızı Giriniz: ")
bankamatik(ad, hesapNo)

# 2 hesapNo'dan da farklı bir bilgi girdiğim zaman uygulama hata veriyor fakat hesapNo doğru girip 
# ad bilgisini yanlış girersem veya her iki bilgiyi de doğru girersem istediğim gibi bir sonuç alıyorum. 
# Bu hatanın çözümü nasıl olur?  1 saat yapmakla uğraştım 30 dk'dır da deneme ile uğraşırken hata buldum. 
# :'( :'(
