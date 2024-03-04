import mysql.connector

def getProducts():
    connection = mysql.connector.connect(
        host = "localhost",
        user = "root",
        password =  "1234",
        database = "node-app"
    )

    cursor = connection.cursor()

    # * diyerek products tablosundaki bütün kolonları getir demiş oluyoruz.
    cursor.execute("SELECT * FROM products")

    # fetchall() metotu products tablosundaki bütün kayıtları getirir. Yani tüm satırları getirir.
    result = cursor.fetchall()

    """
    fetchall() metotu yerine fetchone() metodunu kullanırsak 
    bütün kayıtlar değil de bir tane kayıt getirilir.

    result = cursor.fetchone()

    Bir tane kaydı çektiğimiz için bu şekilde ekranda yazdırırız.

    print(f"Name: {result[0]} - Price: {result[1]}")
    """

    # Bu şekilde tüm products tablosunu tek bir listede verir.
    print(result)

    # Bu şekilde tüm products tablosundakileri satır satır verir.
    for product in result:
        print(product)

    # Bu şekilde products tablosundaki name ve price kolonlarındaki bilgilere ulaşırız.
    for product in result:
        print(f"Name: {product[1]} - Price: {product[2]}")

    """
    cursor.execute("SELECT * FROM products")
    diyerek tüm kolonları almak yerine aşağıdaki gibi yazarak sadece
    istediğimiz kolonları da database'den çekebiliriz. 

    cursor.execute("SELECT name, price FROM products")
    
    Bu şekilde yaparsak yukarıdaki for döngüsü bu şekilde yazılır.
    Çünkü diğerindeki 0. indiste her bir products'ın id'sini tutan kolon var. 

    for product in result:
        print(f"Name: {product[0]} - Price: {product[1]}")
    """


getProducts()
