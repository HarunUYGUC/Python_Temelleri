import numpy as np

result = np.array([1, 3, 5, 7, 9])
print(result)

# 1'den 9'a kadar bir dizi oluşturur. 
result = np.arange(1, 10)
print(result)

# 10'dan 99'a kadar ama 3'er 3'er artan bir dizi oluşturur.
result = np.arange(10, 100, 3)
print(result)

# 10 tane 0'dan oluşan bir dizi oluşturur.
# [0. 0. 0. 0. 0. 0. 0. 0. 0. 0.]
result = np.zeros(10)
print(result)

# 10 tane 1'den oluşan bir dizi oluşturur.
# [1. 1. 1. 1. 1. 1. 1. 1. 1. 1.]
result = np.ones(10)
print(result)

# 0 - 100 arasını 5 eşit parçaya böler.
# [  0.  25.  50.  75. 100.]
result = np.linspace(0, 100, 5)
print(result)

result = np.linspace(0, 5, 5)
print(result)

# 0 ile 9 arasından bir tam sayıyı rastgele üretir.
result = np.random.randint(0, 10)
print(result)

# 0 ile 19 arasından bir tam sayıyı rastgele üretir. 
result = np.random.randint(20)
print(result)

# 1 ile 10 arasından 3 tane rastgele tam sayı üretir ve
# bir dizi içerisinde bunları verir.
# [6 1 4]
result = np.random.randint(1, 10, 3)
print(result)

# 0 ile 1 arasından 5 tane rastgele sayı üretir ve
# bir dizi içerisinde bunları verir.
# [0.81519396 0.08004207 0.18285884 0.03296353 0.23658981]
result = np.random.rand(5)
print(result)

# 0 ile 1 (Negatif 0 ile 1 arası da dahil.) arasından 5 tane rastgele sayı üretir ve
# bir dizi içerisinde bunları verir.
# [-0.96415234  0.30639663  1.21620991 -0.9630139  -0.4953534 ]
result = np.random.randn(5)
print(result)

# 0'dan 49'a kadarlık bir dizi oluşturur.
np_array = np.arange(50)
# 5'e 10'luk bir matris oluşturur.
np_multi = np_array.reshape(5, 10)
print(np_multi)
# Oluşturduğumuz dizinin her bir satırının toplamını verir.
print(np_multi.sum(axis=1))
# Oluşturduğumuz dizinin her bir sütununun toplamını verir.
print(np_multi.sum(axis=0))

# 1 ile 99 arasından 10 tane tam sayıyı rastgele üretir. 
rnd_numbers = np.random.randint(1, 100, 10)
print(rnd_numbers)
# Üretilen sayılardan en büyüğünü verir.
result = rnd_numbers.max()
print(result)
# Üretilen sayılardan en küçüğünü verir.
result = rnd_numbers.min()
print(result)
# Üretilen sayıların ortalamasını verir.
result = rnd_numbers.mean()
print(result)
# Üretilen sayılardan en büyüğünün indeksini verir.
result = rnd_numbers.argmax()
print(result)
# Üretilen sayılardan en küçüğünün indeksini verir.
result = rnd_numbers.argmin()
print(result)
