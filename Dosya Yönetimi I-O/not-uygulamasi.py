# Kullanıcıdan isim, ad, soyad, 3 tane not iste ve bu bilgileri bir dosyaya kaydet.
# Kaydettiğimiz dosyadan istediğimiz bir anda not ortalamasını çekerek ortalamanın harf karşılığını göstereceğiz.
# İstediğimiz zaman da bu dosyadaki hesaplanan ortalamaları başka bir dosyaya kadedeceğiz.

# Kullanıcının karşısına bir menü çıkaracağız. Bu menü sonsuz döngüde olacak. Kullanıcı çıkış yapmak istediği zaman belirttiğimiz bir tuşa basacak.
# Kullanıcı ortalamaları mı yazdırmak istiyor, not mu girmek istiyor, hesaplanan notları kayıt etmek mi istiyor? Ne istediğini öğrenip ona göre işlem yapmalıyız.

def not_hesapla(satir):
    satir = satir[:-1] # Bunun buradaki kullanım mantığını hoca anlattı ama anlayamadım. İlginç.
    liste = satir.split(":")

    ogrencininAdiSoyadi = liste[0]
    notlar = liste[1].split(",")

    not1 = int(notlar[0])
    not2 = int(notlar[1])
    not3 = int(notlar[2])

    ortalama = (not1 + not2 + not3)/3

    if (ortalama >= 90) and (ortalama <= 100):
        harf = "AA"
    elif (ortalama >= 85) and (ortalama < 90):
        harf = "BA"
    elif (ortalama >= 65) and (ortalama < 85):
        harf = "CC"
    else:
        harf = "FF"
    
    return ogrencininAdiSoyadi + ": " + harf + "\n"

def notlari_oku():
    with open(r"c:\Users\Harun\Desktop\Python_Temelleri\Dosya Yönetimi I-O\sinav_notlari.txt", "r", encoding="UTF-8") as file:
        for satir in file:
            # print(satir)
            print(not_hesapla(satir))


def not_gir():
    ad = input("Öğrencinin Adı: ")
    soyad = input("Öğrencinin Soyadı: ")

    not1 = input("1. Not: ")
    not2 = input("2. Not: ")
    not3 = input("3. Not: ")

    with open(r"c:\Users\Harun\Desktop\Python_Temelleri\Dosya Yönetimi I-O\sinav_notlari.txt", "a", encoding="UTF-8") as file:
        file.write(ad + " " + soyad + ": " + not1 + ", " + not2 + ", " + not3 + "\n")
        

def notlari_kayit_et():
    with open(r"c:\Users\Harun\Desktop\Python_Temelleri\Dosya Yönetimi I-O\sinav_notlari.txt", "r", encoding="UTF-8") as file:
        liste = []

        for i in file:
            liste.append(not_hesapla(i))

        with open(r"c:\Users\Harun\Desktop\Python_Temelleri\Dosya Yönetimi I-O\sonuclar.txt", "w", encoding="UTF-8") as file2:
            for i in liste:
                file2.write(i)


while True:
    islem = input("1- Notları Oku \n2- Not Gir \n3- Notları Kayıt Et \n4- Çıkış \n")

    if (islem == "1"):
        notlari_oku()
    elif (islem == "2"):
        not_gir()
    elif (islem == "3"):
        notlari_kayit_et()
    else:
        break
