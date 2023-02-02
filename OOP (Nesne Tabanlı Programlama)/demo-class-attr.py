class Pet:
    cinsler = ["Kedi", "Köpek", "Kuş"]

    def __init__(self, _isim, _cins):
        if _cins not in Pet.cinsler:
            raise ValueError(f"{_cins} bir evcil hayvan değildir!")

        self.isim = _isim
        self.cins = _cins
    
boncuk = Pet("Boncuk", "Kedi")
pasa = Pet("Paşa", "Köpek")
mavis = Pet("Maviş", "Kuş")

print(boncuk)
print(pasa)
print(pasa)

Pet.cinsler.append("Balık") # Class seviyesinde bir değişiklik yaptığımız için bu değişiklik
boncuk.cinsler.append("Hamster") # her yerde değişmiş olacaktır.
# boncuk, pasa, mavis değişkenleri class seviyesinde olduğu için çünkü bunlar bir nesne ve nesneler 
# class'ın bir kopyasıdır yani bunlar üzerinden de Pet class'ında kullandığımız gibi özellikleri kullanabiliriz.

print(Pet.cinsler)
print(boncuk.cinsler)
print(pasa.cinsler)
