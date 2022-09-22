msg = "Python Kursumuza Hoş Geldiniz. Ben Sadık Turan."

print(msg)
print(msg[0])

print(msg.split())
print(msg.split()[0])
print(msg.split()[0][0])


sayilar = [1, 3, 5, 7, 9]

print(sayilar)
print(sayilar[0])


# Kendim denedim. Ne olduğunu anlamak için.
sayilar = 1, 3, 5, 7, 9
print(sayilar)
print(sayilar[0])
#.....

""" 
print(sayilar[5])
# IndexError: list index out of range

"""

sayilar = (1, 3, 5, 7, 9)
print(sayilar)
print(sayilar[0])
# .....


isimler = ["ahmet", "ali", "can", "ada"]

print(isimler)
print(isimler[0])

print(type(isimler[0]))
print(type(sayilar[0]))

print(type(isimler))
print(type(sayilar))


listeAli = ["ali", 20]
listeAhmet = ["ahmet", 22]

print(listeAli[0])
print(listeAli[1])
print(listeAhmet[0])


ogrenciler = [["ahmet", 20], ["ali", 22]]

print(ogrenciler[0])
print(ogrenciler[1])

print(ogrenciler[0][0])
print(ogrenciler[1][0])


# Kendim denedim. Ne olduğunu anlamak için.
ogrenciler = (("ahmet", 20),("ali", 22))
print(ogrenciler[0])
#....


