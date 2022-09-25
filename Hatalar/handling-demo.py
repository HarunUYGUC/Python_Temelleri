liste = ["1", "2", "5a", "10b", "abc", "10", "50"]

# 1: Liste elemanları içindeki sayısal değerleri bulunuz.
i = 0
while (i < len(liste)):
    try:
        print(f"Listedeki {int(liste[i])} sayısal bir veridir!")
    except:
        print(f"Listedeki {liste[i]} verisi sayısal veriye çevrilemez!")
    i += 1


# 2: Kullanıcı 'quit (q)' değerini girmedikçe aldığınız her inputun sayı
# olduğundan emin olunuz aksi halde hata mesajı yazın.

while True:
    sayi = input("Sayınızı Giriniz (Oyunu kapatmak için 'q'ya basınız): ")
    if (sayi == "q"):
        print("Oyunu kapattınız.")
        break
    else:
        try:
            print(f"Geçerli bir sayıyı {float(sayi)}'yi girdiniz. Oyun bitmiştir!")
            break
        except ValueError:
            print("Girdiğiniz değer sayısal bir ifade değlidir.")
            continue


# 3: Dictionary ve key bilgilerini parametre olarak alan get(d, key)
# fonksiyonu hazırlayınız.

urun = {"urunAdi": "samsung s10"}

# d["fiyat"] => KeyError

# get(d, "fiyat") => None
# get(d, "urunAdi") => samsung S10

def get(d, key):
    try:
        return d[key]
    except KeyError:
        return None

print(get(urun, "fiyat"))
print(get(urun, "urunAdi"))
