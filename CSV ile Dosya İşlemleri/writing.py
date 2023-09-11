from csv import writer, reader

with open(r"c:\Users\Harun\Desktop\Python_Temelleri\CSV ile Dosya İşlemleri\cars.csv", "w") as file:
    csv_writer = writer(file)
    print(file) # Dosya İşlemleri\\cars.csv' mode='w' encoding='cp1254'>
    csv_writer.writerow(["Marka", "Model"]) # writerow() metotu ile satır satır veri ekleme işlemini çok seferde yaparız.
    csv_writer.writerow(["Toyota", "Yaris"])
    csv_writer.writerow(["Toyota", "Corolla"])

print("*" * 10)

with open(r"c:\Users\Harun\Desktop\Python_Temelleri\CSV ile Dosya İşlemleri\cars.csv", "w") as file:
    csv_writer = writer(file)
    csv_writer.writerows([["Marka", "Model"], ["Toyota", "Yaris"], ["Toyota", "Corolla"]]) # writerows() metotu ile satır satır veri ekleme işlemini tek seferde yaparız.

print("*" * 10)

with open(r"c:\Users\Harun\Desktop\Python_Temelleri\CSV ile Dosya İşlemleri\cars.csv", "a") as file:
    csv_writer = writer(file)
    csv_writer.writerow(["Toyota", "Rav4"]) # a (append) modu ile dosyaya ekleme işlemi yaparız.

print("*" * 10)

with open(r"c:\Users\Harun\Desktop\Python_Temelleri\CSV ile Dosya İşlemleri\products.csv") as file:
    csv_reader = reader(file)

    with open(r"c:\Users\Harun\Desktop\Python_Temelleri\CSV ile Dosya İşlemleri\new-products.csv", "w") as file:
        csv_writer = writer(file)

        for product_row in csv_reader:
            csv_writer.writerow([p.upper() for p in product_row])

print("*" * 10)

with open(r"c:\Users\Harun\Desktop\Python_Temelleri\CSV ile Dosya İşlemleri\products.csv", "r+") as file:
    csv_reader = reader(file)
    csv_writer = writer(file)

    next(csv_reader)
    products = [[p[0], float(p[1])*1.2, p[1], p[3], p[4]] for p in csv_reader]
    # print(products)

    file.seek(0)
    csv_writer.writerow(["ProductName","Price","IsPublished","Category","Reviews"])
    csv_writer.writerows(products)
