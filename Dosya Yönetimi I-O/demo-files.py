# def dosya_kopyala(dosa_ismi, yenş_dosya_ismi):
#     pass
# dosya_kopyala fonksiyonunu işlevsel hale getiriniz.


# def ters_cevir(dosya_ismi, yeni_dosya_ismi):
#     pass
# eski dosyadaki tüm içerikleri yeni dosyaya tersten yazdırınız.


# def bilgilendir(dosya_ismi):
#     pass
# fonksiyona gönderilen dosya içindeki verilerin özet bilgisini hazırlayınız.
# {"satir_sayisi": 52, "kelime_sayisi": 158, "karakter_sayisi": 1250}


def dosya_kopyala(dosya_ismi, yeni_dosya_ismi):
    with open(dosya_ismi) as file:
        icerik = file.read()

    with open(yeni_dosya_ismi, "w") as new_file:
        new_file.write(icerik)

dosya_kopyala(r"C:\Users\Harun\Desktop\Python_Temelleri\Dosya Yönetimi I-O\msg.txt", r"C:\Users\Harun\Desktop\Python_Temelleri\Dosya Yönetimi I-O\msg_yeni.txt")



def ters_cevir(dosya_ismi, yeni_dosya_ismi):
    with open(dosya_ismi) as file:
        icerik = file.read()

    with open(yeni_dosya_ismi, "w") as new_file:
        new_file.write(icerik[::-1])

ters_cevir(r"C:\Users\Harun\Desktop\Python_Temelleri\Dosya Yönetimi I-O\msg.txt", r"C:\Users\Harun\Desktop\Python_Temelleri\Dosya Yönetimi I-O\msg_ters.txt")



def bilgilendir(dosya_ismi):
    with open(dosya_ismi) as file:
        satirlar = file.readlines()

    sonuc = {
        "satir_sayisi": len(satirlar),
        "kelime_sayisi": sum(len(satir.split(" ")) for satir in satirlar),
        "karakter_sayisi": sum(len(satir) for satir in satirlar)
    }

    return sonuc

print(bilgilendir(r"C:\Users\Harun\Desktop\Python_Temelleri\Dosya Yönetimi I-O\msg.txt"))
print(bilgilendir(r"C:\Users\Harun\Desktop\Python_Temelleri\Dosya Yönetimi I-O\demo-file-sondaki.txt"))
