import sqlite3

# SQLite kullanımı MySQL ile tamamen aynı. 
# Sadece database ile bağlantı kurulumu farklı.
# Çünkü MySQL online server tabanlı iken SQLite yerel bilgisayar ile ilgilidir.

"""
Oluşan node_app.db database dosyasını DB Browser for SQLite
uygulamasında görmek için node_app.db dosyasına sağ tıkladıktan sonra
Reveal in File Explorer dedikten sonra karşımıza gelen node_app.db
dosyasını uygulamanın sol kısmına sürükleyip bırakmalıyız.
"""
"""
Daha sonra DB Browser for SQLite uygulamasına gelen Tablolar'a tıklayıp tablo oluştur
diyip sıfırdan database oluşturmak yerine internetten hazır database bulup indirebiliriz.
İndirdiğimiz bu database dosyasını .zip'den çıkarıp node_app.db dosyasını bulunduğu klasöre taşımalıyız.
"""

# node_app.db ismindeki veri tabanına bağlanırız.
# Veri tabanı, sqlite-db.py dosyasının olduğu klasörde yoksa oluşturulur.
connection = sqlite3.connect(r"C:\Users\Harun\Desktop\Python_Temelleri\MySQL & SQLite\SQLite\chinook.db")
cursor = connection.cursor()

cursor.execute("SELECT * FROM customers")
results = cursor.fetchall()

for i in results:
    print(i)

connection.close()
