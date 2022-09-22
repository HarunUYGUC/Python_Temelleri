# 1) Kullanıcıdan isim, yaş ve eğitim bilgilerini isteyip ehliyet alabilme durumunu
# kontrol ediniz.
# Ehliyet alma durumu en az 18 yaş ve eğitim alma durumu lise ya da üniversite olmalıdır.

name = input("İsminiz: ")
age = int(input("Yaşınız: "))
eduInfo = input("Eğitim Seviyeniz (Üni. vb.): ")

if (age >= 18):
    if (eduInfo.lower() == "üniversite") or (eduInfo.lower() == "lise"):
        print(f"{name.upper()} isimli kişi, Ehliyet Alabilirsiniz!")
    else:
        print("Eğitim seviyeniz 'Lise' veya 'Üni.' olmadığı için ehliyet alamazsınız.")
else:
    print("18 yaşından küçük olduğunuz için ehliyet alamazsınız!")


# 2) Bir öğrencinin 2 yazılı, 1 sözlü notunu alıp hesaplanan ortalamaya göre not ağırlığına
# karşılık gelen not bilgisini yazdırınız.
#       0  - 24  => 0
#       25 - 44  => 1
#       45 - 54  => 2
#       55 - 69  => 3
#       70 - 84  => 4
#       85 - 100 => 5

yazili1 = int(input("1. Yazılı: ")) 
yazili2 = int(input("2. Yazılı: "))
sozlu = int(input("Sözlü: "))

ortalama = (yazili1 + yazili2 + sozlu) / 3

if (ortalama >= 0) and (ortalama < 25):
    print(f"{round(ortalama,2)} ortalama ile 5 üzerinden 0 aldınız!")
elif (ortalama >= 25) and (ortalama < 45):
    print(f"{round(ortalama,2)} ortalama ile 5 üzerinden 1 aldınız!")
elif (ortalama >= 45) and (ortalama < 55):
    print(f"{round(ortalama,2)} ortalama ile 5 üzerinden 2 aldınız!")
elif (ortalama >= 55) and (ortalama < 70):
    print(f"{round(ortalama,2)} ortalama ile 5 üzerinden 3 aldınız!")
elif (ortalama >= 70) and (ortalama < 85):
    print(f"{round(ortalama,2)} ortalama ile 5 üzerinden 4 aldınız!")
elif (ortalama >= 85) and (ortalama <= 100):
    print(f"{round(ortalama,2)} ortalama ile 5 üzerinden 5 aldınız!")
else:
    print("0-100 arasında bir bilgi girmelisiniz!")



# 3) Trafiğe çıkış tarihi alınan bir aracın servis zamanının aşağıdaki bilgilere göre 
# hesaplayınız.
#       1. Bakım => 1. Yıl
#       2. Bakım => 2. Yıl
#       3. Bakım => 3. Yıl
#       ** Süre hesabını alınan gün, yıl bilgisine göre gün bazlı olarak hesaplayınız. 
#       *** datetime modülünü kullanmamız gerekiyor!
#       (simdi) - (2018/8/1) => gun

import datetime

tarih = input("Aracınızın trafiğe çıkış tarihi (2019/7/11 gibi): ")
tarih = tarih.split("/")

simdi = datetime.datetime.now()
trafigeCikis = datetime.datetime(int(tarih[0]),int(tarih[1]),int(tarih[2]))

fark = simdi - trafigeCikis
gun = fark.days

if (gun <= 365):
    print("1. Servis Bakımı")
elif (gun > 365) and (gun <= 365*2):
    print("2. Servis Bakımı")
elif (gun > 365*2) and (gun <= 365*3):
    print("3. Servis Bakımı")
else:
    print("Girilen Bilgi Yanlış!")

