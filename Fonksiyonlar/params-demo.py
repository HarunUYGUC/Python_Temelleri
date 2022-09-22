# Kendisine gönderilen 2 sayıdan hangisi büyük bulan fonksiyonu yazınız.

def buyukluk(a, b):
    if (a > b):
        print(f"Büyük olan sayı {a}'dır.")
    elif (b > a):
        print(f"Büyük olan sayı {b}'dır.")
    else:
        print(f"{a}, {b}'ye eşittir.")

a = float(input("Karşılaştırmak istediğiniz 1. sayıyı yazınız: "))
b = float(input("Karşılaştırmak istediğiniz 2. sayıyı yazınız: "))
buyukluk(a, b)


# Kendisine gönderilen bir string bilgi içinde her karakter kaçar kez tekrarlanmış bulunuz.

def kacKez(msg):
    for letter in msg:
        number = msg.count(letter)
        dctonry = dict()
        dctonry[letter] = number
        print(dctonry)

msg = input("Girmek istediğiniz mesajı yazınız: ")
kacKez(msg)



def kacKezVar(string):
    return {kelime: string.count(kelime) for kelime in string}

string = input("Girmek istediğiniz mesajı yazınız: ")
kacKezVar(string)

print(kacKezVar(string))


# Kendisine gönderilen list, command, position ve value bilgilerine göre liste üzerinde güncelleme yap.
    # [1, 2, 3], ("add, remove"), ("beginning | end"), value
    # list_operation([1, 2, 3], "add", "end", "4") => [1, 2, 3, 4]
    # list_operation([1, 2, 3], "remove", "beginning") => [2, 3]

def update_list(list, command, position, value=None):
    if (command == "remove" and position == "end"):
        return list.pop()
    elif (command == "remove" and position == "beginning"):
        list.pop(0)
        return list
    elif (command == "add" and position == "end"):
        list.append(value)
        return list
    elif (command == "add" and position == "beginning"):
        list.insert(0, value)
        return list

list = [1,2,3]
position = input("Listenin neresinde işlem yapmak istersiniz? (end, beginning): ")
command = input("Listeden bilgi ekleme mi çıkarma mı yapmak istersiniz? (add, remove): ")

if (command == "add"):
    value = int(input("Sayınızı giriniz: "))
else:
    value = ""

update_list(list, command, position, value)

print(update_list(list, command, position, value))


# Kendisine gönderilen renk isimlerinden içinde "blue" rengi varsa True döndüren fonksiyonu yazınız.

def varMiYokMu(kacRenk):
    renkler = []
    
    i = 1
    while (i <= kacRenk):
        renk = input(f"{i}. rengi giriniz: ")
        renkler.append(renk)
        i += 1
    
    if ("blue" in renkler):
        print("Blue rengi listede vardır.")
    else:
        print("Blue rengi listede yoktur.")
        

kacRenk = int(input("Kaç tane renk yazmak istersin?: "))
varMiYokMu(kacRenk)


