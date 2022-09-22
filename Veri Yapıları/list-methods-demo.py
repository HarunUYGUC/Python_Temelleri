isimler = ['Ada', 'Yiğit', 'Hasan', 'Beril']
yaslar = [1998, 2000, 1998, 1987]
        
# 1- "Cenk" ismini listenin sonuna ekleyiniz.

isimler.append("Cenk")
print(isimler)

isimler = ['Ada', 'Yiğit', 'Hasan', 'Beril']

isimler.insert(len(isimler), "Cenk")
print(isimler)

# 2- "Sena" değerini listenin başına ekleyiniz.

isimler = ['Ada', 'Yiğit', 'Hasan', 'Beril']

isimler.insert(0, "Sena")
print(isimler)

# 3- "Yiğit" ismini listeden siliniz.

isimler = ['Ada', 'Yiğit', 'Hasan', 'Beril']

isimler.remove("Yiğit")
print(isimler)

# 4- "Yiğit" isminin indeksi nedir ?

isimler = ['Ada', 'Yiğit', 'Hasan', 'Beril']

print(isimler.index("Yiğit"))

# 5- "Beril" listenin bir elemanı midır ?

isimler = ['Ada', 'Yiğit', 'Hasan', 'Beril']

print(isimler.index("Beril"))

# Hocanın yöntemi:

print("Beril" in isimler)

# 6- Liste elemanlarını ters çevirin.

isimler = ['Ada', 'Yiğit', 'Hasan', 'Beril']

isimler.reverse()
print(isimler)

# 7- Liste elemanlarını alfabetik olarak sıralayınız.

isimler = ['Ada', 'Yiğit', 'Hasan', 'Beril']

isimler.sort()
print(isimler)

# 8- yaslar listesini rakamsal büyüklüğe göre sıralayınız.

yaslar = [1998, 2000, 1998, 1987]

yaslar.sort()
print(yaslar)

# 9- str = "IPhone X,IPhone XR" karakter dizisini listeye çeviriniz.

markalar = ["Iphone X", "Iphone XR"]
print(markalar)

# Hocaın yöntemi:

s = "Iphone X,Iphone XR"
print(s.split(","))

# 10- yaslar dizisinin en büyük ve en küçük elemanı1 nedir ?

yaslar = [1998, 2000, 1998, 1987]

print(min(yaslar))

print(max(yaslar))

# 11- yaslar dizisinde kaç tane 1998 değeri vardır ?

yaslar = [1998, 2000, 1998, 1987]

print(yaslar.count(1998))

# 12- yaslar dizisinin tüm elemanlarını siliniz.

yaslar.clear()
print(yaslar)

# 13- Kullanicıdan alacağınız 3 tane marka bilgisini bir listede saklayınız.

# Hocanın Yöntemi:

markalar = []

marka = input("Marka :")
markalar.append(marka)

marka = input("Marka :")
markalar.append(marka)

marka = input("Marka :")
markalar.append(marka)

print(markalar)


# Kendim bir şey denedim.
deneme = ""

deneme = input("Deneme : ")
print(deneme)

sayi = input("Sayınızı Giriniz : ")
sayi = int(sayi)
islem = sayi * 3
print(islem)

