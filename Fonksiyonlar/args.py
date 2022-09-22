liste = [10, 20, 30]

def toplam (liste):
    sonuc = 0
    for i in liste:
        sonuc += i
    return sonuc

print(toplam(liste))


# args kullanımı:

def toplam(*args):
    sonuc = 0
    for i in args:
        sonuc += i
    return sonuc

print(toplam(10, 20, 30, 40))

# args aslında arguments kelimesinin kısaltması olarak kullandığımız bir değişken ve 
# bu değişkeni biz kendimiz uydurduk yani bu isim yerine başka bir isim de koyabilirdik.

# args'ın başına * koyarak fazla sayıdaki argümanı args değişkeninin içerisine 
# teker teker eklemiş olduk ve böylece args bir tuple listesine dönüşmüş oldu.
