import mysql.connector

def deleteProduct(id):
    connection = mysql.connector.connect(
        host = "localhost",
        user = "root",
        password =  "1234",
        database = "node-app"
    )

    cursor = connection.cursor()

    sql = "DELETE FROM products WHERE id = %s"
    values = (id,)

    cursor.execute(sql, values)

    try:
        connection.commit() # Sorgu database'e gönderilir.
        print(f"{cursor.rowcount} tane kayıt silindi.")
    except mysql.connector.Error as err:
        print("Hata: ", err)
    finally:
        connection.close() # İşimiz bitince connection kapatılmalı.
        print("Database bağlantısı kapandı.")

deleteProduct(4)
