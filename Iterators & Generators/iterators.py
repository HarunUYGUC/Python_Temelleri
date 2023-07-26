# iterable?

# iterator?

"""
for döngüsünde kullanmış olduğumuz liste veya string verileri bir iterable nesnesidir.
Çünkü bu sınıfların içerisinde __iter__ adında bir metot vardır. Bu metot liste veya string
verilerindeki karakterleri teker teker for döngüsü sayesinde yazabilmemizi sağlar. Örneğin int
veri tipinde bu metot yoktur ve bu yüzden böyle bir şey yapamayız.

Liste veya string iterable nesnelerinden tek tek elemanlara ulaşabilmek için bu nesneyi bir
iterator nesnesine çeviriyor olabilmemiz gerekmektedir. Bu çevirme işlemini for döngüsü otomatik
olarak yapar.
"""


sayilar = [1, 2, 3, 4, 5]

for i in sayilar:
    print(i)

print("*********")
isim = "Harun"

for i in isim:
    print(i)

# print("*********")
# sayi = 10

# for i in sayi:
#     print(i)  # TypeError: 'int' object is not iterable

print("-----------")

sayilar = [1, 2, 3, 4, 5]

iterator = iter(sayilar)

# print(next(iterator))
# print(next(iterator))
# print(next(iterator))
# print(next(iterator))
# print(next(iterator))

while True:
    try:
        sayi = next(iterator)
        print(sayi)
    except StopIteration:
        break
