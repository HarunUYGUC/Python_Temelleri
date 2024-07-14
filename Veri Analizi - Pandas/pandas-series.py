import pandas as pd
import numpy as np

# data
numbers = [20, 30, 40, 50]
# numbers2 = [20, 30, 40, 50, 60] => Hatalı kullanım.
letters = ["a", "b", "c", "d"]
# letters = ["a", "b", "c", "d", 20]
scalar = 5
dict = {"a": 10, "b": 20, "c": 30, "d": 40}
random_numbers = np.random.randint(10, 100, 6)
# numbers3 = np.array([20, 30, 40, 50])
numbers4 = [20, 30, 40, 51]

# pandas_series = pd.Series()
# pandas_series = pd.Series(numbers)
# pandas_series = pd.Series(letters)
# pandas_series = pd.Series(scalar)
# pandas_series = pd.Series(scalar, [0, 1, 2, 3])
# pandas_series = pd.Series(numbers, ["a", "b", "c", "d"])
# pandas_series = pd.Series(numbers2, ["a", "b", "c", "d"]) => Hatalı kullanım.
# pandas_series = pd.Series(scalar, ["a", "b", "c", "d"])
# pandas_series = pd.Series(dict)
# pandas_series = pd.Series(random_numbers)
# pandas_series = pd.Series([20, 30, 40, 50], ["a", "b", "c", "d"])
# pandas_series = pd.Series(numbers, ["a", "b", "c", "d"])

# result = pandas_series[0]
# result = pandas_series[-1]
# result = pandas_series[:2]
# result = pandas_series[-2:]
# result = pandas_series["a"]
# result = pandas_series["d"]
# result = pandas_series[["a", "c"]]
# result = pandas_series.ndim # listenin boyutu
# result = pandas_series.dtype # listenin veri tipi
# result = pandas_series.shape
# result = pandas_series.sum()
# result = pandas_series.max()
# result = pandas_series.min()
# result = pandas_series + pandas_series
# result = pandas_series + 50
# result = np.sqrt(pandas_series)
# result = pandas_series >= 50

pandas_series = pd.Series(numbers4, ["a", "b", "c", "d"])

result = pandas_series % 2 == 0

print(pandas_series[result])
print(pandas_series)
print(result)


opel2018 = pd.Series([20, 30, 40, 10], ["Astra", "Corsa", "Mokka", "Insignia"])
opel2019 = pd.Series([40, 30, 20, 10], ["Astra", "Corsa", "Grandland", "Insignia"])

total = opel2018 + opel2019

print(total)
print(total["Astra"])
# print(total["Combo"]) # Error
