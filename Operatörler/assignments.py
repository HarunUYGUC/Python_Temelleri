a = 5
b = 10
c = 20

print(a,b,c)

# 
a, b, c = 5, 10, 20

print(a,b,c)

#
a, b = b, a

print(a,b,c)

# Bu iki sonuçta da a değişenine 5 ekledik ve a'nın değeri 5 artmış oldu.
a = a + 5
print(a)

a += 5
print(a)


# Diğer matematiksel operatörler ile işlemler.
a, b, c = 5, 10, 20

a -= 5   
a = a - 5

a *= 5
a = a * 5

a /= 5
a = a / 5

a //= 5
a = a // 5

a **= 5
a = a ** 5

a %= 5
a =  a % 5

#
values = (1, 2, 3)
a, b, c = values
print(a,b,c)


values = (1, 2, 3, 4, 5)
a, b, *c = values
print(a,b,c)

values = (1, 2, 3, 4, 5)
a, *b, c = values
print(a,b,c)