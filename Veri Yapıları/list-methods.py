sayilar = [1, 5, 8, 9, 3, 45]
harfler = ["a", "b", "e", "s", "a", "y"]

print(min(sayilar))
print(max(sayilar))
print(min(harfler))
print(max(harfler))

harfler2 = ["abc", "acb"]
print(min(harfler2))
print(max(harfler2))

""""
print(sayilar.append(10)) # Hatalı
"""

sayilar.append(10)
print(sayilar)

sayilar.insert(3, 5)
print(sayilar)

"""
print(sayilar.insert(3, 5)) # Hatalı
"""

sayilar.insert(-1, 50)
print(sayilar)

sayilar.insert(len(sayilar), 150)
print(sayilar)

sayilar.pop()
print(sayilar)

sayilar.pop(0)
print(sayilar)

sayilar.remove(5)
print(sayilar)

harfler.remove("a")
print(harfler)

"""
print(sayilar.sort()) #Hatalı
"""

sayilar.sort()
print(sayilar)

harfler.sort()
print(harfler)

sayilar.reverse()
print(sayilar)

print(sayilar.count(5))

print(sayilar.index(5))

sayilar.clear()
print(sayilar)
