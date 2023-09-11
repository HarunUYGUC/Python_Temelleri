import csv

""" Buradaki bilgiler anlamlı bir şekilde gösterilmez. CSV dosyasındaki gibi karmaşıktır. Okunaklı bir 
hale getirmek için her bir bilgiyi anlamlı hale getirmeliyiz yani nesne oluşturmalıyız. """

# with open(r"c:\Users\Harun\Desktop\Python_Temelleri\CSV ile Dosya İşlemleri\products.csv") as file:
#     print(file.read())


with open(r"c:\Users\Harun\Desktop\Python_Temelleri\CSV ile Dosya İşlemleri\products.csv") as file:
    csv_reader = csv.reader(file) # Nesne oluştururuz. Bunun için ilk önce csv kütüphanesini import etmeliyiz.
    print(csv_reader) # Oluşturulan nesne bilgisini yazar. <_csv.reader object at 0x000001568DA871C0>

    for p in csv_reader:
        # print(p) # Her satırı liste şeklinde virgüllerden ayırır.
        # print(p[0]) # Her satırdaki ilk elemanı yazdırır. 
        print(p[0], p[1]) # Her satırdaki ilk elemanı ve ikinci elemanı yazdırır.
    
print("*" * 10)

with open(r"c:\Users\Harun\Desktop\Python_Temelleri\CSV ile Dosya İşlemleri\products.csv") as file:
    csv_reader = csv.reader(file)
    next(csv_reader) # Diğer satıra geçer. İlk satır yani başlık kısmı önemsenmez.

    for p in csv_reader:
        # print(p[0], p[1]) # Başlıksız bir şekilde # Her satırdaki ilk elemanı ve ikinci elemanı yazdırır.
        print(f"Ürün Adı: {p[0]} - Fiyat: {p[1]}")
        
print("*" * 10)

with open(r"c:\Users\Harun\Desktop\Python_Temelleri\CSV ile Dosya İşlemleri\products.csv") as file:
    csv_reader = csv.reader(file)
    next(csv_reader)

    for p in csv_reader:
        if (p[2] == "False"): # Her satırın 2. indeksindeki IsPublished başlığı altındaki verilerin False olanlarını aldık.
            print(f"Ürün Adı: {p[0]} - Fiyat: {p[1]}")

print("*" * 10)

with open(r"c:\Users\Harun\Desktop\Python_Temelleri\CSV ile Dosya İşlemleri\products.csv") as file:
    csv_reader = csv.reader(file)
    print(list(csv_reader)) # Liste halindeki satırların hepsini başka bir listeye kayıt ettik.
