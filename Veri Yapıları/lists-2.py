diller = ["Python", "C#", "Java", "Javascript"]

print(diller)
print(type(diller))

print(diller[0])
print(diller[0:2])

diller[0] = "Html"
print(diller)

diller[-1] = "Html"
print(diller)

print(len(diller))

print(diller + ["Angular", "Vuejs"])


diller = ["Python", "C#", "Java", "Javascript"]

if "Python" in diller:
    print("Evet")


for x in diller:
    print(x)


del diller[0]
print(diller)



