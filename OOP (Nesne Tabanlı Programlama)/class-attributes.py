class User:
    # Class seviyesinde oluşturduğumuz bir özellik yani oluşturlan nesneden bağımsız. 
    # Yani herkes için geçerli.
    active_users = 0

    # Buradan sonrası Nesne seviyesinde oluşturduğumuz özellikler.
    def __init__(self, _firstName, _lastName, _age):
        self.firstName = _firstName
        self.lastName = _lastName
        self.age = _age
        User.active_users += 1 # Class seviyesinde oluşturduğumuz özellik her yerde bu şekilde kullanılır.
    
    def full_name(self):
        return f"{self.firstName} {self.lastName}"

    def log_out(self):
        User.active_users -= 1
        return f"{self.full_name()} uygulamadan çıkış yaptı!"

print(f"Aktif Kullanıcı Sayısı: {User.active_users}")
user1 = User("Harun", "Uyguç", 19)
user2 = User("Esra", "Uyguç", 26)
print(f"Aktif Kullanıcı Sayısı: {User.active_users}")

print(user1.log_out())
print(f"Aktif Kullanıcı Sayısı: {User.active_users}")

print(f"{user1.full_name()}, {user1.age} yaşında.")
print(f"{user2.full_name()}, {user2.age} yaşında.")
