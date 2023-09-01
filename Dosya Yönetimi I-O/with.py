# file = open(r"c:\Users\Harun\Desktop\Python_Temelleri\Dosya Yönetimi I-O\msg-3.txt")
# print(file.read())
# file.close()

# Yukarıdaki gibi open(), close() yapmak yerine aşağıdaki gibi with open() yaparsak açılan dosya with kapsamı alanı içerisinden çıktığı anda 
# otomatik olarak kapanacaktır.


with open(r"c:\Users\Harun\Desktop\Python_Temelleri\Dosya Yönetimi I-O\msg-3.txt") as file:
    print(file.read(10))
    print(file.tell()) # Cursor'un o anda nerede olduğunu söyler.
    print(file.read())

""" Burada bir ilginçlik var. Böyle bir şey keşfettim. """
print("*" * 10)
with open(r"c:\Users\Harun\Desktop\Python_Temelleri\Dosya Yönetimi I-O\msg-3.1.txt") as file:
    print(file.read(10))
    print(file.tell()) # Cursor'un o anda nerede olduğunu söyler.
    print(file.read())

print("*" * 10)
with open(r"c:\Users\Harun\Desktop\Python_Temelleri\Dosya Yönetimi I-O\msg-2.txt") as file:
    for i in file:
        # print(i) # Bu şekilde yazma işlemi yaparsak her satırdan sonra bir boş satır olur. Bunu önlemek için aşağıdaki gibi bir kod yazmalıyız.
        print(i, end="") # end operatörü


print("*" * 10)
try:
    with open(r"c:\Users\Harun\Desktop\Python_Temelleri\Dosya Yönetimi I-O\nomsg.txt") as file:
        for i in file:
            print(i, end="")
except FileNotFoundError as e:
    print("Dosya okuma hatası: ", e)
finally:
    print("Dosya kapandı.")
   

print("*" * 10)
# encoding="utf-8" olarak encoding türünü belirtirsek okuduğumuz dosyadaki Türkçe karakterleri okumama sorunu düzelir.
with open(r"c:\Users\Harun\Desktop\Python_Temelleri\Dosya Yönetimi I-O\msg-3.2.txt", encoding="utf-8") as file:
    for i in file:
        print(i, end="")
