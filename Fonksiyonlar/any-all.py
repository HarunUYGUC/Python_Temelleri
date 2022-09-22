print(all([True, True, False]))

print(all([True, True, True]))


print(any([True, True, False]))

print(any([True, True, True]))

print(any([False, False, False]))


# and => True and True => True => all()
# or => True or False => True => any()

sayilar = [1, 3, 6, 8, 9, 10]

sonuc = [bool(sayi) for sayi in sayilar]
print(sonuc)

sonuc = all([bool(sayi) for sayi in sayilar])
print(sonuc)


sayilar = [0, 1, 3, 6, 8, 9, 10]

sonuc = [bool(sayi) for sayi in sayilar]
print(sonuc)

sonuc = all([bool(sayi) for sayi in sayilar])
print(sonuc)


sayilar = [0, 1, 3, 6, 8, 9, 10]

sonuc = all([sayi % 2 == 0 for sayi in sayilar])
print(sonuc)


sayilar = [0, 1, 3, 6, 8, 9, 10]

sonuc = any([sayi % 2 == 0 for sayi in sayilar])
print(sonuc)
