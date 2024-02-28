import numpy as np

numbers = np.array([0, 5, 10, 15, 20, 25, 50, 75])
# 5. indeksteki elemanı verir. 25.
result = numbers[5]
print(result)

# -1. indeksteki elemanı verir. 75.
result = numbers[-1]
print(result)

# 0. indeksten 2. indekse kadar ki elemanları verir. [ 0  5 10]
result = numbers[0:3]
print(result)

# 3. indeksten dizinin sonuncu indeksine kadar ki elemanları verir.
# [15 20 25 50 75]
result = numbers[3:]
print(result)

# Dizinin başından sonuna kadar ki elemanları verir.
# [ 0  5 10 15 20 25 50 75]
result = numbers[:]
print(result)

# Yukarıdakinin aynısı.
result = numbers[::]
print(result)

# Dizinin sonundan başına kadar ki elemanları verir.
result = numbers[::-1]
print(result)

# Dizinin sonundan başına ikişerli artarak elemanları verir.
# [75 25 15  5]
result = numbers[::-2]
print(result)

""" İki Boyutlu Matris """
numbers2 = np.array([[0, 5, 10], [15, 20, 25], [50, 75, 85]])
print(numbers2)

result = numbers2[0]
print(result)

result = numbers2[1]
print(result)

# Sonuçları aynı.
result = numbers2[0][2]
print(result)

# Sonuçları aynı.
result = numbers2[0, 2]
print(result)

result = numbers2[1]
print(result)

# Her satırın 2. indeksindeki elemanı verir.
# [10 25 85]
result = numbers2[:, 2]
print(result)

result = numbers2[:, 0]
print(result)

# Her satırdan 0. ve 2. indeks arasındaki elemanları verir.
# [[ 0  5]
# [15 20]
# [50 75]]
result = numbers2[:, 0:2]
print(result)

# Son satırdaki elemanları verir.
# [50 75 85]
result = numbers2[-1, :]
print(result)

# 0. ve 1. satırların 0. ve 1. sütunundaki elemanlarını verir.
# [[ 0  5]
# [15 20]]
result = numbers2[:2, :2]
print(result)

# 0'dan 9'a kadar bir dizi oluşturur.
arr1 = np.arange(0, 10)
# Adreslerini eşitlediğimiz için arr2 dizisinin de içeriği arr1 ile aynıdır.
arr2 = arr1 # referans
# arr2 = arr1.copy() şeklinde bir kod yazarsak adresleri aynı olmaz, 
# sadece içerikleri aynı olur. Yani birisinde yapılan değişiklik diğerini etkilemez.
print(arr1)
print(arr2)

# Adresleri aynı olan iki diziden birisindeki elemanı değiştirdiğimizde
# diğerindeki eleman da değişir.
arr2[0] = 20
print(arr2)
print(arr1)
