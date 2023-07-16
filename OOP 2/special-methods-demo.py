class NewDict(dict):
    def __repr__(self):
        print("__repr__() metotundan mesaj var.")
        return super().__repr__()
    
    def __missing__(self, key):
        print("Olmayan key bilgisini istiyorsunuz.")

    def __getitem__(self, key):
        print("Bir elemanı çağırıyorsunuz.")
        return super().__getitem__(key)

    def __setitem__(self, key, value):
        print("Listeye eleman ekliyorsunuz.")
        super().__setitem__(key, value)

    def __contains__(self, item):
        print("Listede eleman arayamazsınız.")
        # return False
        return super().__contains__(item)

data2 = NewDict()
print(data2)
 

data = NewDict({"first:":"Harun", "last":"Uyguç"})

print(data)
# print(data["first"])
data["first"]
data["age"]

data["first"] = "Esra"
print(data)

print("a" in data)
print("first" in data)
