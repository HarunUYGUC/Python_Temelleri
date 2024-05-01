# serialize
# Uygulama tarafında olan bir objeyi dosya tarafına bir .json 
# bir bilgi olarak aktarma işlemine denir.

# deserialize
# Yukarıdakinin tam tersidir.

import json

with open(r"C:\Users\Harun\Desktop\Python_Temelleri\JSON ile Dosya İşlemleri\person.json") as file:
    # data = file.read() 
    # Aşağıdaki gibi yapmak yerine yukarıdaki gibi yaparsak type(data)
    # aşağıdakinde "dict" olarak gelirken bunda "str" olarak gelir. 
    # Ayrıca print() de de sonuç farklı oluyor.
    data = json.load(file)

print(data)
print(type(data))

print(data["firstName"]) # Dosyayı read() olarak işleseydik bu kod çalışmazdı.

print(data["hobbies"])
print(data["hobbies"][0])

print(data["gameCharacters"])
print(data["gameCharacters"][0])
print(data["gameCharacters"][0]["firstName"])


print("---------------------")

# json-string

data = """
{
    "firstName": "Harun",
    "lastName": "Uyguç",
    "hobbies": ["bilgisayar oyunları", "spor"],
    "age": 21,
    "gameCharacters": [
        {
            "firstName": "Kyle",
            "lastName": "Crane",
            "age": 24
        },
        {
            "firstName": "Leon",
            "lastName": "S. Kennedy",
            "age": 22
        }
    ]
}
"""

data = json.loads(data)
print(data)
print(type(data))

print(data["gameCharacters"])
print(data["gameCharacters"][0])
print(data["gameCharacters"][0]["firstName"])
