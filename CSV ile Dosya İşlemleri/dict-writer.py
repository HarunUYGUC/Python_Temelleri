from csv import DictWriter, DictReader

with open(r"c:\Users\Harun\Desktop\Python_Temelleri\CSV ile Dosya İşlemleri\products.csv", "w") as file:
    headers = ["ProductName","Price","IsPublished","Category","Reviews"]
    csv_writer = DictWriter(file, headers)
    csv_writer.writeheader() # Başlıkları yazdırırken writeheader(); satırları yazdırırken writerow() ve writerows() kullanılıyor.

    csv_writer.writerow({
        "ProductName": "Iphone 7",
        "Price": 3000,
        "IsPublished": True,
        "Category": "Telefon",
        "Reviews": 4.7
    })
    csv_writer.writerow({
        "ProductName": "Iphone 8",
        "Price": 4000,
        "IsPublished": True,
        "Category": "Telefon",
        "Reviews": 4.8
    })

""" Yukarıdaki gibi yapmak yerine bu şekilde de yapabiliriz. """

with open(r"c:\Users\Harun\Desktop\Python_Temelleri\CSV ile Dosya İşlemleri\products.csv", "w") as file:
    headers = ["ProductName","Price","IsPublished","Category","Reviews"]
    csv_writer = DictWriter(file, headers)
    csv_writer.writeheader() 

    csv_writer.writerows([
        {
            "ProductName": "Iphone 7",
            "Price": 3000,
            "IsPublished": True,
            "Category": "Telefon",
            "Reviews": 4.7
        },
        {
            "ProductName": "Iphone 8",
            "Price": 4000,
            "IsPublished": True,
            "Category": "Telefon",
            "Reviews": 4.8
        },
        {
            "ProductName": "Iphone X",
            "Price": 5000,
            "IsPublished": True,
            "Category": "Telefon",
            "Reviews": 4.9
        }
    ])

with open(r"c:\Users\Harun\Desktop\Python_Temelleri\CSV ile Dosya İşlemleri\products.csv", "a") as file:
    headers = ["ProductName","Price","IsPublished","Category","Reviews"]
    csv_writer = DictWriter(file, headers)
    # csv_writer.writeheader() # Bu satırı tekrar yazmamıza gerek yok çünkü zaten başlık bilgisi olan bir csv dosyasına veri ekleyeceğiz.
    # Bu satırı yazarsak tekrar orta bir yerlere başlık eklenir.

    csv_writer.writerow(
        {
            "ProductName": "Iphone 12",
            "Price": 8000,
            "IsPublished": True,
            "Category": "Telefon",
            "Reviews": 4.93
        }
    )


def price_with_tax(price):
    return float(price) * 1.18

with open(r"c:\Users\Harun\Desktop\Python_Temelleri\CSV ile Dosya İşlemleri\products.csv") as file:
    csv_reader = DictReader(file)
    products = list(csv_reader)

with open(r"c:\Users\Harun\Desktop\Python_Temelleri\CSV ile Dosya İşlemleri\new-products-2.csv", "w") as file:
    headers = ["ProductName","Price","IsPublished","Category","Reviews"]
    csv_writer = DictWriter(file, headers)
    csv_writer.writeheader() 

    for p in products:
        csv_writer.writerow({
            "ProductName": p["ProductName"],
            "Price": price_with_tax(p["Price"]),
            "IsPublished": p["IsPublished"],
            "Category": p["Category"],
            "Reviews": p["Reviews"]
        })

# CTRL + K + U yorum satırını kaldırır.
