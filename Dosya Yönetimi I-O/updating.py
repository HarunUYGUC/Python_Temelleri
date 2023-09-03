with open(r"c:\Users\Harun\Desktop\Python_Temelleri\Dosya Yönetimi I-O\markalar.txt", "a")  as file:
    file.write("6- BMW") # "a" append (ekle) modu ile dosyanın sonunda ekleme yaparız.

with open(r"C:\Users\Harun\Desktop\Python_Temelleri\Dosya Yönetimi I-O\markalar.txt") as file:
    print(file.read())


print("*" * 10)

with open(r"C:\Users\Harun\Desktop\Python_Temelleri\Dosya Yönetimi I-O\markalar.txt", "r+", encoding="UTF-8")  as file:
    markalar = file.read() # Dosyadaki verileri okuyup bir listeye kaydediyoruz.
    markalar = "1- Toyota \n" + markalar # Listenin başına Toyota bilgisini ekleyip sonrasına markalar listesine eklediğimiz verileri ekliyoruz.
    file.seek(0) # Okuma işlemi yapıldığı için cursor dosyanın sonundadır. Bizim cursor'u en başa getirmemiz gerekmektedir.
    file.write(markalar) # Cursor en başa geldikten sonra markalar listesindeki yeni verileri tekrar dosyaya yazabiliriz.

with open(r"C:\Users\Harun\Desktop\Python_Temelleri\Dosya Yönetimi I-O\markalar.txt") as file:
    print(file.read())


print("*" * 10)

with open(r"C:\Users\Harun\Desktop\Python_Temelleri\Dosya Yönetimi I-O\markalar.txt", "r+", encoding="UTF-8")  as file:
    # Dosyadaki herbir satırı dizi elemanı olarak algılayıp verileri dizi şeklinde kaydetmek için readlines() metotunu kullanmalıyız.
    # Bu sayede istediğimiz indekse ulaşıp değişiklik yapabiliriz.
    markalar = file.readlines()
    markalar.insert(2, "3- Renault \n") # Dizinin 2. indeksine yani dosyanın 2. satırına Renault bilgisini ekleriz.
    file.seek(0)
    file.writelines(markalar) # Aşağıdaki gibi for döngüsü ile dizideki verileri dosyaya eklemek yerine writelines() metotu ile kolayca yapabiliriz.

    # for marka in markalar:
    #     file.write(marka) 

with open(r"C:\Users\Harun\Desktop\Python_Temelleri\Dosya Yönetimi I-O\markalar.txt") as file:
    print(file.read())
