def multiply(a):
    print(a**2)

a = float(input("Karesini almak istediğiniz sayıyı giriniz: "))
multiply(a)


def multiply(a):
    return a**2

a = float(input("Karesini almak istediğiniz sayıyı giriniz: "))
multiply(a)

print(multiply(a))

# Lambda Fonksiyonunu kullanarak aynı sonucu alabiliriz.

sonuc = (lambda a: a**2)(a)

a = float(input("Karesini almak istediğiniz sayıyı giriniz: "))

print(sonuc)


multiply = lambda a: a**2

a = float(input("Karesini almak istediğiniz sayıyı giriniz: "))
print(multiply(a))


toplama = lambda x,y,z: x + y + z

x = float(input("Toplamak istediğiniz sayıyı giriniz: "))
y = float(input("Toplamak istediğiniz sayıyı giriniz: "))
z = float(input("Toplamak istediğiniz sayıyı giriniz: "))

sonuc = toplama(x,y,z)

print(sonuc)


tersCevir = lambda s: s[::-1]

s = input("Ters çevirmek istediğiniz metinsel ifadeyi giriniz: ")
print(tersCevir(s))


def myFunc(n):
    return lambda a: a * n

multiply2 = myFunc(2)

sonuc = multiply2(10)

print(sonuc)
