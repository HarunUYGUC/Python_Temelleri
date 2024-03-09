import mysql.connector

def getProducts():
    connection = mysql.connector.connect(
        host = "localhost",
        user = "root",
        password =  "1234",
        database = "node-app"
    )

    cursor = connection.cursor()

    # sql = "SELECT * FROM products"
    # sql = "SELECT * FROM categories"

    # - INNER JOIN diyerek iki tablonun kesişen bölümlerini alırız.
    # - INNER JOIN ile products tablosundan categories tablosuna geçiş yaparız.
    # - Ortak olan kayıtlar ON keyword'u ile belirtilmeli.

    # - ON categories.id = products.categoryid => categories tablosunun id verisi 
    # products tablosundaki categoryid ile eşleşiyor demiş oluruz.
    # - Yani products tablosundaki categoryid yerinde 1 yazıyorsa ve categories tablosunda bu 1
    # numara Telefon anlamına geliyorsa artık bu şekilde database'den products tablosundaki verilere
    # ulaştığımızda categoryid yerinde 1 değil Telefon yazacak.
    """
    sql = "SELECT * FROM products INNER JOIN categories ON categories.id = products.categoryid"
    Aslında tam anlatamadım.
    (9, 'macbook', Decimal('8000'), '4.jpg', 'iyi', 2)
    Yukarıdaki şekilde iken artık aşağıdaki şekilde olacak.
    (9, 'macbook', Decimal('8000'), '4.jpg', 'iyi', 2, 2, 'Bilgisayar')
    """

    # ('macbook', Decimal('8000'), 'Bilgisayar')
    # sql = "SELECT products.name, products.price, categories.name FROM products INNER JOIN categories ON categories.id = products.categoryid"

    # categories.name = 'Telefon' olan verileri getirir.
    # ('Iphone 8', Decimal('6000'), 'Telefon') şeklinde.
    # sql = "SELECT products.name, products.price, categories.name FROM products INNER JOIN categories ON categories.id = products.categoryid WHERE categories.name = 'Telefon'"

    # ('samsung s8', Decimal('5000'), 'Telefon')
    # sql = "SELECT products.name, products.price, categories.name FROM products INNER JOIN categories ON categories.id = products.categoryid WHERE products.name = 'Samsung S8'"

    # products as p şeklinde kısaltma tanımlayabiliriz.
    sql = "SELECT p.name, p.price, c.name FROM products as p INNER JOIN categories as c ON c.id = p.categoryid WHERE p.name = 'Samsung S8'"

    cursor.execute(sql)

    try:
        result = cursor.fetchall()
        for product in result:
            print(product)
    except mysql.connector.Error as err:
        print("Hata: ", err)
    finally:
        connection.close()
        print("Database bağlantısı kapandı.")

getProducts()
