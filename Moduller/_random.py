import random

# result = dir(random)
# print(result)

# result = help(random)
# print(result)

### 0-1 arasından rastgele bir sayı üret.
result = random.random()
print(result)

# 0-1 arasından rastgele bir sayı üret ve direkt o sayı üzerinden işlem yap.
result = random.random() * 100
print(result)

### Belirtilen aralıkta rastgele bir sayı üret.
result = random.uniform(1, 10)
print(result)

# Belirtilen aralıkta rastgele bir tam sayı üret.
result = int(random.uniform(1, 10))
print(result)

### Belirtilen aralıkta rastgele bir tam sayı üret.
result = random.randint(1, 10)
print(result)

# Listeden rastgele bir bilgi seç.
names = ["ali", "yağmur", "deniz", "cenk", "ahmet", "efe"]

result = names[random.randint(0, len(names)-1)]
print(result)

### Listeden rastgele bir bilgi seç.
names = ["ali", "yağmur", "deniz", "cenk", "ahmet", "efe"]

result = random.choice(names)
print(result)

### Devam...
greeting = "hello there"

result = random.choice(greeting)
print(result)

### Listedeki elemanların yerlerini karıştır.
liste = list(range(10))
random.shuffle(liste)
print(liste)

### Belirtilen listeden istenen sayıda eleman seç.
liste = list(range(100))

result = random.sample(liste, 3)
print(result)
