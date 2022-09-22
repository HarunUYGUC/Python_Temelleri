isimler = ["Ahmet", "ali", "Çınar", "DeNiz"]
string = "Hello 12345 World"
yillar = [1983, 1999, 2008, 1956, 1986]
dereceler = [20,5,15,-2,0,-6]

# 1- "1-100" arasındaki sayılardan 12'e tam bölünebilen sayı listesi oluşturunuz.

sayilar = [sayi for sayi in range(1,101) if (sayi % 12 == 0)]
print(sayilar)


# 2- isimler listesindeki her ismi küçük harfe çevirip tersten yazınız.

tersten = [isim.lower()[::-1] for isim in isimler]
print(tersten)


# 3- verilen "string" içindeki rakamları içeren bir liste oluşturunuz.

sonuc = [i for i in string if (i.isdigit())]
print(sonuc)


# 4- "yillar"  dizisindeki her doğum yılı için yaş bilgisini içeren liste oluşturunuz.

import datetime
simdi = datetime.datetime.now().year

yas = [(simdi - yil) for yil in yillar]
print(yas)


# 5- "dereceler" listesinde bulunan hava sıcaklık bilgisine göre eksi değer için buzlanma tehlikesi yazınız.

sonuc = [buzlanma if (buzlanma > 0) else "Buzlanma Tehlikesi!" for buzlanma in dereceler]
print(sonuc)
