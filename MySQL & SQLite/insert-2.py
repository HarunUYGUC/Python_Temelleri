import mysql.connector

# Bir tane veri eklemek için.
def insertProduct(name, price, imageUrl, description):
    connection = mysql.connector.connect(
        host = "localhost",
        user = "root",
        password =  "1234",
        database = "node-app"
    )

    cursor = connection.cursor()

    sql = "INSERT INTO Products(name, price, imageUrl, description) VALUES(%s, %s, %s, %s)"
    values = (name, price, imageUrl, description)
    
    cursor.execute(sql, values) # Sorgu çalıştırılır. sql ile values birleştirilir.
   
    try:
        connection.commit() # Sorgu database'e gönderilir.
        print(f"{cursor.rowcount} tane kayıt eklendi.")
        print(f"Son eklenen kaydın id numarası: {cursor.lastrowid}")
    except mysql.connector.Error as err:
        print("Hata: ", err)
    finally:
        connection.close() # İşimiz bitince connection kapatılmalı.
        print("Database bağlantısı kapandı.")


name = input("Ürün adı: ")
price = input("Ürün fiyatı: ")
imageUrl = input("Ürün resim adı: ")
description = input("Ürün açıklaması: ")

insertProduct(name, price, imageUrl, description)
