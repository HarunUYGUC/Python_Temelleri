import mysql.connector

# Birden fazla veri eklemek için.
def insertProducts(list):
    connection = mysql.connector.connect(
        host = "localhost",
        user = "root",
        password =  "1234",
        database = "node-app"
    )

    cursor = connection.cursor()

    sql = "INSERT INTO Products(name, price, imageUrl, description) VALUES(%s, %s, %s, %s)"
    values = list
    
    # Birden fazla veri eklemek için execute değil executemany metotunu kullanmalıyız.
    cursor.executemany(sql, values) # Sorgu çalıştırılır. sql ile values birleştirilir.
   
    try:
        connection.commit() # Sorgu database'e gönderilir.
        print(f"{cursor.rowcount} tane kayıt eklendi.")
        print(f"Son eklenen kaydın id numarası: {cursor.lastrowid}")
    except mysql.connector.Error as err:
        print("Hata: ", err)
    finally:
        connection.close() # İşimiz bitince connection kapatılmalı.
        print("Database bağlantısı kapandı.")


list = []

while True:
    name = input("Ürün adı: ")
    price = input("Ürün fiyatı: ")
    imageUrl = input("Ürün resim adı: ")
    description = input("Ürün açıklaması: ")
    
    """
    insertProducts(list) fonksiyonunu oluşturmadan ve list kullanmadan
    insertProduct(name, price, imageUrl, description) kodunu her seferinde bir tane 
    veri eklemek için burada çağırabiliriz aslında ama bu kötü bir durumdur.
    Çünkü kaç tane veri eklersek o kadar kez database ile bağlantı kurmamız gerekecek bu şekilde.
    Ama list oluşturup hepsini toplu şekilde gönderirsek database ile bir kez bağlantı kuracağız.
    """
    
    # Devam etmek istiyor musunuz sorusuna hayır diyene kadar alınan cevapları
    # bu tuple listesinde saklayacağız. Hayır dediğinde ise bu tuple listesindeki
    # verileri veri tabanına aktaracağız.
    list.append((name, price, imageUrl, description)) # Tuple listesi.

    result = input("Devam etmek istiyor musunuz? (e / h): ")
    
    if (result == "h"):
        print("Kayıtlarınız veri tabanına aktarılıyor...")
        print(list)
        insertProducts(list)
        break
