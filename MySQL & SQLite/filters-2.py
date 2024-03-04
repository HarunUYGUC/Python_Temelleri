import mysql.connector

def getProductById(id):
    connection = mysql.connector.connect(
        host = "localhost",
        user = "root",
        password =  "1234",
        database = "node-app"
    )

    cursor = connection.cursor()

    # sql'deki %s yerine params'daki id geçecek.
    sql = "SELECT * FROM products WHERE id=%s"
    params = (id,)

    cursor.execute(sql, params)

    result = cursor.fetchone()

    print(f"Id: {result[0]}, Name: {result[1]}, Price: {result[2]}")


getProductById(3)
