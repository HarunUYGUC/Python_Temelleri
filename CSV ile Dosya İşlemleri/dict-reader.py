from csv import DictReader

with open(r"c:\Users\Harun\Desktop\Python_Temelleri\CSV ile Dosya İşlemleri\products.csv") as file:
    csv_reader = DictReader(file)
    print(csv_reader) # <csv.DictReader object at 0x000002785DF0C290>

    for row in csv_reader:
        # print(row) # {"ProductName": "Iphone 11", "Price": "7000", ...} vb. olarak dictionary şeklinde her satırdaki veriyi ve başlığını alırız. 
        # Yani başlık satırı diğer satırlara ve gelmesi gereken yerlere dağılır.
        
        # print(row["ProductName"]) # DictReader() sayesinde oluşturduğumuz dictionarydeki key verisi ile value değerlerine ulaşabiliriz.
        print(row["ProductName"], row["Price"])

print("*" * 10)

with open(r"c:\Users\Harun\Desktop\Python_Temelleri\CSV ile Dosya İşlemleri\products.csv") as file:
    csv_reader = DictReader(file)

    for p in csv_reader:
        if (p["Category"] == "Telefon"):
            print(p["ProductName"], p["Price"])

print("*" * 10)

# CTRL + SHIFT + L ile ilgili dosyadaki seçtiğimiz karakteri tüm dosyadan seçebiliriz.
# Örneğin products.csv dosyasındaki virgülleri | işareti ile değiştirmek için tek bir virgülü seçtikten sonra CTRL + SHIFT + L yaparak hepsini seçebiliriz.

with open(r"c:\Users\Harun\Desktop\Python_Temelleri\CSV ile Dosya İşlemleri\products-2.csv") as file:
    csv_reader = DictReader(file, delimiter="|") # virgül yerine | işaretinden verilerin ayrılacağını belirtmek için delimiter= parametresini kullanıyoruz.

    for p in csv_reader:
        if (p["Category"] == "Telefon"):
            print(p["ProductName"], p["Price"])
