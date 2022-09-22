# List
# Tuple
# Dictionary
# Set

meyveler = {"elma", "kiraz", "kavun", "üzüm"}
sebzeler = {"bezelye", "soğan"}

print(meyveler)

for x in meyveler:
    print(x)

print("elma" in meyveler)

meyveler.add("karpuz")
print(meyveler)

meyveler.update(["vişne", "muz"])
print(meyveler)

print(len(meyveler))

meyveler.remove("karpuz")
print(meyveler)

meyveler.discard("karpuz")
print(meyveler)

print(meyveler.pop())

meyveler.clear()
print(meyveler)

meyveler = {"elma", "kiraz", "kavun", "üzüm"}
sebzeler = {"bezelye", "soğan"}

sonuc = meyveler.union(sebzeler)
print(sonuc)
