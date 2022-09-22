#Uygulama 1 İçin Çözümüm

ogrenciAdi, ogrenciSoyadi, ogrenciNumarasi = "Harun", "Uyguç", 201104340
ogrenciCinsiyeti, ogrenciTC, ogrenciDogumTarihi = "Erkek", 15538650601, "19/07/2003"
ogrenciAdres, ogrenciYas = "AYDIN/Çine", 18
print(ogrenciAdi, ogrenciSoyadi, ogrenciNumarasi, ogrenciCinsiyeti, ogrenciTC, ogrenciDogumTarihi)
print(ogrenciAdres, ogrenciYas)

ogrenciAd = "Harun"
ogrenciSoyad = "Uyguç"
ogrenciAdSoyad = ogrenciAd + ogrenciSoyad # Böyle yaparsam isim soyisim arasında boşluk olmaz.
print(ogrenciAdSoyad)

ogrenciAdSoyad1 = ogrenciAd + " " + ogrenciSoyad # Boşluk olması için böyle yazmalıyım.
print(ogrenciAdSoyad1)


# Uygulama 2 İçin Çözümüm

urun1, urun2, urun3 = 50, 60.5, 356.45
toplam = urun1 + urun2 + urun3
print(toplam)
print("Ürün Toplamı =", toplam)
