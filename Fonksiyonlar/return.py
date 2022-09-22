def toplam():
    print(f"Toplam: {10 + 20}")

toplam()


def toplam():
    return f"Toplam: {10 + 20}"

a = toplam()
print(a)


def toplam():
    return f"Toplam: {10 + 20}"

print(toplam())


def toplam():
    return 10 + 20

sonuc = toplam() + 50
print(sonuc)


def simdi():
    import datetime
    return datetime.datetime.now().year

def simdikiYas():
    return simdi() - 2003

print(simdikiYas())

def saat():
    import datetime
    return datetime.datetime.now().hour
    
print(saat())

def selamlama():
    if (saat() >= 0) and (saat() < 6):
        return "İyi Geceler!"
    elif (saat() >= 6) and (saat() <= 12) :
        return "Günaydın!"
    elif (saat() > 12) and (saat() <= 18):
        return "İyi Günler!"
    else:
        return "İyi Geceler!"

print(selamlama())

