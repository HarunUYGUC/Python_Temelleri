import pandas as pd
import numpy as np

data = {
    "Column1": [1, 2, 3, 4, 5],
    "Column2": [10, 20, 20, 45, 25],
    "Column3": ["abc", "bcaa", "ade", "cb", "dea"]
}

df = pd.DataFrame(data)

def kareal(x):
    return x * x

kareal2 = lambda x: x * x

result = df
result = df["Column2"].unique() # Tekrarlamayan elemanları verir.
result = df["Column2"].nunique() # Tekrarlamayan eleman sayısını verir.
result = df["Column2"].value_counts() # Hangi elemanın kaç tane olduğunu verir. 
result = df["Column1"] * 2
result = df["Column1"].apply(kareal)
result = df["Column1"].apply(kareal2)
result = df["Column1"].apply(lambda x: x * x)
result = df["Column3"].apply(len)
df["Column4"] = df["Column3"].apply(len)

result = df.columns
result = len(df.columns)
result = df.index
result = len(df.index)
result = df.info

result = df.sort_values("Column2")
result = df.sort_values("Column3") # Büyükten küçüğe sıralar.
result = df.sort_values("Column3", ascending = False) # Küçükten büyüğe sıralar.

data = {
    "Ay": ["Mayıs", "Haziran", "Nisan", "Mayıs", "Haziran", "Nisan", "Mayıs", "Haziran", "Nisan"],
    "Kategori": ["Elektronik", "Elektronik", "Elektronik", "Kitap", "Kitap", "Kitap", "Giyim", "Giyim", "Giyim"],
    "Gelir": [20, 30, 15, 14, 32, 42, 12, 36, 52]
}

df = pd.DataFrame(data)
df = df.pivot_table(index = "Ay", columns = "Kategori", values = "Gelir")

# print(result)
print(df)
