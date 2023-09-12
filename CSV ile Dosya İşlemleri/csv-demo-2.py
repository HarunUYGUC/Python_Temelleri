""" Bende bu kodlar hatalı çalışıyor!!! """

import csv

# update_users() isminde bir fonksiyon ekleyip kayıt güncelleyiniz.

def update_users(f_name, l_name, new_first, new_last):
    with open(r"c:\Users\Harun\Desktop\Python_Temelleri\CSV ile Dosya İşlemleri\users.csv") as file:
        csv_reader = csv.reader(file)
        users = list(csv_reader)

    with open(r"c:\Users\Harun\Desktop\Python_Temelleri\CSV ile Dosya İşlemleri\users.csv", "w") as file:
        csv_writer = csv.writer(file)
        
        count = 0
        for user in users:
            if (user[0] == f_name) and (user[1] == l_name):
                csv_writer.writerow([new_first, new_last])
                count += 1
            else:
                csv_writer.writerow(user)
        
    return f"{count} tane kayıt güncellendi."

print(update_users("Harun", "Uyguç", "Leon", "Kennedy"))

# delete_users() isminde bit metot ekleyip kayıt siliniz.

def delete_users(f_name, l_name):
    with open(r"c:\Users\Harun\Desktop\Python_Temelleri\CSV ile Dosya İşlemleri\users.csv") as file:
        csv_reader = csv.reader(file)
        users = list(csv_reader)

    with open(r"c:\Users\Harun\Desktop\Python_Temelleri\CSV ile Dosya İşlemleri\users.csv", "w") as file:
        csv_writer = csv.writer(file)
        
        count = 0
        for user in users:
            if (user[0] == f_name) and (user[1] == l_name):
                count += 1
            else:
                csv_writer.writerow(user)
        
    return f"{count} tane kayıt silindi."

print(delete_users("Harun", "Uyguç"))
