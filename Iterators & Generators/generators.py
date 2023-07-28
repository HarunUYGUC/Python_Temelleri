# Generator'u, Iterable Nesne oluşturan bir fonksiyon gibi düşünebiliriz.

def sayi_say(max):
    sayi = 1
    sayilar = []

    while (sayi <= max):
        sayilar.append(sayi)
        sayi += 1

    return sayilar

sonuc = sayi_say(10)
print(sonuc)




def sayi_say(max):
    sayi = 1

    while (sayi <= max):
        yield sayi # yield keyword'u sayesinde oluşturduğumuz sayıyı direkt olarak geriye döndürebiliriz.
        sayi += 1 # Böylece bir Generator Nesnesi oluşturmuş oluruz.

generator = sayi_say(10)
print(generator)
print(next(generator))
print(next(generator))
print(next(generator))

""" Next metotu ile Generator Nesnesi'ndeki verileri teker teker okuruz ve okuduktan sonra bu veriler 
silinir. Bu sayede ilk örnekte yaptığımız gibi bellekte gereksiz bir kullanım yapmamış oluruz. Çünkü 
ilk örnekte bütün verileri bir listede tuttuğumuz için bellekte gereksiz bir kullanım yapmış oluyoruz.  """

generator = sayi_say(10)
iterator = iter(generator) # Böyle yapmak yerine üst satırdaki kodda generator yerine direkt iterator'de
print(iterator) # yazabiliriz. Sonuçta Decorator'da bir Iterator gibi düşünülebilir.
print(next(iterator))
print(next(iterator))
print(next(iterator))

# print(help(generator))

# for i in iterator:
#     print(i)

sonuc = list(iterator)
print(sonuc)

liste = [i for i in range(1, 11)]
print(liste)

generator = (i for i in range(1, 11))
print(generator)
print(next(generator))
print(next(generator))
""" Generator üretmek için illa bir fonksiyon oluşturmamıza gerek yoktur. List Comprehension'ı köşeli değil de
normal parantezlerle kullanırak generator oluşturabiliriz. """
