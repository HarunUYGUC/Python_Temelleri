import numpy as np

# 10 ile 99 arasındaki sayılardan rastgele 6 tane sayıyı üretir.
# [25 17 40 75 53 36]
numbers1 = np.random.randint(10, 100, 6)
numbers2 = np.random.randint(10, 100, 6)

print(numbers1)
print(numbers2)

# Dizilerin aynı indeksindeki elemanlarını toplar.
result = numbers1 + numbers2
print(result)
# Dizideki her elemana 10 ekler.s
result = numbers1 + 10
print(result)

result = numbers1 - numbers2
print(result)
result = numbers1 - 10
print(result)

result = numbers1 * numbers2
print(result)
result = numbers1 * 10
print(result)

result = numbers1 / numbers2
print(result)
result = numbers1 / 10
print(result)

# Dizideki her elemanınn sinüs değerini verir. 
result = np.sin(numbers1)
print(result)

result = np.cos(numbers1)
print(result)

result = np.sqrt(numbers1)
print(result)

result = np.log(numbers1)
print(result)

# Önceki diziyi 2 satır 3 sütuna sahip olacak şekilde değiştiriyoruz.
mnumbers1 = numbers1.reshape(2, 3)
mnumbers2 = numbers2.reshape(2, 3)
print(mnumbers1)
"""
 [[89 97 91]
 [18 50 18]] """
print(mnumbers2)
""" 
 [[36 63 97]
 [35 45 25]] """

# İki diziyi dikey olarak birleştirip tek dizi oluşturur.
result = np.vstack((mnumbers1, mnumbers2))
print(result)
""" 
[[89 97 91]
 [18 50 18]
 [36 63 97]
 [35 45 25]] """

# İki diziyi yatay olarak birleştirip tek dizi oluşturur.
result = np.hstack((mnumbers1, mnumbers2))
print(result)
""" [[89 97 91 36 63 97]
    [18 50 18 35 45 25]] """

# Dizideki bütün elemanları tek-çift olarak kontrol eder.
result = numbers1 % 2 == 0
print(result)

# Dizideki bütün elemanların 50'den büyük olup olmadığını kontrol eder.
# [ True  True True  False  True  False]
result = numbers1 >= 50
print(result)

# Yukarıdaki koşulu sağlayan dizinin elemanlarını verir.
# [89 97 91 50]
print(numbers1[result])
