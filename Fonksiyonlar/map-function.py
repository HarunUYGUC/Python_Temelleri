sayilar = [1,2,5,7,9]
kareleri = []

for sayi in sayilar:
    kareleri.append(sayi**2)

print(kareleri)


sayilar = [1,2,5,7,9]

def kareAl(sayi):
    return sayi**2

print(list(map(kareAl, sayilar)))


sayilar = [1,2,5,7,9]

print(list(map(lambda sayi: sayi**2, sayilar)))


str_sayilar = ["1","2","5","7","9"]

print(list(map(int, str_sayilar)))


sayilar = [1-2,5,-7,9]

print(list(map(abs, sayilar)))


isimler = ["ali", "deniz", "emel", "çınar"]

print(list(map(str.capitalize, isimler)))

