import mysql.connector

mydb = mysql.connector.connect(
    host = "localhost", 
    # Şu an yazdığımız adres yerel serverın adresi yani bilgisayarımızdaki database'in.
    # İnternet üzerinden database servisi aldığımızda 192.23.45.56 gibi bir adresi buraya yazacağız.
    user = "root",
    password = "1234",
    database = "mydatabase"
)

print(mydb) # Oluşturulan objeyi yazar.

# MySQL'de database oluşturmak ve üzerinde işlemler yapmak için gerekli.
mycursor = mydb.cursor()

# mydatabase adında MySQL'de bir database oluşturur.
mycursor.execute("CREATE DATABASE mydatabase")

# Oluşturulan database'leri gösterir.
mycursor.execute("SHOW DATABASES")

# Yukarıdakini yazdırmaya yarar.
for x in mycursor:
    print(x)

# Bağlandığımız database'de yeni tablo oluşturur.
mycursor.execute("CREATE TABLE customers (name VARCHAR(255), address VARCHAR(255))")

"""
Burada yaptıklarımızı zaten bunları yapmak için indirmiş olduğumuz
MySQL Workbench üzerinden daha rahat bir şekilde yapabiliriz.
Ama istersek bu şekilde de yapabiliyoruz.
"""
