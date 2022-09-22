website = "http://www.sadikturan.com"
kursAdi = "Python Dersleri: Sıfırdan İleri Seviye Python Programlama."

# "kursAdi" karakter dizisinde kaç karakter bulunmaktadır?
print(len(kursAdi))

# "website" içinden www karakterlerini alın.
print(website[7:10])

# "website" içinden com karakterlerini alın. 
print(website[-3:])

karakterSayisi = len(website)
print(website[karakterSayisi-3:])

print(website[len(website)-3:])


# "kursAdi" içinden ilk 15 ve son 15 karakterlerini alın.
print(kursAdi[:16])
print(kursAdi[-15:])

# "kursAdi" ifadesindeki karakterleri tersten yazdırın.
print(kursAdi[::-1])


# "Hello world" ifadesindeki w harfini W ile değiştirin.
yeni = "W"
print(f"Hello {yeni}orld")

# "Hello world" ifadesindeki w harfini W ile değiştirin. HOCANIN YÖNTEMİ:
s = "Hello world"
s = s[0:6] + "W" + s[-4:]
print(s)


# "abc" ifadesini yan yana 3 defa yazdırın.
yaz = "abc"
print(f"{yaz} {yaz} {yaz}")
print("{0} {0} {0}".format(yaz))

# "abc" ifadesini yan yana 3 defa yazdırın. HOCANIN YÖNTEMİ:
print("abc" * 3) 


name, surname, age, job = "Sadık", "Turan", 37, "Eğitimci"
# Yukarıdaki değişkenler ile ekrana aşağıdaki ifadeyi yazdırınız.
# "Benim adım Bora Yılmaz, yaşım 32 ve mesleğim mühendis."
print(f"Benim adım {name} {surname}, yaşım {age} ve mesleğim {job}.")
print("Benim adım {} {}, yaşım {} ve mesleğim {}.".format(name,surname,age,job))

