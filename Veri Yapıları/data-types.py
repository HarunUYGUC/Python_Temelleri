#integer  int
#float    float
#string   str
#boolean  bool

x = input("x: ")
y = input("y: ")

print(type(x))
print(type(y))

toplam = x + y

print("Girilen Sayıların Toplamı =", toplam) 

#input'tan alınan veriler string bir ifade olarak okunduğu için bu işlem toplama 
#işlemi olarak yapılmaz. Aldığımız veriler yan yana yazılır ve 30 sonucu yerine 
#1020 sonucu oluşur.
#Bu yüzden bizim aldığımız bilgi bir işleme girmeden önce matematiksel bir 
#dönüştürme işlemine girmeli.

x = int(input("x: "))
y = int(input("y: "))


print(type(x))
print(type(y))

toplam = x + y

print("Girilen Sayıların Toplamı =", toplam) 

#Dönüştürme işlemini yapmak için x = int(input("x: ")) komutunu yazmalıyız. 
#Buradaki int komutu input'tan alınan string (yani metinsel) 
#ifadeyi(çünkü input'tan alınan veriler her zaman string olarak okunur)
#ınteger (yani tam sayı) veri tipine dönüştürür.


age = 4
weight = 12.5
name = "Harun"
isStudent= True

print(type(age))
print(type(weight))
print(type(name))
print(type(isStudent))

#from int to float

result = float(age)

print(type(result))
print("Int to float sonucu =", type(result))
print(result)

#Int veri tipi olarak aldığımız age bilgisini float veri tipine dönüştürmek için result adında değişken oluşturduk çünkü yeni veriyi bir değişkende saklamalıyız ki bu bilgi bir işe yarsın. Bunun için 
#result = float(age) komutunun yazdık.

#from float to int

result = int(weight)

print(type(result))
print(result)

#from blooean to int

result = int(isStudent)
print(type(result))
print(result)

#Boolean veri tipindeki True int veri tipinde 1'e, False ise 0'a eşit olur çünkü bilgisayar dilinde 
#bir şey doğruysa 1 yanlışsa 0 anlamına geldiği için.