x = int(input("x: "))
y = int(input("y: "))

print(x / y)

"""
Yukarıdaki gibi bir kod yazınca y'ye 0 bilgisini girersek "ZeroDivisionError: division by zero" 
hatasını alırız.
y'ye a veya 10a gibi bir bilgi girersek "ValueError" hatasını alırız.
Bizim bu hatalardan biri çıkınca onunla ilgili bir mesajı kullanıcıya vermemiz gereklidir, bu yüzden
hataya uygun bir mesaj nasıl verilir onu öğrenmeliyiz.
"""

# SyntaxError => Yazım Yanlışı Hatası
"""
def yazdir((:
    pass

print("Merhab"a)
"""

# NameError => Tanımlanmamış Bir Değişken Kullanımı Hatası 
"""
print(ad)
"""

# TypeError => Hatalı Parametre Kullanımı Hatası
"""
len(5)

4 + "a"
"""

# IndexError => Yanlış Index Numarası Hatası 
"""
liste = ["Merhaba"]
print(liste[1])
"""

# ValueError => Hatalı Tip Kullanımı Hatası
"""
print(int("10a"))
"""

# KeyError => Key (Anahtar) Hatası 
"""
d = {}
print(d["ad"])
"""

#  AttributeError => Olmayan Bir Özelliğe Ulaşmaya Çalışma Hatası
"""
print("Merhaba".Upper())
"""
