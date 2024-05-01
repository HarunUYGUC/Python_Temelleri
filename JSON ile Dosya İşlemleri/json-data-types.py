import json

data = [
    {
        "userName": "harunuyguc",
        "firstName": "Harun",
        "lastName": "Uyguç"
    }
]

# with open(r"C:\Users\Harun\Desktop\Python_Temelleri\JSON ile Dosya İşlemleri\urunler.json", "w") as file:
#     json.dump(data, file, ensure_ascii=False, indent=2)

user = {
    "userName": "kylecrane",
    "firstName": "Kyle",
    "lastName": "Crane"
}

with open(r"C:\Users\Harun\Desktop\Python_Temelleri\JSON ile Dosya İşlemleri\users.json") as file:
    users = json.load(file)

for user in users:
    # print(user)

    if (user["userName"] == "harunuyguc"):
        user["userName"] = "HarunUyguc"

users.remove(users[0])

# users.append(user)

with open(r"C:\Users\Harun\Desktop\Python_Temelleri\JSON ile Dosya İşlemleri\users.json", "w") as file:
    json.dump(users, file, ensure_ascii=False, indent=2)
