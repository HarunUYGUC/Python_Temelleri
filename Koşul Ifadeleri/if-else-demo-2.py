# 1) Bir aracın yakıt tipine göre (benzin, dizel) belirtilen bir mesafede ne kadar
# yakıt masrafı olduğunu hesaplayan uygulamayı yapınız.

x = input("Aracınızın yakıt tipi (benzin, dizel, LPG) nedir?: ")
y = float(input("Aracınız 100 km'de ortalama kaç litre yakıt tüketiyor?: "))
z = float(input("Kaç kilometre yol gideceksiniz?: "))

benzinFiyati = 20.32
dizelFiyati = 27.08
lpgFiyati = 11.03

if (x == "benzin"):
    topBenzinTL = z / 100 * y * benzinFiyati
    print(f"{z} km'de {topBenzinTL} TL'lik yakıt kullanırsınız!")
elif (x == "dizel"):
    topDizelTL = z / 100 * y * dizelFiyati
    print(f"{z} km'de {topDizelTL} TL'lik yakıt kullanırsınız!")
else:
    topLPGTL = z / 100 * y * lpgFiyati
    print(f"{z} km'de {topLPGTL} TL'lik yakıt kullanırsınız!")


    
    
    
