class User:
    
    active_users = 0

    @classmethod
    def display_active_users(cls):
        return f"{cls.active_users} tane aktif kullanıcı var."

    # Instance Method yerine 
    # Class Method kullanarak aşağıdaki şekilde de nesne oluşturabiliriz.
    @classmethod
    def from_string(cls, data_str):
        firstName, lastName, age = data_str.split(",")
        return cls(firstName, lastName, age)

    # Instance Method kullanarak aşağıdaki şekilde nesne oluşturabiliriz.
    def __init__(self, _firstName, _lastName, _age):
        self.firstName = _firstName
        self.lastName = _lastName
        self.age = _age
        User.active_users += 1 

user = User("Harun", "Uyguç", 19)
print(user.firstName)

user = User.from_string("Harun, Uyguç, 19")
print(user.firstName)
