import pandas as pd

df = pd.read_csv(r"C:\Users\Harun\Desktop\Python_Temelleri\Veri Analizi - Pandas\Ready Dataset 3\nba.csv")

# 1- İlk 10 kaydı getiriniz.
result = df.head(10)

# 2- Toplam kaç kayıt vardır?
result = len(df.index)

# 3- Tüm oyuncuların boy ortalaması nedir?
result = df["player_height"].mean()

# 4- En uzun boy ne kadardır?
result = df["player_height"].max()

# 5- En uzun oyuncu kimdir?
result = df[df["player_height"] == df["player_height"].max()] # İlgili satırlar gelir.
result = df[df["player_height"] == df["player_height"].max()]["player_name"] # İlgili isim index ile birlikte gelir.
result = df[df["player_height"] == df["player_height"].max()]["player_name"].iloc[0] # Sadece ilgili isim gelir.

# 6- Yaşı 20-25 arasında olan oyuncuların isim ve oynadıkları takımları azalan şekilde sıralı getiriniz.
result = df[(df["age"] >= 20) & (df["age"] < 25)][["player_name", "team_abbreviation", "age"]].sort_values("age", ascending = False)

# 7- "Dexter Pittman" isimli oyuncunun oynadığı takım hangisidir?
result = df[df["player_name"] == "Dexter Pittman"]["team_abbreviation"].iloc[0]

# 8- Takımlara göre oyuncuların ortalama yaş bilgisi nedir?
result = df.groupby("team_abbreviation")["age"].mean()

# 9- Kaç farklı takım mevcut?
result = len(df.groupby("team_abbreviation"))
result = df["team_abbreviation"].nunique()
result = df["team_abbreviation"].unique()

# 10- Her takımda kaç oyuncu oynamaktadır?
result = df["team_abbreviation"].value_counts()

# 11- İsmi içinde "and" geçen kayıtları bulunuz.
result = df[df["player_name"].str.contains("and")]
# df = df.dropna() # NaN veriler varsa ilk önce bu işlem yapılır.
# df.dropna(inplace = True) # NaN veriler varsa ilk önce bu işlem yapılır.

def str_find(name):
    if ("and" in name.lower()):
        return True
    return False

result = df[df["player_name"].apply(str_find)]


print(result)
