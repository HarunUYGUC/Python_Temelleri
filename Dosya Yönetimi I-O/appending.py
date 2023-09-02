# open(dosaya_adi, dosya_erişim_modu)
# dosya_erişim_modu => Dosyayı hangi amaçla açtığımızı belirtir.


# "r" => (Read) Okuma modu. Dosya konumda yoksa hata verir.

# "w" => (Write) Yazma modu. 
#     ** Dosyayı konumda oluşturur.
#     ** Dosya içeriğini siler ve yeniden ekleme yapar.

# "a" => (Append) Ekleme modu. Dosya konumda yoksa oluşturur.
#     ** Eklenecek her veri dosyanın sonuna eklenir. Bu durumu değiştiremeyiz.

# "r+" => Hem okuma hem yazma modunda açılır. Dosya konuma yoksa hata verir.
#      ** Yazma modundayken eklenecek veri en başa eklenir. seek ile eklenecek konumu değiştirebiliriz.
#      ** Konumu değiştirdiğimizde orada başka bir veri var ise yeni veri onun üzerine yazılır yani önceki veri silinir.

""" Olmayan bir şeyi okuyamayacağımıza göre okuma modunda iken o dosya yoksa hata verecektir. """
""" Yazma veya ekleme modunda ise yazmak/eklemek istediğimiz dosyayı oluşturacaktır. Yazmak/Eklemek istiyorsan bir şey bulmak zorundasındır. """


with open(r"c:\Users\Harun\Desktop\Python_Temelleri\Dosya Yönetimi I-O\msg-2.txt", "a") as file:
    file.write("altıncı satır \n")
    file.write("yedinci satır \n")
    file.write("Yukarıdaki altı ve yedide encoding belirtmedim \n")

with open(r"c:\Users\Harun\Desktop\Python_Temelleri\Dosya Yönetimi I-O\msg-2.txt", "a", encoding="UTF-8") as file:
    file.write("altıncı satır \n")
    file.write("yedinci satır \n")
    file.write("encoding='UTF-8' olarak belirttim \n")


with open(r"c:\Users\Harun\Desktop\Python_Temelleri\Dosya Yönetimi I-O\msg-2.txt", "r+", encoding="UTF-8") as file:
    file.write("yeni satır \n")

with open(r"c:\Users\Harun\Desktop\Python_Temelleri\Dosya Yönetimi I-O\msg-2.txt", "r+", encoding="UTF-8") as file:
    file.seek(10)
    file.write("üzerine eklenecek satır \n")

with open(r"c:\Users\Harun\Desktop\Python_Temelleri\Dosya Yönetimi I-O\msg-2.txt", "r+") as file:
    file.read()
    file.write("sonuna kadar okunacak, daha sonra bu satır eklenecek \n")
