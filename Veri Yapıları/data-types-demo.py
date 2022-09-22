# 1. soru için çözümüm:

r = input("Yarı Çap Uzunluğunu Giriniz: ")
r = float(r)
cevre = 2 * 3.14 * r
alan = 3.14 * r ** 2
print("Çevre =", cevre)
print("Alan =", alan)

# 2. soru için çözümüm:

print("Kaç kilometre yol gittiniz?")
x = input("km bilgisi: ")
x = float(x)
mil = x / 1.609344
print("km'nin mil cinsinden değeri =", mil)


# 1. soru için başka yöntem:

pi = 3.14
r = float(input("Yarı Çapı Giriniz = "))
cevre = 2 * pi * r
alan = pi * r ** 2
print("Alan =", alan, "Çevre =", cevre) # Bunu yapmak daha mantıklı.
print("Alan = " + str(alan) + " Çevre = " + str(cevre)) # Buna göre.


print("Diğer Çözüm")

result = "Alan =", alan, "Çevre =", cevre # Burada da üstte kolay olan yöntemi yapmak
print(result) # saçma oldu.

result = "Alan = " + str(alan) + " Çevre = " + str(cevre) # Burada ise üstte zor olan
print(result) # yöntemi yapmak mantıklı oldu.

# Ama genel olarak en mantıklı yöntem üsttekinin kolay olanını yapmak.
