import os
import datetime

# result = dir(os)
# print(result)

# result = os.name
# print(result)

# result = os.getcwd()
# print(result)

"""Klasörün  konumlanacağı dizini değiştiririz. change directory nin kısaltması"""
# os.chdir("C:\\")

"""Bu dizin içerisinde yeni klasör oluştururuz. make directory nin kısaltması"""
# os.mkdir("newdirectory")

"""Klasörün adını değiştirmek için."""
# os.rename("newdirectory", "yeniklasör")

"""Üst dizindeki klasörü silmek için."""
# os.rmdir("newdirectory")

"""Alt dizindeki klasörü silmek için."""
# os.removedirs("yeniklasör/yeniklasör")

"""Bir alt klasöre geçiş yaparız."""
# os.chdir("..")

"""Bir alt klasörün de altındaki klasöre geçiş yaparız."""
# os.chdir("../..")

"""Klasör içerisinde klasör oluşturmaya yarar."""
# os.makedirs("newdirectory/yeni klasör")

"""İlgili dizin içerisindeki klasörleri listeler."""
# result = os.listdir()
# print(result)

"""Listeleme yaparken filtre kullanmak. Yani istediğimiz addaki klasörleri bulmak için."""
# for dosya in os.listdir():
#     if (dosya.endswith(".py")):
#         print(dosya)

"""Bir dosya hakkında bilgi sahibi olmak için."""
# result = os.stat("_datetime.py")
# print(result)

"""Kilobayt cinsinden dosyanın boyutunu göstermek için."""
# result = result.st_size/1024
# print(result)

"""Dosyanın anlamadığımız şekilde olan zaman bilgilerini 
anladığımız şekilde yazdırmak için."""
# result = datetime.datetime.fromtimestamp(result.st_ctime) # Oluşturulma tarihi.
# print(result)

"""Bilgisayardaki bir programı çalıştırmak için."""
# os.system("notepad.exe")

"""Dosyanın konumunu göstermek için."""
# result = os.path.abspath("_os.py")
# print(result)

"""Dosyanın dizinini göstermek için."""
# result = os.path.abspath("C:/Users/LNV/Desktop/Python Çalışmalarım/Python_Temelleri/_os.py")
# print(result)

"""2. YOL:"""
# result = os.path.dirname("os.path.abspath("_os.py")")
# print(result)

"""Dosyanın veya klasörün olup olmadığını anlamak için."""
# result = os.path.exists("_os.py")
# print(result)

"""Adresini (dizin) belirttiğimizin klasör olup olmadığını anlamak için."""
# result = os.path.isdir("C:/Users/LNV/Desktop/Python Çalışmalarım/Python_Temelleri")
# print(result)

"""Adresini (dizin) belirttiğimizin dosya olup olmadığını anlamak için."""
# result = os.path.isfile("C:/Users/LNV/Desktop/Python Çalışmalarım/Python_Temelleri/_os.py")
# print(result)

"""Dizin oluşturmak için."""
# result = os.path.join("C:\\", "deneme", "deneme1")
# print(result)

"""Dizini bölmek için."""
# result = os.path.split("C:\\deneme")
# print(result)

"""Dosyanın ismiyle uzantısını ayırmak için."""
# result = os.path.splittext("_os.py")
# print(result)

"""Devam... Dosyanın ayırdığımız özelliklerini ayrı ayrı yazdırmak için."""
# indexs1 = result[0]
# print(indexs1)
# indexs2 = result[1]
# print(indexs2)
