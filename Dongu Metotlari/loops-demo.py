"""
   1-100 arasında rastgele üretilecek bir sayıyı aşağı, yukarı ifadeleri ile
   buldurmaya çalışın.
   ** "random modülü" için "python random" şeklinde arama yapın.
   ** 100 üzerinden puanlama yapın. Her soru 20 puan.
   ** Hak bilgisini kullanıcıdan alın ve her soru belirtilen can sayısı
      üzerinden hesaplansın.
"""
import random

bulunacakSayi = random.randint(0,100)
kaçHak = int(input("Bu sayıyı bulmak için max. kaç hak istersiniz?: "))
tahminEdilenSayi = int(input("Sizce sayı kaç?: "))
i = 1

while (i <= kaçHak):
    if (tahminEdilenSayi == bulunacakSayi):
        print(f"Tebrikler sayı {bulunacakSayi}'idi, sayıyı buldunuz!")
        alinanPuan = 100 - (100 / kaçHak) * (i - 1)
        print(f"100 Üzerinden Aldığınız Puan: {round(alinanPuan,2)}")
        break
    else:
        if (tahminEdilenSayi < bulunacakSayi):
            if (i == kaçHak):
                break
            print(f"Sayınızı arttırmalısınız! {kaçHak - i} hakkınız kaldı!")
            tahminEdilenSayi = int(input("Sizce sayı kaç?: "))
        else:
            if (i == kaçHak):
                break
            print(f"Sayınızı azaltmalısınız! {kaçHak - i} hakkınız kaldı!")
            tahminEdilenSayi = int(input("Sizce sayı kaç?: "))
    i += 1

if (i == kaçHak):
    print(f"Hakklarınız bitti. Aldığınız puan 0 / Bulunacak Sayı: {bulunacakSayi}'idi.")

