# 1) Girilen bir sayının 50-100 arasında olup olmadığını kontrol ediniz.
x = int(input("x: "))

sonuc = (x > 50) and (x < 100)

print(f"{x} sayısı 50 ile 100 arasındadır: {sonuc}")



# 2) Girilen bir sayının pozitif tek sayı olup olmadığının kontrol ediniz.
x = int(input("x: "))

sonuc = (x > 0) and (x % 2 == 1)

print(f"{x} sayısı pozitif tek sayıdır: {sonuc}")



# 3) Username ve parola bilgileri ile giriş kontrolü yapınız.
_username = "Harun Uyguç"
_password = "159357"

username = input("Username: ")
password = input("Password: ")

sonuc = (username == _username) and (password == _password)

print(sonuc)

kontrol1 = (username == _username)

print(f"{username} bilginiz: {kontrol1}")

kontrol2 = (password == _password)

print(f"{password} bilginiz: {kontrol2}")



# 4) Girilen 3 sayıyı büyüklük olarak karşılaştırınız.
x = float(input("x: "))
y = float(input("y: "))
z = float(input("z: "))

xy = (x > y)
xz = (x > z)
yz = (y > z)

sonucxy = (f"x: {x}, y: {y}'den büyüktür: {xy}")
sonucxz = (f"x: {x}, y: {z}'den büyüktür: {xz}")
sonucyz = (f"x: {y}, y: {z}'den büyüktür: {yz}")

print(sonucxy)
print(sonucxz)
print(sonucyz)



# 5) Kullanıcıdan 2 Vize (%60) ve Final (%40) notunu alıp ortalama hesaplayınız.
#   Eğer ortalama 50 üstündeyse geçti, altındaysa kaldı yazdırınız.
#   a-) Ortalama 50 olsa bile Final notu en az 50 olmalıdır.
#   b-) Finalden 70 alındığında ortalamanın bir önemi olmasın.

vize1 = float(input("1. Vize: ")) 
vize2 = float(input("2. Vize: ")) 
final = float(input("Final: ")) 

ortalama = ((vize1 + vize2)/2 * 0.6) + (final * 0.4)

cevap = (final >= 70) or ((ortalama >= 50) and (final >= 50))

sonuc = (f"{ortalama} ortalama ve {final} final notu ile sınıfı geçtiniz mi: {cevap}")

print(sonuc)



# 6) Kişinin ad, kilo ve boy bilgilerini alıp kilo indekslerini hespalayınız.
#   Formül: (Kilo / Boy uzunluğunun karesi)
#   Aşağıdaki tabloya göre kişi hangi gruba girmektedir?
#   0-18.4      => Zayıf
#   18.5-24.9   => Normal
#   25-29.9     => Fazla Kilolu
#   30-34.9     => Şişman (Obez)

name = input("İsim: ")
weight = float(input("Kilo: "))
height = float(input("Metre Cinsinden Boy: "))

oran = weight / (height**2)
ortalamaDegeri = round(oran, 2)

zayif1 = (oran >= 0) and (oran <= 18.4)
normal1 = (oran > 18.4) and (oran <= 24.9)
kilolu1 = (oran > 24.9) and (oran <= 29.9)
şişman1 = (oran > 29.9) and (oran <= 34.9)

zayıf2 = (f"{name} isimli, {weight} kilodaki ve {height} uzunluğundaki kişi {ortalamaDegeri} ile Zayıf mı?: {zayif1}")
print(zayıf2)

normal2 = (f"{name} isimli, {weight} kilodaki ve {height} uzunluğundaki kişi {ortalamaDegeri} ile Normal mi?: {normal1}")
print(normal2)

kilolu2 = (f"{name} isimli, {weight} kilodaki ve {height} uzunluğundaki kişi {ortalamaDegeri} ile Kilolu mu?: {kilolu1}")
print(kilolu2)

şişman2 = (f"{name} isimli, {weight} kilodaki ve {height} uzunluğundaki kişi {ortalamaDegeri} ile Şişman mı?: {şişman1}")
print(şişman2)
