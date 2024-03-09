# 5- Aşağıdaki güncelleme sorularını yapınız.
#   a- id'ye göre aldığınız bir öğrencinin bilgilerini güncelleyiniz.
#   b- cinsiyet'e göre aldığınız bir öğrencinin bilgilerini güncelleyiniz.

import mysql.connector

class Student:
    
    connection = mysql.connector.connect(
        host = "localhost",
        user = "root",
        password = "1234",
        database = "schooldb"
    )

    mycursor = connection.cursor()

    def __init__(self, id, studentNumber, name, surname, birthdate, gender):
        # None ile eğer id belirtilmediyse demiş oluyoruz.
        # Ve id'yi otomatik 0 (sıfır) yapıyoruz..
        if (id is None):
            self.id = 0
        # Eğer id gönderilmişse id'yi o gönderilen id yapıyoruz.
        else:
            self.id = id

        self.studentNumber = studentNumber
        self.name = name
        self.surname = surname
        self.birthdate = birthdate
        self.gender = gender

    @staticmethod
    def getStudentById(id):
        sql = "SELECT * FROM student WHERE id = %s"
        value = (id,)

        Student.mycursor.execute(sql, value)

        try:
            obj = Student.mycursor.fetchone()
            return Student(obj[0], obj[1], obj[2], obj[3], obj[4], obj[5])
        except mysql.connector.Error as err:
            print("Hata: ", err)

    def updateStudent(self):
        sql = "UPDATE student SET StudentNumber = %s, Name = %s, Surname = %s, Birthdate = %s, Gender = %s WHERE Id = %s"
        values = (self.studentNumber, self.name, self.surname, self.birthdate, self.gender, self.id)

        Student.mycursor.execute(sql, values)

        try:
            Student.connection.commit()
            print(f"{Student.mycursor.rowcount} tane kayıt güncellendi.")
        except mysql.connector.Error as err:
            print("Hata: ", err)

    @staticmethod
    def getStudentsGender(gender):
        sql = "SELECT * FROM student WHERE gender = %s"
        value = (gender,)

        Student.mycursor.execute(sql, value)

        try:
            return Student.mycursor.fetchall()
        except mysql.connector.Error as err:
            print("Hata: ", err)

    @staticmethod
    def updateStudents(liste):
        sql = "UPDATE student SET StudentNumber = %s, Name = %s, Surname = %s, Birthdate = %s, Gender = %s WHERE Id = %s"
        """
        Hazırladığımız sql cümleciğine ilk olarak StudentNumber, son olarak da Id gelmeli fakat 
        gönderdiğimiz liste de ilk olarak Id var. Bu yüzden sıralamanın nasıl olması gerektiğini order listesinde tutarken
        oluşturduğumuz boş values listesine de liste listesinden order listesi sayesinde alacağımız istediğimiz sıradaki verileri 
        yazacağız. Daha sonra istediğimiz şekilde oluşan values listesini mycursor ile kullanacağız.
        """
        values = []
        order = [1, 2, 3, 4, 5, 0]

        for item in liste:
            item = [item[i] for i in order]
            values.append(item)

        Student.mycursor.executemany(sql, values)

        try:
            Student.connection.commit()
            print(f"{Student.mycursor.rowcount} tane kayıt güncellendi.")
        except mysql.connector.Error as err:
            print("Hata: ", err)

student = Student.getStudentById(35)

student.name = "Jill"
student.surname = "Valentine"

student.updateStudent()


students = Student.getStudentsGender("E")
print(students)


# Students listesinden gelen std ler bir tuple listesi olduğundan 
# aslında bunlar üzerinde bir değişiklik yapamayız.
# Bu yüzden bizim ilk önce bu tuple listelerini list'e çevirmemiz gerekiyor.

liste = []

for std in students:
    std = list(std)
    std[2] = "Mr. " + std[2] # Gender = "E" olan kayıtların name bilgisinin önüne Mr. ekledik. 

    liste.append(std)

Student.updateStudents(liste)
