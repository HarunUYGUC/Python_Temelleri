opelObj = {
    "Marka": "Opel",
    "Model": "Corsa",
    "Yıl": 2020
}

print(opelObj)

print(opelObj["Marka"])

print(opelObj.get("Marka"))


for x in opelObj:
    print(x)


for x in opelObj:
    print(opelObj[x])


for x in opelObj.values():
    print(x)

for x,y in opelObj.items():
    print(x,y)

"""
# Kendim bir şey denedim.
for x in opelObj.items():
    print(x)
"""

print("Marka" in opelObj)

print(len(opelObj))

opelObj["Renk"] = "Kırmızı"
print(opelObj)

opelObj.pop("Renk")
print(opelObj)

opelObj.popitem()
print(opelObj)

del opelObj["Marka"]
print(opelObj)

del opelObj
# print(opelObj)


opelObj = {
    "Marka": "Opel",
    "Model": "Corsa",
    "Yıl": 2020
}

opelObj.clear()
print(opelObj)



opelObj = {
    "Marka": "Opel",
    "Model": "Corsa",
    "Yıl": 2020
}

obj = opelObj

obj["Marka"] = "Mazda"

print(obj)
print(opelObj)




opelObj = {
    "Marka": "Opel",
    "Model": "Corsa",
    "Yıl": 2020
}

obj = opelObj.copy()

obj["Marka"] = "Mazda"

print(obj)
print(opelObj)


opelObj.update({
    "Marka": "BMW",
    "Renk": "Kırmızı"
})

print(opelObj)
