# key - value

# 41 => Kocaeli
# 34 => İstanbul

sehirler = ["Kocaeli", "İstanbul"]
plakalar = [41, 34]

print(sehirler[0], plakalar[0])
print(sehirler[1], plakalar[1])

print(plakalar[sehirler.index("İstanbul")])

print(plakalar[sehirler.index("İstanbul")], "İstanbul") # Kendim denedim.




plakalar = {"Kocaeli":41, "İstanbul":34}
print(plakalar["Kocaeli"])
print(plakalar["İstanbul"])

plakalar["Rize"] = 53
print(plakalar)


plakalar["İzmir"] = 35
print(plakalar)


ogrenciler = {100:"Çınar", 101:"Ada"}
print(ogrenciler[100])


ogrenciler = {
    100: {
        "Ad": "Çınar",
        "Soyad": "Turan",
        "Yaş": 4,
        "Notlar": [70, 80, 70]
    },
    101: {
        "Ad": "Ada",
        "Soyad": "Bilgi",
        "Yaş": 10
    }
}

print(ogrenciler[100])

print(ogrenciler[100]["Ad"])

print(ogrenciler[100]["Notlar"][0])

ortalama = (ogrenciler[100]["Notlar"][0] + ogrenciler[100]["Notlar"][1] + ogrenciler[100]["Notlar"][2]) / 3
print(ortalama)
