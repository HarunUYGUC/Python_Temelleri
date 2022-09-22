sayilar = [1,2,3,6,8,9]

for i in sayilar:
    print(i)

for i in sayilar:
    print("Merhaba!")


isimler = ["Ali","Deniz","Yağmur"]

for isim in isimler:
    print(isim)


ismim = "Sadık Turan"

for a in ismim:
    print(a)


_tuple = [(1,2),(3,4),(5,6)]

for a in _tuple:
    print(a)

for x,y in _tuple:
    print(x,y)


_dict = {"k1":1,"k2":2,"k3":3}

for x in _dict:
    print(x)

for x in _dict:
    print(_dict[x])

for x in _dict.values():
    print(x)

for key,value in _dict.items():
    print(key,value)
