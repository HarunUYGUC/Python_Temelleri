import pandas as pd
from numpy.random import randn

df = pd.DataFrame(randn(3, 3), index = ["A", "B", "C"], columns = ["Column1", "Column2", "Column3"])

result = df
result = df["Column1"]
result = type(df["Column1"])
result = df[["Column1", "Column2"]]

# loc["row", "column"] => loc["row"] => loc[:, "column"]
result = df.loc["A"]
result = type(df.loc["A"])
result = df.iloc[2] # Index'e göre çalışmak için.

result = df.loc[:, "Column1"]
result = df.loc[:, ["Column1", "Column2"]]
result = df.loc[:, "Column1":"Column3"] # 1 ve 3 arası (1 ve 3 dahil) tüm kolonlar gelir.
result = df.loc[:, :"Column3"] # Baştan 3'e (baş ve 3 dahil) tüm kolonlar gelir.

result = df.loc["A":"C":, :"Column3"] # A ve C arası (A ve C dahil) tüm satırlar gelir.
result = df.loc["A":"C"] # A ve C arası (A ve C dahil) tüm satırlar gelir.
result = df.loc[:"C"]  # Baştan C'ye (baş ve C dahil) tüm satırlar gelir.

result = df.loc["A", "Column2"]
result = df.loc["C", "Column1"]
result = df.loc[["A", "B"], ["Column1", "Column2"]]

df["Column4"] = pd.Series(randn(3), ["A", "B", "C"])
df["Column5"] = df["Column1"] + df["Column3"]

result = df.drop("Column5", axis = 1, inplace = True)

print(result)
print(df)
