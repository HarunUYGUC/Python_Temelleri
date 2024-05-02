db = {
    "users": {
        "harunuyguc": {
            "firstName": "Harun",
            "lastName": "Uyguç"
        },
        "kylecrane": {
            "firstName": "Kyle",
            "lastName": "Crane"         
        }
    },
    "products": {
        "1": {
            "productName": "Iphone 8",
            "price": 5000 
        },
        "2": {
            "productName": "Iphone 12",
            "price": 8000     
        }
    }
}

import json

# with open(r"C:\Users\Harun\Desktop\Python_Temelleri\JSON ile Dosya İşlemleri\db.json" ,"w") as file:
#     json.dump(db, file, ensure_ascii=False, indent=2)

with open(r"C:\Users\Harun\Desktop\Python_Temelleri\JSON ile Dosya İşlemleri\db.json") as file:
    db = json.load(file)

print(db)
print(db["users"])
print(db["products"])

print(db["users"]["harunuyguc"])
print(db["users"]["harunuyguc"]["firstName"])

db["products"].update({
    "3": {
      "productName": "Iphone 11",
      "price": 7000
    }
})

with open(r"C:\Users\Harun\Desktop\Python_Temelleri\JSON ile Dosya İşlemleri\db.json" ,"w") as file:
    json.dump(db, file, ensure_ascii=False, indent=2)

db["products"].update({
    "3": {
      "productName": "Iphone 11",
      "price": 7600
    }
})

with open(r"C:\Users\Harun\Desktop\Python_Temelleri\JSON ile Dosya İşlemleri\db.json" ,"w") as file:
    json.dump(db, file, ensure_ascii=False, indent=2)
