class Person:
    def __init__(self, _name, _surname, _age):
        self.name = _name
        self.surname = _surname
        self.age = _age
        print("Person Nesnesi Türetildi")

    def intro(self):
        print(self.name, self.surname, self.age)

class Student(Person):
    pass

class Teacher(Person):
    pass


p1 = Person("Harun", "Uyguç", 20)
p1.intro()

s1 = Student("Esra", "Uyguç", 26)
s1.intro()

t1 = Teacher("Ad", "Soyad", 52)
t1.intro()
