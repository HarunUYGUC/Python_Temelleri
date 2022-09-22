# 1) Girilen bir sayının 50-100 arasında olup olmadığının kontrol ediniz.
x = float(input("Sayınızı Giriniz: "))

if (x >= 50) and (x <= 100):
    print("Sayınız 50-100 arasındadır!")
else:
    print("Sayınız 50-100 arasında değildir.")


# 2) Girilen bir sayının pozitif tek sayı olup olmadığının kontrol ediniz.
x = int(input("Sayınızı Giriniz: "))

isRight = (x > 0) and (x % 2 == 1)

if (isRight):
    print("Sayınız pozitif tek sayıdır.")
else:
    print("Sayınız pozitif tek sayı değildir.")


y = int(input("Sayınızı Giriniz: "))

if (y > 0):
    if (y % 2 == 1):
        print("Sayınız pozitif tek sayıdır!")
    else:
        print("Sayınız pozitif ancak tek değildir!")
else:
    print("Sayınız negatiftir, yani çift, tek bakmamıza gerek kalmadı!")

# 3) username ve parola bilgileri ile giriş kontrolü yapınız.
_username = "sadikturan"
_password = "1234"

username = input("Kullanıcı Adınızı Giriniz: ")
password = input("Şifrenizi Giriniz: ")

if (_username == username):
    if (_password == password):
        print("Uygulmaya Hoş Geldiniz!")
    else:
        print("Kullanıcı Adınız Doğru Fakat Şifreniz Hatalı!")
else:
    print("Kullanıcı Adınız Hatalı!")


# 4) Girilen 3 sayıyı büyüklük olarak karşılaştırınız.
x = float(input("x: "))
y = float(input("y: "))
z = float(input("z: "))

if (x > y):
    print("x, y'den büyüktür.")
elif (x == y):
    print("x, y'ye eşittir.")
else:
    print("y, x'den büyüktür.")


if (x > z):
    print("x, z'den büyüktür.")
elif (x == z):
    print("x, z'ye eşittir.")
else:
    print("z, x'den büyüktür.")


if (y > z):
    print("y, z'den büyüktür.")
elif (y == z):
    print("y, z'ye eşittir.")
else:
    print("z, y'den büyüktür.")


# 5) Kullanıcıdan 2 Vize (%60) ve Final (%40) notunu alıp ortalama hesaplayınız.
#   Eğer ortalama 50 üstündeyse geçti, altındaysa kaldı yazdırınız.
#   a-) Ortalama 50 olsa bile Final notu en az 50 olmalıdır.
#   b-) Finalden 70 alındığında ortalamanın bir önemi olmasın.
vize1 = int(input("1. Vize: "))
vize2 = int(input("2. Vize: "))
final = int(input("Final: "))

ortalama = ((vize1 + vize2)/2 * 0.6) + (final * 0.4)
yaklasıkOrt = round(ortalama, 2)

if (final >= 70):
    print(f"Final 70'in üzerinde olduğu için {yaklasıkOrt} ile direkt olarak Geçtiniz!")
else:
    if (final >= 50):
        if (ortalama >= 50):
            print(f"Sınıfı {yaklasıkOrt} ile Geçtiniz!")
        else:
            print(f"Final 50'nin üzerinde fakat ortalamanız {yaklasıkOrt} yani 50'nin altında, Kaldınız!")
    else:
        print(f"Final notunuz 50'nin altında olduğu için Kaldınız! Ortalamanız: {yaklasıkOrt}")


# 6) Kişinin ad, kilo ve boy bilgilerini alıp kilo indekslerini hespalayınız.
#   Formül: (Kilo / Boy uzunluğunun karesi)
#   Aşağıdaki tabloya göre kişi hangi gruba girmektedir?
#   0-18.4      => Zayıf
#   18.5-24.9   => Normal
#   25-29.9     => Fazla Kilolu
#   30-34.9     => Şişman (Obez)

name = input("Adınız: ")
weight = float(input("Kilonuz: "))
height = float(input("Metre Cinsinden Boyunuz: "))

kiloIndex = weight / height**2
yaklasikIndex = round(kiloIndex, 2)

if (kiloIndex >= 0) and (kiloIndex <= 18.4):
    print(f"{name} isimli kişi, {yaklasikIndex} ortlama ile Zayıfsınız!")
elif (kiloIndex > 18.4) and (kiloIndex <= 24.9):
    print(f"{name} isimli kişi, {yaklasikIndex} ortlama ile Normalsiniz!")
elif (kiloIndex > 24.9) and (kiloIndex <= 29.9):
    print(f"{name} isimli kişi, {yaklasikIndex} ortlama ile Fazla Kilolusunuz!")
elif (kiloIndex > 29.9) and (kiloIndex <= 34.9):
    print(f"{name} isimli kişi, {yaklasikIndex} ortlama ile Şişmansınız! (Obezsiniz!)")
