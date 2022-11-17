class Person:
    # Yapıcı Metotlar (Constructor)
    def __init__(self, name, surname, year):
        # Object Attributes veya Instance Attributes (Nesneye Özel Olan Özellikler)
        self.name = name
        self.surname = surname
        self.year = year

    # Instance Methods
    def intro(self):
        return f"Benim adım {self.name}, soyadım {self.surname}"

    def calculate_age(self):
        return f"Benim yaşım {2022 - self.year}"


# Üretmiş Olduğumuz Nesnelere Verdiğimiz İsim = Object veya Instance idir.
p1 = Person("Sadık", "Turan", 1983)
p2 = Person("Sena", "Turan", 1999)

print(p1.intro())
print(p2.intro())

print(p1.calculate_age())
print(p2.calculate_age())
