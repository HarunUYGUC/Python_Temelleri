import mysql.connector
from datetime import datetime
from connection import connection 
from student import Student
from teacher import Teacher
from Class import Class

class DbManager:

    def __init__(self):
        self.connection = connection
        self.cursor = self.connection.cursor()
    
    def getStudentById(self, id):
        sql = "SELECT * FROM student WHERE id = %s"
        value = (id,)

        self.cursor.execute(sql, value)

        try:
            obj = self.cursor.fetchone()
            """
            return Student(obj[0], obj[1], obj[2], obj[3], obj[4], obj[5], obj[6])
            - student dosyası içerisinde oluşturduğumuz createStudent() metotu sayesinde artık
            yukarıdaki gibi bir kod yazmak yerine aşağıdaki gibi bir kod yazabiliriz.
            """
            return Student.createStudent(obj)
        except mysql.connector.Error as err:
            print("Error: ", err)

    def getClasses(self):
        sql = "SELECT * FROM class"
        self.cursor.execute(sql)

        try:
            obj = self.cursor.fetchall()
            return Class.createClass(obj)
        except mysql.connector.Error as err:
            print("Error: ", err) 

    def getStudentsByClassId(self, classid):
        sql = "SELECT * FROM student WHERE classid = %s"
        value = (classid,)

        self.cursor.execute(sql, value)

        try:
            obj = self.cursor.fetchall()
            return Student.createStudent(obj)
        except mysql.connector.Error as err:
            print("Error: ", err)

    def addStudent(self, student: Student):
        sql = "INSERT INTO Student(StudentNumber, Name, Surname, Birthdate, Gender, ClassId) VALUES (%s, %s, %s, %s, %s, %s)"
        value = (student.studentNumber, student.name, student.surname, student.birthdate, student.gender, student.classid)
        self.cursor.execute(sql, value)

        try:
            self.connection.commit()
            print(f"{self.cursor.rowcount} tane kayıt eklendi.")
        except mysql.connector.Error as err:
            print("Hata:", err)

    def editStudent(self, student: Student):
        sql = "UPDATE student SET StudentNumber = %s, Name = %s, Surname = %s, Birthdate = %s, Gender = %s, ClassId = %s WHERE Id = %s"
        value = (student.studentNumber, student.name, student.surname, student.birthdate, student.gender, student.classid, student.id)
        self.cursor.execute(sql, value)

        try:
            self.connection.commit()
            print(f"{self.cursor.rowcount} tane kayıt güncellendi.")
        except mysql.connector.Error as err:
            print("Hata:", err)    

    def deleteStudent(self, studentid):
        sql = "DELETE FROM student WHERE id = %s"
        value = (studentid,)
        self.cursor.execute(sql, value)

        try:
            self.connection.commit()
            print(f"{self.cursor.rowcount} tane kayıt eklendi.")
        except mysql.connector.Error as err:
            print("Hata:", err)

    def addTeacher(self, teacher: Teacher):
        pass

    def editTeacher(self, teacher: Teacher):
        pass

    # __init__() metodu sınıfı çağırdığımız anda otomatik olarak başta kullanıldığı gibi
    # __del__() metodu da otomatik olarak sonda kullanılır.
    def __del__(self):
        self.connection.close()
        print("Database'den Çıkış Yapıldı.")


db = DbManager()

# print(student.name)
# createStudent() metodunu oluşturduğumuz için artık yukarıdaki 
# kodu aşağıdaki şekilde yazmamız gerekiyor.
"""
student = db.getStudentById(32)
print(student[0].name)
print(student[0].surname)
"""

"""
students = db.getStudentsByClassId(1)
print(students[0].name)
print(students[4].name)
"""

"""
student = db.getStudentById(32)

student[0].name = "Ahmet"
student[0].surname = "Yılar"
student[0].studentNumber = "501"

db.addStudent(student[0])
"""

student = db.getStudentById(32)

student[0].name = "Ada"
student[0].surname = "Wong"

db.editStudent(student[0])
