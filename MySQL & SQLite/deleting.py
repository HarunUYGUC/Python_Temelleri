import mysql.connector

def deleteProduct():
    connection = mysql.connector.connect(
        host = "localhost",
        user = "root",
        password =  "1234",
        database = "node-app"
    )

    cursor = connection.cursor()

    # Bu şekilde DELETE işlemi yaparsak products tablosundaki bütün kayıtlar silinir.
    # sql = "DELETE FROM products"

    # Böyle id'si 6 olan satır silinir.
    # sql = "DELETE FROM products WHERE id = 6"

    # Bu şekilde DELETE işleminde name içerisinde s7 geçen satırlar silinir.
    sql = "DELETE FROM products WHERE name LIKE '%s7%'"

    cursor.execute(sql)

    try:
        connection.commit() # Sorgu database'e gönderilir.
        print(f"{cursor.rowcount} tane kayıt silindi.")
    except mysql.connector.Error as err:
        print("Hata: ", err)
    finally:
        connection.close() # İşimiz bitince connection kapatılmalı.
        print("Database bağlantısı kapandı.")

deleteProduct()
