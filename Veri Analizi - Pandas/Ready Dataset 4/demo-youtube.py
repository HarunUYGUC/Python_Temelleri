import pandas as pd

df = pd.read_csv(r"C:\Users\Harun\Desktop\Python_Temelleri\Veri Analizi - Pandas\Ready Dataset 4\youtube-ing.csv")

# 1- İlk 10 kaydı getiriniz.
result = df.head(10)

# 2- İkinci 5 kaydı getiriniz.
result = df[5:10].head(5)
result = df[5:10]

# 3- Dataset'de bulunan kolon isimleri ve sayısını bulunuz.
result = df.columns
result = len(df.columns)

# 4- Aşağıda bulunan bazı kolonları silin ve kalan kolonları listeleyiniz.
# ("dislikes")
# df = df.drop("dislikes", axis=1) # Aşağıdaki ile bu aynı.
df.drop("dislikes", axis=1, inplace=True)

result = df

# 5- Views ve likes sayılarının ortalamasını bulunuz. 
result = df["likes"].mean()
result = df["views"].mean()

# 6- İlk 50 videonun views ve likes kolonlarını getiriniz.
result = df.head(50)[["channel", "views", "likes"]]

# 7- En çok görüntülenen video hangisidir?
result = df[df["views"].max() == df["views"]][["channel", "views"]]
result = df[df["views"].max() == df["views"]]["channel"].iloc[0]

# 8- En az görüntülenen video hangisidir?
result = df[df["views"].min() == df["views"]]["channel"].iloc[0]

# 9- En çok görüntülenen ilk 10 video hangisidir?
result = df.sort_values("views", ascending=False).head(10)[["channel", "views"]]

# 10- Kategoriye göre likes ortalamalarını sıralı şekilde getiriniz.


print(result)
