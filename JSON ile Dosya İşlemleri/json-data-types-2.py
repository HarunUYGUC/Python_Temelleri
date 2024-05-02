data = {
    "harunuyguc": {
        "firstName": "Harun",
        "lastName": "Uyguç"
    },
    "kylecrane": {
        "firstName": "Kyle",
        "lastName": "Crane"
    }
}

import json

with open(r"C:\Users\Harun\Desktop\Python_Temelleri\JSON ile Dosya İşlemleri\users-2.json", "w") as file:
    json.dump(data, file, ensure_ascii=False, indent=2)

with open(r"C:\Users\Harun\Desktop\Python_Temelleri\JSON ile Dosya İşlemleri\users-2.json") as file:
    users = json.load(file)

print(users)
print(users["harunuyguc"])

users.update({
  "leonkennedy": {
    "firstName": "Leon",
    "lastName": "Kennedy"
  }
})

with open(r"C:\Users\Harun\Desktop\Python_Temelleri\JSON ile Dosya İşlemleri\users-2.json" ,"w") as file:
    json.dump(users, file, ensure_ascii=False, indent=2)

users.update({
  "harunuyguc": {
    "firstName": "Harun",
    "lastName": "Uyguç",
    "age": 20
  }
})

with open(r"C:\Users\Harun\Desktop\Python_Temelleri\JSON ile Dosya İşlemleri\users-2.json" ,"w") as file:
    json.dump(users, file, ensure_ascii=False, indent=2)

users.pop("kylecrane")

with open(r"C:\Users\Harun\Desktop\Python_Temelleri\JSON ile Dosya İşlemleri\users-2.json" ,"w") as file:
    json.dump(users, file, ensure_ascii=False, indent=2)
