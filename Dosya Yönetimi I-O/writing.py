# "w" => (Write) Yazma modu.
#     ** Dosyayı konumda oluşturur.
#     ** Eğer konumda aynı dosya varsa dosyayı siler ve yeni oluşturur.

file = open(r"C:\Users\Harun\Desktop\Python_Temelleri\Dosya Yönetimi I-O\newfile.txt", "w")
print(file) # Oluşturduğumuz dosya hakkındaki bilgileri yazar.
# Terminalde şu şekilde gözükür: <_io.TextIOWrapper name='c:\\Users\\Harun\\Desktop\\Python_Temelleri\\Dosya Yönetimi I-O\\newfile.txt' mode='w' encoding='cp1254'>

# Windows işletim sistemli bilgisayarlarda write modunu kullanarak oluşturduğumuz dosyanın encoding bilgisi
# otomatik olarak encoding='cp1254' şeklinde gelir. Türkçe karakter sorunu yaşamamak için encoding='UTF-8' bilgisini başta belirtmeliyiz.


file = open(r"C:\Users\Harun\Desktop\Python_Temelleri\Dosya Yönetimi I-O\newfile1.1.txt", "w", encoding="UTF-8")
file.write("Harun Uyguç \n") # Üst satırda oluşturduğumuz dosyaya veri girmek istersek bu şekilde yapmalıyız.
file.write("Leon F. Kennedy \n") # \n diyip girdiğimiz verinin altında boş satır oluşturmalıyız. Yoksa gireceğimiz diğer veri aynı satıra yazılır.
file.write("Kyle Crane")
file.close()
print(file)


with open(r"C:\Users\Harun\Desktop\Python_Temelleri\Dosya Yönetimi I-O\newfile1.2.txt", "w", encoding="UTF-8") as file:
    file.write("Harun Uyguç \n")
    file.write("Leon F. Kennedy \n")
    file.write("Kyle Crane \n")
    file.close()
    print(file)


with open(r"C:\Users\Harun\Desktop\Python_Temelleri\Dosya Yönetimi I-O\newfile1.2.txt", encoding="UTF-8") as file:
    print(file.read())
