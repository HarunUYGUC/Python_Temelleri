# 5000 ve 6000 TL'lik bir ürün var ve %18 KDV eklenmiş halini hesaplayacağız.
print(5000 + 5000 * 18 / 100)
print(6000 + 6000 * 0.18)

# Şimdi değişken tanımlayarak bu işlemleri yapacağız.
urunA = 5000
urunB = 6000
kdv = 0.18
print(urunA + urunA * kdv)
print(urunB + urunB * kdv)


# Değişken tanımlarken böyle de tanımlayabiliriz.
a = 10
b = 20
c = 30
print(a)
print(b)
print(c)

print(a, b, c)

# Değişken tanımlarken böyle de tanımlayabiliriz.
d, e, f = 40, 50, 60
print(d, e, f)

print(d)
print(e)
print(f)



x = 1
y = 2.5

print(type(x))
print(type(y))

name = "Harun"
print(type(name))

name1, name2 = "Harun", "Max"
print(type(name1))
print(type(name2))

isStudent = True
isStudent = False
print(type(isStudent))


x, y, name, isStudent = 1, 2.5, "Harun", False
print(x, y, name, isStudent)

# İşlem yaparken veri tipine göre işlem yapmayı dikkat etmeliyiz.
a, b = 10, 20
toplam = a + b
print(toplam)

# Buradaki gibi hatalı bir sonuç almamak için.
c, d = "10", "20"
toplam1 = c + d 
print(toplam1)

