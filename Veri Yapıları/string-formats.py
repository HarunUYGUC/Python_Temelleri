ad = "Harun"
soyad = "Uyguç"
yas = 18

print("My name is {} {}".format(ad,soyad))
print("My name is {0} {1}".format(ad,soyad))
print("My name is {1} {0}".format(ad,soyad))
print("My name is {n} {s}".format(n=ad,s=soyad))

print("My name is {} {}. I'm {} years old.".format(ad,soyad,yas))

number = 200 / 700
print("The result is {}".format(number))
print("The result is {}".format(round(number, 2)))
print("The result is {n:1.2}".format(n=number))
print("The result is {n:5.2}".format(n=number))

print(f"My name is {ad} {soyad} and I'm {yas} years old.")
print(f"The result is = {round(number, 2)}")


"""
print("My name is {} {}".format(ad, soyad))
print("My name is {} {}".format(n = ad, s = soyad))
# Böyle şık gözükmüyor.
"""
"""
print("Hello")
print("The result is {n:.2}".format(n=number))
print("The result is {n:2}".format(n=number))
"""