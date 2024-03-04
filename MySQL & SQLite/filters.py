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
    SELECT * FROM products WHERE id=1
    diyerek 1. id'deki tüm kolonları getir deriz.
    
    cursor.execute("SELECT * FROM products WHERE id=1")
    """

    """
    Samsung S8 ve samsung s8 olmak üzere database'imizde 2 tane ürün var fakat
    yazımları farklı olmasına rağmen iki ürün de geldi. Yani önemli olan isimlerinin aynı olması.
    Sadece Samsung şeklinde arama yaparsak hiçbir ürün gelmez. Bunun için LIKE özelliği kullanılır.
    
    Eğer bunlardan birisini istiyorsak "and price=3000" şeklinde yazarak fiyatı farklı olanı database'den çekebiliriz.
    "price>3000", "price>=3000" şeklinde kullanımlar da yapılabilir.

    "or price=3000" şeklinde de kullanılabilir.

    cursor.execute("SELECT * FROM products WHERE name='Samsung S8' or price=3000")
    """

    """
    İçerisinde Samsung yazan bütün kayıtları getirir.
    samsungdeneme, Samsung S5, samsung s7 gibi...
    cursor.execute("SELECT * FROM products WHERE name LIKE '%Samsung%'")

    Samsung ile başlasın ama sonu farklı şekilde bitebilir demek.
    cursor.execute("SELECT * FROM products WHERE name LIKE 'Samsung%'")

    Başında farklı karakterler olabilir ama Samsung ile bitsin demek.
    cursor.execute("SELECT * FROM products WHERE name LIKE '%Samsung'")
    """

    cursor.execute("SELECT * FROM products WHERE name LIKE '%Samsung%' and price=3000")

    result = cursor.fetchall()

    """
    Önceki şartlara uyan bir eleman olsa bile fetchall() metotu bu elemanı liste içerisinde getirir.
    Bu yüzden bu elemana ulaşmadan önce bir for döngüsü kullanmamız gerekiyor.
    
    fetchone() metodunu kullandığımızda ise zaten önceki şartlara uyan birden fazla eleman olsa bile
    bir tanesi geliyor bu yüzden for döngüsü kullanmamıza gerek yok. Aşağıdaki gibi yazarız. 

    print(f"Id: {result[0]}, Name: {result[1]}, Price: {result[2]}")
    """

    print(result)

    # Bu şekilde products tablosundaki name ve price kolonlarındaki bilgilere ulaşırız.
    for product in result:
        print(f"Id: {product[0]}, Name: {product[1]}, Price: {product[2]}")


getProducts()
