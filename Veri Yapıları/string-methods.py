msg = "Python kursumuza hoş geldiniz. Ben Sadık Turan"

print(msg.upper())
print(msg.lower())
print(msg.title())
print(msg.capitalize())

print(msg.islower())
print(msg.isupper())
print("abc".islower())

print("    abc ".strip())

print(msg.split())
print(msg.split()[0])
print(msg.split("."))

sonuc = msg.split()
print("-".join(sonuc))

# print(sonuc.join("-")) Yanlış bir yöntem.
print("Hello World")

print(msg.index("hoş"))

print(msg.startswith("P"))
print(msg.endswith("A"))

print(msg.replace("Sadık", "Çınar"))
print(msg.replace(" ", "-").replace("ş", "s").replace(".", " "))
print(msg.lower( ).replace(" ", "-").replace("ş", "s").replace(".", " "))
