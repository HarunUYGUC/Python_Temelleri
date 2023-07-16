liste = [1, 2, 3]
print(len(liste))

s = "hello world"
print(len(s))

class Film:
    def __init__(self, _baslik, _yonetmen, _sure):
        self.baslik = _baslik
        self.yonetmen = _yonetmen
        self.sure = _sure

    def __str__(self): # 2 tane alt çizgiye sahip fonksiyonlar (__) sınıfa özel ve dışarıdan çağırılmayan fonksiyonlar anlamına gelir.
        return f"{self.baslik} {self.yonetmen} tarafından yönetildi." # İstersek Property'deki gibi çağırabiliriz ama çağırmamamız gerekiyor.

    def __repr__(self):
        return f"{self.baslik} {self.yonetmen} tarafından yönetildi." # İstersek Property'deki gibi çağırabiliriz ama çağırmamamız gerekiyor.
        
    def __len__(self):
        return self.sure
    
    def __del__(self):
        print("film objesi silindi.")

# f = Film()

# print(type(liste))
# print(type(s))
# print(type(f))

f = Film("film adı", "yonetmen", 120)

print(str(liste))
print(liste)
print(str(f))
print(f)
print(len(f))
del f # Bunu yazmasak bile Obje kullanıldıktan sonra otomatik olarak bellekten silindiğinden dolayı bu mesaj 
# yine de karşımıza çıkacaktır. Çünkü Sınıf içerisinde __del__() metotunu kullandık.  
