import mysql.connector

def updateProduct():
    connection = mysql.connector.connect(
        host = "localhost",
        user = "root",
        password =  "1234",
        database = "node-app"
    )

    cursor = connection.cursor()

    """
    Bu şekilde UPDATE işlemi yaparsak products tablosundaki bütün
    name alanları burada belirttiğimiz gibi olur.
    sql = "UPDATE products SET name = 'Samsung S10'"
    """

    # Bu şekilde yazarsak id'si 5 olan satırın name bilgisini değiştirir.
    # sql = "UPDATE products SET name = 'Samsung S10' WHERE id = 5"

    # Bu şekilde yazarsak id'si 1 olan satırın name ve price bilgisini değiştirir.
    sql = "UPDATE products SET name = 'Samsung S10', price = 5000 WHERE id = 1"

    cursor.execute(sql)

    try:
        connection.commit() # Sorgu database'e gönderilir.
        print(f"{cursor.rowcount} tane kayıt güncellendi.")
    except mysql.connector.Error as err:
        print("Hata: ", err)
    finally:
        connection.close() # İşimiz bitince connection kapatılmalı.
        print("Database bağlantısı kapandı.")    

updateProduct()
