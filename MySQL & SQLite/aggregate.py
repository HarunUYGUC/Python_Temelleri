import mysql.connector

def getProductInfo():
    connection = mysql.connector.connect(
        host = "localhost",
        user = "root",
        password =  "1234",
        database = "node-app"
    )

    cursor = connection.cursor()

    """
    - "COUNT(*)", tablodaki tüm satır sayılarının kaç tane olduğunu verir.
    - "SELECT COUNT(*) FROM products WHERE price > 2000", tablodaki price değeri 2000'den
    büyük olan satırların sayısını verir.
    - "COUNT(name)" şeklinde de yazılabilir.
    - "AVG(price)", tablodaki price değerlerinin ortalamasını verir.
    - Filtreleme yapmak istersek tabii ki de yapabiliriz. 
    - "SUM(price)", tablodaki price değerlerinin toplamını verir.
    - "MIN(price)", tablodaki price değerlerinin en küçüğünü verir.
    - "MAX(price)", tablodaki price değerlerinin en büyüğünü verir.
    """

    # price = () => Parantez içerisine yazdığımız yerden gelecek olan tablodaki price değerlerinin en büyüğünün
    # tablodaki hangi ürüne ait olduğunu bu şekilde bulabiliriz.
    # sql = "SELECT name FROM products WHERE price = (SELECT MAX(price) FROM products)"

    # Ayrıca yukarıdakine fiyat bilgisini eklemek istersek böyle yapabiliriz.
    # sql = "SELECT name, price FROM products WHERE price = (SELECT MAX(price) FROM products)"
    # print(f"Result: {result[0]}, Price: {result[1]}")

    sql = "SELECT name FROM products WHERE price = (SELECT MAX(price) FROM products)"

    cursor.execute(sql)

    result = cursor.fetchone()

    print(f"Result: {result[0]}")

getProductInfo()
