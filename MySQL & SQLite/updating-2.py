import mysql.connector

def updateProduct(id, name, price):
    connection = mysql.connector.connect(
        host = "localhost",
        user = "root",
        password =  "1234",
        database = "node-app"
    )

    cursor = connection.cursor()

    sql = "UPDATE products SET name = %s, price = %s WHERE id = %s"
    values = (name, price, id)

    cursor.execute(sql, values)

    try:
        connection.commit() # Sorgu database'e gönderilir.
        print(f"{cursor.rowcount} tane kayıt güncellendi.")
    except mysql.connector.Error as err:
        print("Hata: ", err)
    finally:
        connection.close() # İşimiz bitince connection kapatılmalı.
        print("Database bağlantısı kapandı.")    

updateProduct(1, "Iphone 8", 6000)

# Aşağıdaki şekilde isim alanını boş bir şekilde gönderirsek bunun karşılığı False'idir.
# Ve buna göre sql cümleciğini if şartlarıyla şekillendirebiliriz.
# updateProduct(1, "", 6000)
