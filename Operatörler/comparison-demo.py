# 1) Girilen 2 sayıdan hangisi büyüktür?
x = int(input("x: "))
y = int(input("y: "))

sonuc = (x > y)

print(f"{x} {y}'den büyüktür: {sonuc}")


# 2) Girilen bir sayının tek mi, çift mi olduğunu yazdırınız.
x = int(input("x: "))

sonuc = ((x % 2) == 0)

print(f"{x} çift sayıdır: {sonuc}")


# 3) Girilen bir sayının negatif, pozitif durumunu yazdırınız?
x = int(input("x: "))

sonuc = (x > 0)

print(f"{x} sayısı pozitiftir: {sonuc}")


# 4) Kullanıcıdan 2 Vize (%60) ve Final (%40) notlarını alıp ortalamasını hesaplayınız.
#   Eğer ortalama 50 ve üzerindeyse geçti değilse kaldı yazdırınız.
vize1 = float(input("1. Vize Notu: "))
vize2 = float(input("2. Vize Notu: "))
final = float(input("Final Notu: "))

vizeDeger = (vize1 + vize2)/2 * 6/10
finalDeger = final * 4/10

ortalama = vizeDeger + finalDeger

gecmeDurumu = (ortalama >= 50)

print(f"{ortalama} ortalama ile sınıf geçme durumunuz: {gecmeDurumu}")


# 5) Parola ve e-mail bilgisini isteyip doğruluğunu kontrol ediniz.
# e-mail: info@sadikturan.com    parola: 12345
_email = "info@sadikturan.com"   # Bu iki bilgiyi veri tabanındaki bilgiler olarak 
_password = "12345"              # düşünebiliriz. Yani bu bilgiler kullanıcının  
                                 # uygulamaya kayıt olurken girdiği bilgiler.
email = input("e-mail: ")
password = input("password: ")

kontrol1 = (email == _email)
kontrol2 = (password == _password)

print(f"{email} bilginizin doğruluğu: {kontrol1}")
print(f"{password} bilginizin doğruluğu: {kontrol2}")
