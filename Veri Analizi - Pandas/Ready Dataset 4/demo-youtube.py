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
result = df.groupby("category").mean("likes").sort_values("likes")["likes"]

# 11- Kategoriye göre görüntülenme sayılarını yukarıdan aşağıya sıralayınız.
result = df.groupby("category").sum().sort_values("views", ascending=False)["views"]

# 12- Her kategoride kaç video vardır?
result = df["category"].value_counts()

# 13- Her videonun title uzunluğu bilgisini yeni bir kolonda gösteriniz.
df["title_len"] = df["name"].apply(len)
result = df

# 14- Her video için name'deki kelime sayısını yeni kolonda gösteriniz.
df["word_count"] = df["name"].apply(lambda x: len(x.split(" ")))
result = df

def wordCount(name):
    return len(name.split(" "))

df["word_count"] = df["name"].apply(wordCount)
result = df


print(result)

# 15- En popüler videoları listeleyiniz. (likes/views oranına göre.)

def likeDislikeOranınıHesapla(dataset):
    likesList = list(dataset["likes"])
    viewsList = list(dataset["views"])

    liste = list(zip(likesList, viewsList)) # zip ile tuple'a çevirdik.

    oranListesi = []

    for like, view in liste:
        if ((like + view) == 0):
            oranListesi.append(0)
        else:
            oranListesi.append(like / (like + view))

    # print(liste)
    # print(likesList, viewsList)
    return oranListesi

# likeDislikeOranınıHesapla(df)
# print(likeDislikeOranınıHesapla(df))
df["beğeni_oranı"] = likeDislikeOranınıHesapla(df)
print(df.sort_values("beğeni_oranı", ascending=False)[["channel", "likes", "views", "beğeni_oranı"]])
