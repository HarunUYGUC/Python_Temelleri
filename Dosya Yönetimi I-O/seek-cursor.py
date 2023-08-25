f = open(r"c:\Users\Asus\Desktop\Python_Temelleri\Dosya Yönetimi I-O\msg-2.txt")
print(f.read())
print(f.read())

# Terminal'e python yazarak Python moduna giriş yaparız. PS C:\Users\Asus\Desktop\Python_Temelleri> python
# Terminal'e quit() yazarak ise Python modundan çıkış yaparız.


# msg.txt dosyası içerisindeki bu yazıları f.read() dediğimiz anda hepsini okuruz. Yani cursor boş satırın sonuna gider. Boş satırı \n ile gösterir.
# Boş satıra ekleme yaptığıktan sonra tekrar f.read() dersek sadece ekleme yaptığımız satır okunur, öncekiler okunmaz.
# İki satır arasındaki boş satıra ekleme yaparsak o satır ve altındaki satırı okur.
""" 
Hello World.
evavaeva
adssada

"""
print("*" * 10)

f.seek(0) # seek() fonksiyonu sayesinde cursor'u istediğimiz indeksin başına getirebiliriz. seek(0) dersek cursor en başa döner.
print(f.read())


print("*" * 10)

f.seek(5)
print(f.read())


print("*" * 10)

f.seek(0)
print(f.readline()) # Cursor'un olduğu satırın sonuna kadar okur. Cursor alt satıra geçer.
print(f.readline())
print(f.readline())


print("*" * 10)

f.seek(0)
print(f.readlines()) # Bütün satırları bir dizinin içerisinde satır satır yazar.


print("*" * 10)

f.seek(0)
satirlar = f.readlines()
print(satirlar)
print(satirlar[2])

print(f.closed) # Dosya kapalı mı diye sorduk. Kapalı olmadığı için False cevabını aldık.
f.close() # Dosyayı kapattık.
print(f.closed) # Dosya kapalı mı diye sorduk. Kapalı olduğu için True cevabını aldık.

"""f.seek(0)""" # ValueError: I/O operation on closed file.
