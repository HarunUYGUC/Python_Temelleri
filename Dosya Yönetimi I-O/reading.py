# Dosya açmak ve oluşturmak için open fonksiyonu kullanılır.
# Kullanımı: open(dosya_adi, dosya_erişme_modu)
# dosya_erişme_modu => dosyaı hangi amaçla açtığımızı belirtir.
# "r": okuma modu => belirtilen konumda dosya olmalıdır.

# dosya_erişme_modu nu belirtmezsek "r" varsayılan olarak tanımlandığı için open() fonksiyonu açmak istediğimiz dosyayı "okuma modu"nda açar.
# open() fonksiyonu ilgili klasör içerisindeki dosyaları arar ve eğer varsa belirttiğimi moda göre işlem yapar.

# Mod "r" ise erişmek istediğimiz dosyanın o klasör içerisinde olması gerekmektedir. Eğer yoksa hata alırız. Çünkü olmayan bir dosyayı okumaya çalışıyoruz.

f = open(r"c:\Users\Asus\Desktop\Python_Temelleri\Dosya Yönetimi I-O\msg.txt") # open() fonksiyonu ile "msg.txt" dosyasını okumaya çalıştığımızda bir f nesnesi dönecektir.

"""f = open("msg.txt")""" # Videoda çalışıyor ama bende çalışmıyor.
"""print(f)""" # Videoda çalışıyor ama bende çalışmıyor.

print(help(f)) # help() fonksiyonu ile f nesnesinin sınıfına ait metotlara ulaşıyoruz. Help dökümanından çıkmak için "q"ya basmalıyız.
print(f.read())
