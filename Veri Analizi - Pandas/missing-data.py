import pandas as pd
import numpy as np

data = np.random.randint(10, 100, 15).reshape(5, 3)

df = pd.DataFrame(data, index = ["a", "c", "e", "f", "h"], columns = ["Column1", "Column2", "Column3"])

df = df.reindex(["a", "b", "c", "d", "e", "f", "g", "h"])

newColumn = [np.nan, 30, np.nan, 51, np.nan, 30, np.nan, 10]
df["Column4"] = newColumn

result = df
result = df.drop("Column1", axis = 1) # "axis = 1 => kolon, axis = 0 => satır" demek.
result = df.drop(["Column1", "Column2"], axis = 1)
result = df.drop("a", axis = 0) # drop ile satır veya kolonları sileriz.
result = df.drop(["a", "b", "h"], axis = 0)

result = df.isnull() # Nan (Not a Number) mı?
result = df.notnull() # Nan (Not a Number) değil mi?
result = df.isnull().sum()
result = df["Column1"].isnull().sum()
result = df["Column1"].isnull()
result = df[df["Column1"].isnull()]
result = df[df["Column1"].isnull()]["Column1"]
result = df[df["Column1"].notnull()]["Column1"]
result = df[df["Column1"].notnull()]

result = df.dropna() # drop() ve dropna() metotlarının varsayılan axis değeri 0'dır yani satırdır.
result = df.dropna(axis = 1)
result = df.dropna(how = "any") # Satırda herhangi bir NaN varsa o satır gelmez.
result = df.dropna(how = "all") # Satırın tamamında NaN varsa o satır gelmez.
result = df.dropna(subset = ["Column1", "Column2"], how = "all") # Belirtilen 2 kolonda da NaN varsa o satır gelmez.
result = df.dropna(subset = ["Column1", "Column2"], how = "any") # Belirtilen 2 kolondan herhangi birinde NaN varsa o satır gelmez.
result = df.dropna(thresh = 2) # En az 2 tane normal veri varsa (NaN olmayan) o satırları verir.
result = df.dropna(thresh = 4)
result = df.dropna(thresh = 3)

result = df.fillna(value = "No Input") # NaN olan alanları ilgili value ile doldurur.
result = df.fillna(value = 1)

result = df.sum()
result = df.sum().sum()
result = df.size
result = df.isnull().sum()
result = df.isnull().sum().sum()

def ortalama(df):
    toplam = df.sum().sum()
    adet = df.size - df.isnull().sum().sum()
    return toplam / adet

result = df.fillna(value = ortalama(df))

print(result)
# print(df)
