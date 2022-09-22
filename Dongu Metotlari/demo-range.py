# 1- Çarpım tablosu hazırlayınız.

for x in range(1,11):
    print("***********")
    print(f"{x}'lerin Çarpım Tablosu: ")
    for y in range(1,11):
        print(f"{x} * {y} = {x * y}")

# Diğer yöntem. Kurstan buldum.

for i in range(1, 10 + 1):
    print("")
    for k in range(1, 10 + 1):
        print(f"{i} x {k} = {i * k}", end="\t   ")


# 2- Girilen bir sayının asal olup olmadığını kontrol ediniz.
# Asal Sayı 1 ve kendisi hariç tam böleni olmayan sayılara denir.

sayi = int(input("Asal sayı olup olmadığını merak ettiğiniz sayıyı giriniz: "))
islem = int(sayi / 2 + 1)
bayrak = 0
liste = []


if (sayi < 0):
    print("Negatif Asal Sayı Olamaz!")
    bayrak = 1
elif (sayi == 0):
    print("0 Asal Sayı Değildir!")
    bayrak = 1
else:
    for x in range(2,islem):
        if (sayi % x == 0):
            liste.append(x)
            bayrak = 1

 
if (bayrak == 1):
    print(f"Sayınız {liste} listesindeki sayılara bölündüğü için Asal Sayı Değildir!")
else:
    print("Sayınız Asal Sayıdır!")            

