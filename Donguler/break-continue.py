isim = "Sadık Turan"

for karakter in isim:
    if (karakter != " "):
        print(karakter)

for karakter in isim:
    if (karakter == " "):
        continue
    print(karakter)


for karakter in isim:
    if (karakter == " "):
        break
    print(karakter)


i = 0

while (i < 5):
    if (i == 3):
        break
    print(i)
    i += 1

print("Döngü Bitti!")


# i = 0

# while (i < 5):
#     if (i == 3):
#         continue
#     print(i)
#     i += 1
# """ Bu kod satırı sonsuz döngüye girer."""

i = 0

while (i < 5):
    i += 1
    if (i == 3):
        continue
    print(i)


# 1-100 arasındaki çift sayılar toplamını bulunuz.
i = 0
toplam = 0

while (i < 100):
    i += 1
    if (i % 2 == 1):
        continue
    toplam = toplam + i

print(toplam)

