class Person:
    def __init__(self, _name, _surname, _age):
        self.name = _name
        self.surname = _surname
        self.age = _age
        print("Person Nesnesi Türetildi")

    def intro(self):
        print(self.name, self.surname, self.age)

""" Person Base Class'ının aldığı _name, _surname, _age bilgilerini doğal olarak Child Class'ı olan Student Class'ı
da alır. Bu bilgileri alacağını söylemek için Student Class'ının içerisinde de __init__() metotunu 
kullanmamız gerekmektedir. Bu metotu kullandığımız anda Person Class'ındaki metotu baskılarız. Bu yüzden
kayıt işlerini tekrardan Student Class'ı içerisinde yapmak yerine Person Base Class'ını kullanırız.
Bunun için __init() içerisinde Person.__init__() komutunu kullanırız. """

""" Student Child Class'ındaki ek özellikleri kaydetmek için ise Student Class'ı içerisinde self.number = _number 
şeklinde bir kayıt işlemi yapmamız gerekmektedir. """
class Student(Person):
    def __init__(self, _name, _surname, _age, _number):
        # Person.__init__(self, _name, _surname, _age) # Bununla alttaki kodun ikisinin de kullanımı aynı sonucu verir.
        super().__init__(_name, _surname, _age) # Burada super() metotunu kullanırken self parametresini kullanmayız.
        self.number = _number
        print("Student Nesnesi Türetildi")

    def study(self):
        print(f"{self.number} numaralı öğrenci ders çalışıyor.")

    def intro(self):
        print(self.name, self.surname, self.age, self.number)

class Teacher(Person):
    def __init__(self, _name, _surname, _age, _branch):
        Person.__init__(self, _name, _surname, _age)
        self.branch = _branch
        print("Teacher Nesnesi Türetildi")

    def teach(self):
        print(f"{self.name} isimli öğretmen {self.branch} eğitimini veriyor.")


p1 = Person("Harun", "Uyguç", 20)
p1.intro() # Base Class'dan.

s1 = Student("Esra", "Uyguç", 26, 97)
s1.intro() # Student Child Class'ından. Child Class'ındaki metot Base Class'daki metotu ezdi.
print(s1.number)
s1.study()

t1 = Teacher("Ad", "Soyad", 52, "Bilgisayar")
t1.intro() # Base Class'dan.
print(t1.branch)
t1.teach()
