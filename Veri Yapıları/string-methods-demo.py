from turtle import clear


website = "http://www.sadikturan.com"
kursAdi = "Python Dersleri: Sıfırdan İleri Seviye Python Programlama."

# " Hello World " karakter dizisinin baş ve sondaki boşluk karakterlerini silin.
msg = " Hello World "
print(msg.strip())

print(msg.lstrip())
print(msg.rstrip())

print(website.lstrip("/pthw."))
print(website.lstrip("/pthw.:"))

# "www.sadikturan.com" içindeki sadikturan bilgisi haricindeki her karakteri silin.
msg = "www.sadikturan.com"
print(msg.split(".")[1])

msg = "www.sadikturan.com"
print(msg.strip("w.moc"))

# "kursAdi" karakter dizisinin tüm karakterlerini küçük harf yapın.
print(kursAdi.lower())

# "website" içinde kaç tane a karakteri vardır? (count('a'))
print(website.count("a"))

print(website.count("w"))
print(website.count("www"))
print(website.count("www", 9,15))

# "website" "www" ile başlayıp "com" ile bitiyor mu?
print(website.startswith("www"))
print(website.endswith("com"))

print(website.startswith("http"))  

# "website" içinde ".com" ifadesi var mı?
print(website.find(".com"))

print(website.find(".com", 0,10))
print(kursAdi.find("Python"))
print(kursAdi.rfind("Python"))

print(kursAdi.index("Python"))
print(kursAdi.rindex("Python"))

# "kursAdi" içindeki karakterlerin hespi alfabetik mi?
print(kursAdi.isalpha())
print(kursAdi.isdigit())

print("Merhaba".isalpha())
print("123".isdigit())

# "Contents" ifadesini satırda 50 karakter içine yerleştirip sağ ve soluna * ekleyiniz.
print(len(kursAdi))
print(kursAdi[:50] + "*Contents*" + kursAdi[50:])

msg = "Contents"
print(msg.center(50, "*"))
print(msg.ljust(50, "*"))

# "kursAdi" karakter dizisindeki tüm boş luk karakterlerini '-' ile değiştirin.
print(kursAdi.replace(" ", "-"))

# "Hello World" karakter dizisinin 'World' ifadesini 'There' olarak değiştirin
msg = "Hello World"
print(msg.replace("World", "There"))

print("Hello World".replace("World", "There"))

# "kursAdi" karakter dizisini boşluk karakterlerinden ayırın.
print(kursAdi.split(" "))

print(kursAdi.split())
print(kursAdi.replace(":", " ").lower().split())


# Deneme
print("Sadık Turan".isalpha()) 
# Arada bir karakter boşluk olduğu için yani tüm karakterler alfabede olmadığı
#için False sonucunu alırız.

print("SadıkTuran".isalpha())
# Arada bir karakter boşluk olmadığı için yani tüm karakterler alfabede olduğu
#için True sonucunu alırız.