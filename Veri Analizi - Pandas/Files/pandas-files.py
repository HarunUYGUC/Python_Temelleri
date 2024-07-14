import pandas as pd
import sqlite3

df = pd.read_csv(r"C:\Users\Harun\Desktop\Python_Temelleri\Veri Analizi - Pandas\Files\sample.csv")
df = pd.read_json(r"C:\Users\Harun\Desktop\Python_Temelleri\Veri Analizi - Pandas\Files\sample.json", encoding="UTF-8")

df = pd.read_excel(r"C:\Users\Harun\Desktop\Python_Temelleri\Veri Analizi - Pandas\Files\sample.xlsx")
# xlsx yani Excel dosyalarını okumak için harici bir kütüphane kurmamız gereklidir.
# pip install xlrd

connection = sqlite3.connect(r"C:\Users\Harun\Desktop\Python_Temelleri\Veri Analizi - Pandas\Files\sample.db")

df = pd.read_sql_query("SELECT * FROM students", connection)
# db yani SQL dosyalarını okumak için harici bir kütüphane kurmamız gereklidir.
# pip install pysqlite3

print(df)
