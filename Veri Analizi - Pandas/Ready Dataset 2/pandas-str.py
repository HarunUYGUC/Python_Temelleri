import pandas as pd

data = pd.read_csv(r"C:\Users\Harun\Desktop\Python_Temelleri\Veri Analizi - Pandas\Ready Dataset 2\nba.csv")

data.dropna(inplace = True)

print(data.columns)

data["player_name"] = data["player_name"].str.upper()
data["player_name"] = data["player_name"].str.lower()
data["index"] = data["player_name"].str.find("a")

# data = data.player_name.str.contains("jericho")
# data = data["player_name"].str.contains("jericho")
# data["player_name"] = data["player_name"].str.contains("jericho")
# data = data[data.player_name.str.contains("jericho")]

# data = data.player_name.str.replace(" ", "-")
# data = data.player_name.str.replace(" ", "-").str.replace(".", " ")

data[["FirstName", "LastName"]] = data["player_name"].loc[data["player_name"].str.split().str.len() == 2].str.split(expand = True)

print(data.head(10))
