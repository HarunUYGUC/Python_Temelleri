# users.csv dosyasını oluştur.
# FirstName, LastName başlıkları olacak.
# Harun,Uyguç adlı kullanıcıyı ekle.
# Esra,Uyguç adlı kullanıcıyı ekle.
 
import csv

# 1- add_user() isminde 2 parametre alan fonksiyonu oluştur.

def add_user(first_name, last_name):
    with open(r"c:\Users\Harun\Desktop\Python_Temelleri\CSV ile Dosya İşlemleri\users.csv", "a", encoding="UTF-8") as file:
        csv_writer = csv.writer(file)
        csv_writer.writerow([first_name, last_name])
    
add_user("Harun", "Uyguç")
add_user("Esra", "Uyguç")

# 2- get_users() isminde tüm bilgileri getiren fonksiyonu oluştur.

def get_users():
    with open(r"c:\Users\Harun\Desktop\Python_Temelleri\CSV ile Dosya İşlemleri\users.csv", encoding="UTF-8") as file:
        csv_reader = csv.DictReader(file)
        
        for user in csv_reader:
            print(f"{user['FirstName']} {user['LastName']}")

get_users()

# 3- find_user() isminde FirstName ve LastName bilgisine göre kaydın indeksini getiren fonksiyonu oluştur.

def find_user(first_name, last_name):
    with open(r"c:\Users\Harun\Desktop\Python_Temelleri\CSV ile Dosya İşlemleri\users.csv", encoding="UTF-8") as file:
        csv_reader = csv.reader(file)

        for (index, row) in enumerate(csv_reader): # enumerate() metotu her bir verinin indeksini verinin başında belirtir.
            if (row[0] == first_name) and (row[1] == last_name):
                return index
            
        return -1
    
print(find_user("Harun", "Uyguç"))
print(find_user("Esra", "Uyguç"))
print(find_user("Kyle", "Crane"))
