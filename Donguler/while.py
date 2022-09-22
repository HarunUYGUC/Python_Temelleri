sayilar = [2,5,7,9]

i = 0

while (i < 10):
    print(i)
    i += 1

while (i <= 100):
    if (i % 2 == 1):
        print("Tek Sayı:", i)
    else:
        print("Çift Sayı:", i)
    i += 1


username = ""

while not username:
    username = input("Kullanıcı adınızı giriniz: ")

print("Girdiğiniz kullanıcı adı:", username)
