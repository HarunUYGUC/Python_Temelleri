import mysql.connector

def getProducts():
    connection = mysql.connector.connect(
        host = "localhost",
        user = "root",
        password =  "1234",
        database = "node-app"
    )

    cursor = connection.cursor()
    
    """
    - "ORDER BY name" dediğimiz için alfabetik sıraya göre kayıtları verir.
    - "ORDER BY price" veya "ORDER BY id" dediğimizde küçükten büyüğe bir sıralama yapar.
    - Bunları "ORDER BY name ASC" şeklinde yazarsak sonuç yine yukarıdakiler gibi olur.
    - "ORDER BY name DESC" yazarsak ise sonuçlar sondan başa doğru olur.
    - "ORDER BY name, price" şeklinde yazarsak ise ilk önce name'e göre bir sıralama yapar ve eğer 
    aynı name'den birden fazla varsa onları da price'a göre sıralar.
    """

    cursor.execute("SELECT * FROM products ORDER BY name, price")
    
    try:
        result = cursor.fetchall()
        for product in result:
            print(f"Id: {product[0]}, Name: {product[1]}, Price: {product[2]}")
    except mysql.connector.Error as err:
            print("Hata: ", err)
    finally:
         connection.close()
         print("Database bağlantısı kapandı.")


getProducts()
