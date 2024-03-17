from dbmanager import DbManager
from student import Student
import datetime

class App:
    def __init__(self):
        self.db = DbManager()

    def initApp(self):
        msg = "************ \n1-Öğrenci Listesi \n2-Öğrenci Ekle \n3-Öğrenci Güncelle \n4-Öğrenci Sil \n5-Öğretmen Ekle \n6-Sınıflara Göre Dersler \n7-Çıkış (E/Ç)"

        while True:
            print(msg)
            islem = input("Seçim: ")

            if (islem == "1"):
                self.displayStudents()
            elif (islem == "2"):
                self.addStudent()
            elif (islem == "3"):
                self.editStudent()  
            elif (islem == "4"):
                self.deleteStudent()       
            elif (islem == "E") or (islem == "Ç"):
                break
            else:
                print("Yanlış Seçim!!!")

    def displayClasses(self):
        classes = self.db.getClasses()

        for c in classes:
            print(f"{c.id}: {c.name}")

    def displayStudents(self):
        self.displayClasses()
        classid = int(input("Hangi Sınıf?: "))
        students = self.db.getStudentsByClassId(classid)

        print("Öğrenci Listesi: ")

        # for index, std in enumerate(students):
        #     print(f"{index + 1}- {std.name} {std.surname}")

        for std in students:
            print(f"{std.id}- {std.name} {std.surname}")

        return classid

    def addStudent(self):
        self.displayClasses()

        classid = int(input("Hangi Sınıf?: "))
        number = input("Numara: ")
        name = input("Ad: ")
        surname = input("Soyad: ")
        year = int(input("Yıl:"))
        month = int(input("Ay: "))
        day = int(input("Gün: "))
        birthdate = datetime.date(year, month, day)
        gender = input("Cinsiyet (E/K): ")

        student = Student(None, number, name, surname, birthdate, gender, classid)
        self.db.addStudent(student)

    def editStudent(self):
        classid = self.displayStudents()
        studentid = int(input("Öğrenci ID: "))
        student = self.db.getStudentById(studentid)

        # Kullanıcı bir değer girerse güncelleme yapılacak, girmezse eski haline dönecek.
        student[0].name = input("Name: ") or student[0].name
        student[0].surname = input("Surname: ") or student[0].surname
        student[0].gender = input("Gender (E/K): ") or student[0].gender
        student[0].classid = input("Sınıf: ") or student[0].classid
        
        # Bu bilgiler int iken bilgi girmezsek hata veriyor, 
        # int değilken ise bilgi girersek hata veriyor. 
        year = int(input("Year: ")) or student[0].birthdate.year
        month = int(input("Month: ")) or student[0].birthdate.month
        day = int(input("Day: ")) or student[0].birthdate.day
        student[0].birthdate = datetime.date(year, month, day)
        
        self.db.editStudent(student[0])

    def deleteStudent(self):
        classid = self.displayStudents()
        studentid = int(input("Öğrenci ID: "))
        self.db.deleteStudent(studentid)
        

app = App()
app.initApp()
