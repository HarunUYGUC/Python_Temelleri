sayilar = [4,6,9,10,35,57,89,125,244]

# 1: sayilar listesini while ile ekrana yazdırın.
for x in sayilar:
    print(x)


i = 0

while (i < len(sayilar)):
    print(sayilar[i])
    i += 1


# 2: Başlangıç ve bitiş değerlerini kullanıcıdan alıp aradaki tüm tek sayıları
# ekrana yazdırın.
baslangıc = int(input("Başlangıç değerini giriniz: "))
bitis = int(input("Bitiş değerini giriniz: "))

while (baslangıc <= bitis):
    if (baslangıc % 2 == 1):
        print(baslangıc)
    baslangıc += 1

        
# 3: 1-100 arasındaki sayıları azalan şekilde yazdırın.
i = 100

while (i > 0):
    print(i)
    i -= 1


# 4: Kullanıcıdan alacağınız 5 sayıyı ekranda küçükten büyüğe sıralı bir şekilde yazdırın.
sayilar = []
i = 1

while (i <= 5):
    x = int(input(f"{i}. sayıyı giriniz: "))
    sayilar.append(x)
    i += 1

sayilar.sort()
print(sayilar)
