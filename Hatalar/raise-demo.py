# 1- Faktöriyel fonksiyonu oluşturup fonksiyona gelen değer için hata mesajları verin.

def faktoriyel(sayi):
    try:
        int(sayi)
    except:
        return "Sayı girmeniz gerekmektedir!"
        
    sayi = int(sayi)
    if (sayi < 0):
        return "Negatif bir sayı olamaz!"
    else:
        fakSonuc = 1
        for i in range(1, sayi + 1):
            fakSonuc *= i
        return fakSonuc


sayi = input("Faktöriyelini bulmak istediğiniz sayıyı giriniz: ")
faktoriyel(sayi)

print(faktoriyel(sayi))

# 2- Girilen parola içinde türkçe karakter hatası veriniz.

def parolaOlusturucu(parola):
    turkceKarakterler = ["ç", "Ç", "ğ", "Ğ", "ı", "İ", "ö", "Ö", "ş", "Ş", "ü", "Ü"]
    for i in parola:
        if i in turkceKarakterler:
            raise ValueError("Parola Türkçe karakter içeremez!")

    print("Parolanız oluştu!")

            
parola = input("Oluşturmak istediğiniz parolayı giriniz: ")

try:
    parolaOlusturucu(parola)
except ValueError as ex:
    print(ex)

