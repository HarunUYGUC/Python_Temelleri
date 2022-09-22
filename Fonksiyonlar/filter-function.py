yaslar = [5,12,18,24,45]

def yetiskinMi(x):
    if (x < 18):
        return False
    else:
        return True

print(list(filter(yetiskinMi, yaslar)))


yaslar = [5,12,18,24,45]

print(list(filter(lambda x: x >= 18, yaslar)))


sayilar = [0,1,25,6,8,9]

print(list(filter(lambda sayi: (sayi % 2 == 0), sayilar)))


isimler = ["çınar", "yiğit", "sena", "ada", "ali"]

print(list(filter(lambda isim: isim[0] == "a", isimler)))


isimler = ["çınar", "yiğit", "sena", "ada", "ali"]

print(list(map(lambda isim: isim.upper(), filter(lambda isim: isim[0] == "a", isimler))))


isimler = ["çınar", "yiğit", "sena", "ada", "ali"]

filteredResult = filter(lambda isim: isim[0] == "a", isimler)
print(list(map(lambda isim: isim.upper(), filteredResult)))


users = [
    {"username": "sadikturan", "tweets": ["tweet1", "tweet2"]},
    {"username": "cinarturan", "tweets": []},
    {"username": "senaturan", "tweets": ["tweet1"]}
]

print(list(filter(lambda user: len(user["tweets"]) > 0, users)))


filteredResults = filter(lambda user: len(user["tweets"]) > 0, users)
print(list(map(lambda user: user["username"].upper(), filteredResults)))


sonuc = [user["username"].upper() for user in users if len(user["tweets"]) > 0]
print(sonuc)
