import numpy as np

# 1- (10, 15, 30, 45, 60) değerlerine sahip numpy dizisi oluşturunuz.

result = np.array((10, 15, 30, 45, 60))
# result = np.array([10, 15, 30, 45, 60]) şeklinde de oluyor.
print(result)

# 2- (5-15) arasındaki sayılarla numpy dizisi oluşturunuz.

result = np.arange(5, 15)
print(result)

# 3- (50-100) arasında 5'er 5'er artarak numpy dizisi oluşturunuz.

result = np.arange(50, 100, 5)
print(result)

# 4- 10 elemanlı sıfırlardan oluşan bir dizi oluşturunuz.

result = np.zeros(10)
print(result)

# 5- 10 elemanlı birlerden oluşan bir dizi oluşturunuz.

result = np.ones(10)
print(result)

"""
Belirttiğim indeksteki elemanı değiştirmeyi denedim.
result[0] = 2
print(result)
"""

# 6- (0-100) arasında eşit aralıklı 5 sayı üretin.

""" linspace => lineer space """
result = np.linspace(0, 100, 5)
print(result)

# 7- (10-30) arasında rastgele 5 tane tam sayı üretin.

result = np.random.randint(10, 30, 5)
print(result)

# 8- [-1 ile 1] arasında 10 adet sayı üretin.

result = np.random.randn(10)
print(result)

# 9- (3x5) boyutlarında (10-50) arasında rastgele bir matris oluşturunuz.

""" İlk önce 3*5'lik yani 15 elemanlı bir dizi oluşturduk. 
Daha sonra o diziyi 3 satır 5 sütun olacak şekilde şekillendirdik. """
result = np.random.randint(10, 50, 15).reshape(3, 5)
print(result)

# 10- Üretilen matrisin satır ve sütün sayıları toplamlarını hesaplayınız.

matris = np.random.randint(10, 50, 15).reshape(3, 5)
print(matris)

rowTotal = matris.sum(axis=1)
colTotal = matris.sum(axis=0)
print(rowTotal)
print(colTotal)

# 11- Üretilen matrisin en büyük, en küçük ve ortalaması nedir?

max = matris.max()
print(max)

min = matris.min()
print(min)

avg = matris.mean()
print(avg)

# 12- Üretilen matrisin en büyük ve en küçük değerinin indeksi kaçtır?

result = matris.argmax()
print(result)

result = matris.argmin()
print(result)

# 13- (10-20) arasındaki sayıları içeren dizinin ilk 3 elemanını seçiniz.

arr = np.arange(10, 20)
print(arr)

result = arr[:3]
print(result)

# 14- Üretilen dizinin elemanlarını tersten yazdırın.

result = arr[::-1]
print(result)

# 15- Üretilen matrisin ilk satırını seçiniz.

result = matris[0]
print(result)

# 16- Üretilen matrisin 2. satır 3. sütunundaki elemanı hangisidir?

result = matris[1, 2]
print(result)

# 17- Üretilen matrisin tüm satırlarındaki ilk elemanı seçiniz.

result = matris[:, 0]
print(result)

# 18- Üretilen matrisin her bir elemanının karesini alınız.

result = matris ** 2
print(result)

# 19- Üretilen matris elemanlarının hangisi pozitif çift sayıdır?
#     Aralığı (-50, +50) arasında yapınız.

matris = np.random.randint(-50, 50, 15).reshape(3, 5)
print(matris)

ciftler = matris[matris % 2 == 0]
print(ciftler)
result = ciftler[ciftler > 0]
print(result)
