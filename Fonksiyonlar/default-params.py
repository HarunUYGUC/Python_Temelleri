# Kendimce bir şeyler denedim. :D :D :D

def selamlama(isim, gununVakti, cinsiyet):
    if (cinsiyet.lower() == "erkek"):
        if (gununVakti.lower() == "sabah"):
            print(f"{isim.upper()} Bey, günaydın!")
        elif (gununVakti.lower() == "öğlen"):
            print(f"{isim.upper()} Bey, iyi günler!")
        elif (gununVakti.lower() == "akşam"):
            print(f"{isim.upper()} Bey, iyi akşamlar!")
        else:
            print("Yanlış bilgi girdiniz!")
    elif (cinsiyet.lower() == "kız"):
        if (gununVakti.lower() == "sabah"):
            print(f"{isim.upper()} Hanım, günaydın!")
        elif (gununVakti.lower() == "öğle"):
            print(f"{isim.upper()} Hanım, iyi günler!")
        elif (gununVakti.lower() == "akşam"):
            print(f"{isim.upper()} Hanım, iyi akşamlar!")
        else:
            print("Yanlış bilgi girdiniz!")
    else:
        print("Yanlış bilgi girdiniz!")

isim = input("İsminizi giriniz: ")
cinsiyet = input("Cinsiyetinizi giriniz. (erkek, kız): ")
gununVakti = input("Günün hangi vakindesiniz? (sabah, öğle, akşam): ")
selamlama(isim, gununVakti, cinsiyet)

# Bittiş!


def selamlama(isim="Kullanıcı", mesaj="İyi Günler"):
    print(f"{mesaj} {isim}")

selamlama()


def toplam(a, b):
    return a + b

def cikarma(a, b):
    return a - b

def islem(a, b):
    print(toplam(a, b))
    print(cikarma(a, b))

a = int(input("1. Sayıyı Giriniz: "))
b = int(input("2. Sayıyı Giriniz: "))
islem(a, b)
