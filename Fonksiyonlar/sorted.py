sayilar = [1, 53, 45, 67, 97, 5, 7]

sayilar.sort()

print(sayilar)


sayilar = [1, 53, 45, 67, 97, 5, 7]

sonuc = sorted(sayilar)

print(sonuc)

print(sayilar)


sayilar = [1, 53, 45, 67, 97, 5, 7]

sonuc = sorted(sayilar, reverse=True)

print(sonuc)



users = [
    {"username": "sadikturan", "tweets": ["tweet1", "tweet2"], "email": "info@gmail.com"},
    {"username": "cinarturan", "tweets": [], "email": "info@gmail.com"},
    {"username": "senaturan", "tweets": ["tweet1"], "name": "", "phone": "455545523"}
]
sonuc = sorted(users, key=len)
print(sonuc)

sonuc = sorted(users, key=len, reverse=True)
print(sonuc)

sonuc = sorted(users, key=lambda user: user["username"])
print(sonuc)

sonuc = sorted(users, key=lambda user: len(user["tweets"]))
print(sonuc)


kurslar = [
    {"title": "python kursu", "students": "25000"},
    {"title": "web geliştirme kursu", "students": "35000"},
    {"title": "javascript kursu", "students": "5000"}
]

sonuc = sorted(kurslar, key=lambda kurs: kurs["students"])
print(sonuc)

sonuc = sorted(kurslar, key=lambda kurs: kurs["students"], reverse=True)
print(sonuc)

sonuc = list(map(lambda kurs: kurs["title"], sorted(kurslar, key=lambda kurs: kurs["students"], reverse=True)))
print(sonuc)
