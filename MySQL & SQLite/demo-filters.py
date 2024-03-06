# Demo Insert üzerine eklenmiş yeni soru.

# 4- Aşağıdaki sorguları yazınız.
#   a- Tüm öğrenci kayıtlarını alınız.
#   b- Tüm öğrencilerin sadece öğrenci no, ad ve soyad bilgilerini alınız.
#   c- Sadece kız öğrencilerin ad ve soyadlarını alınız.
#   d- 2003 doğumlu öğrenci bilgilerini alınız.
#   e- İsmi Ali ve doğrum tarihi 2005 olan öğrenci bilgilerini alınız.
#   f- ad veya soyadı içinde 'an' ifadesi geçen kayıtları alınız.
#   g- Kaç erkek öğrenci vardır?
#   h- Kız öğrencileri harf sırasına göre getiriniz.

import mysql.connector

class Student:
    
    connection = mysql.connector.connect(
        host = "localhost",
        user = "root",
        password = "1234",
        database = "schooldb"
    )

    mycursor = connection.cursor()

    def __init__(self, studentNumber, name, surname, birthdate, gender):
        self.studentNumber = studentNumber
        self.name = name
        self.surname = surname
        self.birthdate = birthdate
        self.gender = gender

    @staticmethod
    def studentInfo():
        # a- sql = "SELECT * FROM student"
        # b- sql = "SELECT studentnumber, name, surname FROM student"
        # c- sql = "SELECT name, surname FROM student WHERE gender='K'"
        # d- sql = "SELECT * FROM student WHERE YEAR(birthdate) = 2003"
        # MONTH(birthdate) ile ay bilgisine, DAY(birthday) ile gün bilgisine ulaşabiliriz. 
        # e- sql = "SELECT * FROM student WHERE YEAR(birthdate) = 2005 AND name = 'Ali'"
        # f- sql = "SELECT * FROM student WHERE name LIKE '%an%' OR surname LIKE '%an%'"        
        # g- sql = "SELECT COUNT(*) FROM student WHERE gender = 'E'"
        # h- sql = "SELECT name, surname FROM student WHERE gender = 'K' ORDER BY name, surname"

        # Tüm kayıtların sadece ilk 5 tanesini getirir.
        sql = "SELECT * FROM student LIMIT 5"

        Student.mycursor.execute(sql)

        try:
            results = Student.mycursor.fetchall()
            
            for result in results:
                print(f"{result}")
        except mysql.connector.Error as err:
            print("Hata: ", err)
        finally:
            Student.connection.close()
            print("Database bağlantısı kapandı.")

Student.studentInfo()
