# User
# Moderator

class User:

    active_users = 0

    @classmethod
    def display_active_users(cls):
        return f"Şu anda aktif {cls.active_users} kullanıcı var."

    def __init__(self, _firstname, _lastname):
        self.firstname = _firstname
        self.lastname = _lastname
        User.active_users += 1

    def fullname(self):
        return f"{self.firstname} {self.lastname}"

class Moderator(User):

    active_moderators = 0

    @classmethod
    def display_active_moderators(cls):
        return f"Şu anda aktif {cls.active_moderators} moderatör var."    

    def __init__(self, _firstname, _lastname, _community):
        super().__init__(_firstname, _lastname)
        self.community = _community
        Moderator.active_moderators += 1

    def remove_task(self):
        return f"{self.fullname()}, {self.community} göreviyle bir görevi iptal etti."

    def update_task(self):
        return f"{self.fullname()}, {self.community} göreviyle bir görevi güncelledi."


print(Moderator.display_active_moderators())
print(User.display_active_users())

u1 = User("Kyle", "Crane")
m1 = Moderator("Jade", "Aldemir", "Tower Assistant")
m2 = Moderator("Brecken", "Governor", "Tower Leader")

print(User.display_active_users())
print(Moderator.display_active_moderators())

print(m1.remove_task())
print(m2.update_task())

print(isinstance(u1, User)) # True! "u1 nesnesi User Class'ından mı?" demektir. "True" veya "False" cevabını alırız.
print(isinstance(u1, Moderator)) # False!

print(isinstance(m1, User)) # True!
print(isinstance(m1, Moderator)) # True!

print(u1.fullname())
print(m1.fullname())
