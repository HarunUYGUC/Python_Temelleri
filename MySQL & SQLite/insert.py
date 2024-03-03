import mysql.connector

def insertProduct():
    connection = mysql.connector.connect(
        host = "localhost",
        user = "root",
        password =  "1234",
        database = "node-app"
    )

    cursor = connection.cursor()

    # Kayıt eklemek için SQL cümleciği oluşturmalıyız.
    """
    node-app database'inde Columns'ları oluştururken Nullable'ı No ('İlla bir değer gönderilsin mi?' 
    diye sormuştu başta kolonları oluştururken. Biz de tik atmıştık.) olarak işaretlediysek
    Products() ve Values() içerisinde bunları yazmalıyız. Yes olarak işaretlediklerimizi ise 
    yazmamıza gerek yok. Ayrıca id otomatik olarak artsın olarak işaretlediğimiz için onu da 
    yazmamıza gerek yok.
    """

    sql = "INSERT INTO Products(name, price, imageUrl, description) VALUES(%s, %s, %s, %s)"
    values = ("Samsung S5", 1000, "1.jpg", "iyi telefon")
    
    cursor.execute(sql, values) # Sorgu çalıştırılır. sql ile values birleştirilir.
   
    try:
        connection.commit() # Sorgu database'e gönderilir.
    except mysql.connector.Error as err:
        print("Hata: ", err)
    finally:
        connection.close() # İşimiz bitince connection kapatılmalı.
        print("Database bağlantısı kapandı.")

insertProduct()
