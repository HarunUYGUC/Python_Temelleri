# 1- "Samsung S5, Samsung S6, Samsung S7, Samsung S8" eleman larına sahip bir liste oluşturunuz

telMarkalari = ["Samsung S5", "Samsung S6", "Samsung S7", "Samsung S8"]
print(telMarkalari)

# 2- Liste Kaç elemanlıdır ?

print(len(telMarkalari))

# 3- Listenin ilk ve son elemanı nedir ?

print("Listenin ilk elemanı:", telMarkalari[0])
print("Listenin son elemanı:", telMarkalari[-1])

# 4- "Samsung S5" değerini "Samsung S9" ile değiştirin.

telMarkalari[0] = "Samsung S9"
print(telMarkalari)

# 5- "Samsung S6" Listenin bir elemani midir ?

if "Samsung S6" in telMarkalari:
    print("Evet")

# 6- Listenin -3 indeksindeki değer nedir ?

print(telMarkalari[-3])

# 7- Listenin ilk 2 elemanını alın.

print(telMarkalari[0:2])

# 8- Listenin son 2 elemanı yerine "Samsung S9" ve "Samsung S10" değerlerini ekleyin.

telMarkalari[-2] = "Samsung S9"
telMarkalari[-1] = "Samsung S10"
print(telMarkalari)

# Diğer yöntem:
telMarkalari[-2:] = ["Samsung S9", "Samsung S10"]
print(telMarkalari)

# 9- Listenin üzerine "IPhone X" ve "IPhone XR" değerlerini ekleyin.

print(telMarkalari + ["Iphone X", "Iphone XR"])

# 10- Listenin son elemanını silin.

del telMarkalari[-1]
print(telMarkalari)

# 11- Liste elemanlarını tersten yazdırınız.

telMarkalari = ["Samsung S5", "Samsung S6", "Samsung S7", "Samsung S8"]
print(telMarkalari[::-1])

# 12- Aşağıdaki verileri bir liste içinde saklayınız.

     # kullaniciA: Yiğit Bilgi 2010, (70,60,70)
     
kullaniciA = ["Yiğit", "Bilgi", 2010, [70, 60, 70]]
     
     # kullaniciB: Sena Turan 1999, (80,80,70)
     
kullaniciB = ["Sena", "Turan", 1990, [80, 80, 70]]
     
     # kullaniciC: Ahmet Turan 1998, (80,70,90)

kullaniciC = ["Ahmet", "Turan", 1998, [80, 70, 90]]

kullanicilar = [kullaniciA, kullaniciB, kullaniciC]

for kullanici in kullanicilar:
     print(kullanici)
     print(kullanici[0])
     print(f"{kullanici[0]} {kullanici[1]}")
     print(f"{kullanici[0]} {kullanici[1]} {2022 - kullanici[2]} yaşında.")


# 13- Liste elemanlarini ekrana yazdırınız.

for x in telMarkalari:
    print(x)
