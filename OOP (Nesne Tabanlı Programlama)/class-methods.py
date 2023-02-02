class User:
    
    active_users = 0

    @classmethod
    def display_active_users(cls):
        return f"{cls.active_users} tane aktif kullanıcı var."

    @classmethod
    def from_string(cls, data_str):
        firstName, lastName, age = data_str.split(",")
        return cls(firstName, lastName, age)

    def __init__(self, _firstName, _lastName, _age):
        self.firstName = _firstName
        self.lastName = _lastName
        self.age = _age
        User.active_users += 1 
    
    def full_name(self):
        return f"{self.firstName} {self.lastName}"

    def log_out(self):
        User.active_users -= 1
        return f"{self.full_name()} uygulamadan çıkış yaptı!"

user = User("Harun", "Uyguç", 19)
print(user.firstName)

user = User.from_string("Harun, Uyguç, 19")
print(user.firstName)
