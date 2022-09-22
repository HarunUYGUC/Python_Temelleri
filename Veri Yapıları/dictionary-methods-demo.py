"""
    player 1: 
        id             => 1
        name           => Cristiano Ronaldo
        yearOfBirth    => 1985
        nationality    => Portugal
        current_team   => Portugal
        history        => Juventus, Real Madrid, Portugal

    player 2:
        id             => 2
        name           => Lionel Messi
        yearOfBirth    => 1987
        nationality    => Argentina
        current_team   => Barcelona
        history        => Barcelona, Argentina, Portugal
"""

# 1- Yukarıda verilen bilgileri liste içerisinde saklayınız.

sporcular = {
    "player 1": {
        "id": 1,
        "name": "Cristiano Ronaldo",
        "yearOfBirth": 1985,
        "nationality": "Portugal",
        "current_team": "Portugal",
        "history": "Juventus, Real Madrid, Portugal"
    } ,
    "player 2": {
        "id": 2,
        "name": "Lionel Messi",
        "yearOfBirth": 1987,
        "nationality": "Argentina",
        "current_team": "Barcelona",
        "history": "Barcelona, Argentina, Portugal"
    }
}

print(sporcular)

print(sporcular["player 1"]["name"])


# 2- id' e göre arama yapınız.

sporcular = {
    1: {
        "name": "Cristiano Ronaldo",
        "yearOfBirth": 1985,
        "nationality": "Portugal",
        "current_team": "Portugal",
        "history": "Juventus, Real Madrid, Portugal"
    } ,
    2: {
        "name": "Lionel Messi",
        "yearOfBirth": 1987,
        "nationality": "Argentina",
        "current_team": "Barcelona",
        "history": "Barcelona, Argentina, Portugal"
    }
}

id = input("Sporcunun ID'sini Giriniz / 1 veya 2 : ")
print(sporcular[int(id)]["name"])


# 3- id' e göre bilgi kayıt siliniz.

id = input("Hangi ID'den bilgi silmek istiyorsunuz? : ")
degistir = input("Hangi bilgiyi silmek istiyorsunuz? : ")

sporcular[int(id)].pop(degistir)

print(sporcular)
