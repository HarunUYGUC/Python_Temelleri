# 1- Kullanıcıdan aldığı ürün bilgisini (ad, fiyat) urunler.txt dosyasına kayıt eden fonksiyon.

def urun_ekle(ad, fiyat):
    with open(r"C:\Users\Harun\Desktop\Python_Temelleri\Dosya Yönetimi I-O\urunler.txt", "a", encoding="UTF-8") as file:
        file.write(f"Ad: {ad} | Fiyat: {fiyat} \n")

urun_ekle("Samsung S10", 5000)
urun_ekle("Samsung S11", 6000)


# 2- dosya ismi, eski kelime ve yeni kelime parametrelerini alarak dosyada bir güncelleme yapan fonksiyon.

def bul_ve_degistir(dosya_ismi, eski_kelime, yeni_kelime):
    with open(dosya_ismi, "r+") as file:
        text = file.read()
        yeni_text = text.replace(eski_kelime, yeni_kelime)
        file.seek(0)
        file.write(yeni_text)
        file.truncate() # Cursor'un geldiği son konumdan itibaren sona kadar bütün karakterleri siler. 
        # 20 byte'lık bir .txt dosyamız varken dosyadaki bir veriyi değiştirdikten sonra 19 byte vb. daha düşük bytelık veriye sahip olursak
        # fazladan kalan karakterleri siler ve boşa fazladan byte depolamada yer kaplamamış oluruz.
        # file.truncate(5) gibi bir değer yazarsak cursor bulunduğu konumdan itibaren 5 karakteri siler.

bul_ve_degistir(r"C:\Users\Harun\Desktop\Python_Temelleri\Dosya Yönetimi I-O\urunler.txt", "S10", "S9")
bul_ve_degistir(r"C:\Users\Harun\Desktop\Python_Temelleri\Dosya Yönetimi I-O\urunler.txt", "6000", "0")
