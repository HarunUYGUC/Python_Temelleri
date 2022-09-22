markalar = ["opel","bmw","mercedes"]

index = 1
for marka in markalar:
    print(f"{index}- {marka}")
    index += 1

index = 0
for marka in markalar:
    print(f"{index+1}- {markalar[index]}")
    index += 1


# enumerate

obj1 = enumerate(markalar)

print(type(obj1))
print(list(obj1))


for i in enumerate(markalar):
    print(i)


# zip

liste1 = [1,2,3,4,5]
liste2 = ["a","b","c","d","e"]

print(list(zip(liste1,liste2)))


for item in zip(liste1,liste2):
    print(item)
