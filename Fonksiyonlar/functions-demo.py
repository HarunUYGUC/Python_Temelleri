# 1- Kendisine gönderilen bir kelimeyi belirtilen kez ekranda gösteren fonksiyonu yazınız.

def kosulluKelime(sayi, kelime):
    i = 1
    while (i <= sayi):
        print(f"{i}. {kelime}")
        i += 1
    
kelime = input("Hangi kelimeyi ekranda göstermek istersiniz?: ")
sayi = int(input("Yazdığınız kelimeyi kaç kez ekranda göstermek istersiniz?: "))
kosulluKelime(sayi, kelime)


# 2- Dikdörgenin alan ve çevresini hesaplayan fonksiyonu yazınız.

def dikdortgen(kisaKenar, uzunKenar):
    cevre = kisaKenar * 2 + uzunKenar * 2
    print(f"Dikdörtgenin Çevresi: {cevre}")
    alan = kisaKenar * uzunKenar
    print(f"Dikdörtgenin Alanı: {alan}")

kisaKenar = int(input("Dikdörtgenin kısa kenarını yazınız!: "))
uzunKenar = int(input("Dikdörtgenin uzun kenarını yazınız!: "))
dikdortgen(kisaKenar, uzunKenar)


# 3- Yazı tura uygulamasını fonksiyon kullanarak yapınız. (Random modülü)

def yaziTura(cevap):
    import random
    yaziMiTuraMi = random.randint(0, 1)
    
    if (yaziMiTuraMi == cevap):
        print(f"{cevap} diyerek DOĞRU bildiniz!")
    else:
        print(f"{cevap} diyerek YANLIŞ bildiniz!")

cevap = int(input("Yazı mı (1), Tura mı (0) ?: "))
yaziTura(cevap)


# 3- Kendisine gönderilen 2 sayı arasındaki tüm asal sayıları bulan fonksiyonu yazınız.

def asalSayiMi(x, y):
    for i in range(x, y+1):
        if (i > 1):
            for j in range(2, int(i/2+1)):
                if (i % j == 0):
                    break
            else:
                print(f"{i} Asal Sayıdır!")

x = int(input("Alt aralığı belirleyiniz.: "))
y = int(input("Üst aralığı belirleyiniz.: "))
asalSayiMi(x, y)


# 4- Kendisine gönderilen bir sayının tam bölenlerini bir liste şeklinde döndüren fonksiyonu yazınız.

def tamBoleniBulunacak(x):
    tamBolenler = []
    for i in range(1, x+1):
        if (x % i == 0):
            tamBolenler.append(i)
    print(tamBolenler)

x = int(input("Hangi sayının Tam Bölenlerini bulmak istersiniz?: "))
tamBoleniBulunacak(x)
