sayilar = [1,5,15,35,57,72]

# 1- sayilar listesindeki her bir elemanı yazdırın.

for x in sayilar:
    print(x)


# 2- Sayilar listesindeki hangi sayılar 5'in katıdır?

for x in sayilar:
    if (x % 5 == 0):
        print(x)


# 3- Sayilar listesinde sayıların toplamı kaçtır?

toplam = 0

for x in sayilar:
    toplam = x + toplam
    
print(toplam)


# 4- Sayilar listesindeki çift sayıların karesini alınız.

for x in sayilar:
    if (x % 2 == 0):
        print(x**2)        


urunler = ['iphone 8','iphone X','iphone XR','samsung S10']

# 5- urunler listesindeki tüm ürünlerin 2. karakterlerini ekrana yazdırın.

for urun in urunler:
    print(urun[1])


# 6- urunler listesinde içinde "iphone" geçen kaç ürün vardır?

for urun in urunler:
    print(urun.find("iphone"))


count = 0

for urun in urunler:
    index = urun.find("iphone")
    if (index > -1):
        count += 1

print(count)
