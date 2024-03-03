"""
MySQL Workbench'de oluşturduğumuz Schema'lar Database'dir.
Bu oluşturduğumuz database'ler MySQL Local Server'ında saklanır.
"""

# 1 - Workbench IDE ile schooldb isminde bir database oluşturup Student tablosunu ekleyiniz.
# Id, StudentNumber, Name, Surname, Birthdate, Gender

# 2- Database bağlantısını oluşturunuz.

import mysql.connector

connection = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "1234",
    database = "schooldb"
)

mycursor = connection.cursor()

mycursor.execute("Show Databases")

for i in mycursor:
    print(i)
