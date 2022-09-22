a, b, c = 2, 5, 10

# 1) Kullanıcıdan aldığınız 2 sayının çarpımı ile a, b, c toplamının farkı nedir?
x = int(input("x: "))
y = int(input("y: "))

carpim = x * y
toplam = a + b + c

print(carpim - toplam)

# 2) c'nin b'ye kalansız bölümünü hesaplayınız.
print(c // b)

sonuc = c // b
print(sonuc)

# 3) (a, b, c) toplamının mod 3'ü nedir?
sonuc2 = a + b + c
cevap = sonuc2 % 3
print(cevap)

print((a + b + c) % 3)

# 4) b'nin a. kuvvetini hesaplayınız.
print(b**a)

# 5) a, *b, c = sayilar işlemine göre c'nin küpü kaçtır?
# sayilar = 1, 5, 7, 10, 3

sayilar = 1, 5, 7, 10, 3
a, *b, c = sayilar

print(a, b, c)
print(c**3)


# 6) a, *b, c = sayilar işlemine göre b'nin değerleri toplamı kaçtır?
sayilar = 1, 5, 7, 10, 3
a, *b, c = sayilar 

x, y, z = b
print(x + y + z)

# 2. yöntem:
sayilar = 1, 5, 7, 10, 3
a, *b, c = sayilar 

print(b[0] + b[1] + b[2])

