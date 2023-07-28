# (1 - ∞) aralığında her sayının karesini getiren fonksiyon.
# Fibonacci serisini hem normal fonksyion hem de Generator fonksiyon ile oluşturun.
# Performans testlerini yapın.


# (1 - ∞) aralığında her sayının karesini getiren fonksiyon.

def sonsuz_sayi_uret():
    sayi = 0
    
    while True:
        yield sayi
        sayi += 1

print(sonsuz_sayi_uret())

generator = sonsuz_sayi_uret()
print(next(generator))
print(next(generator))
print(next(generator))

for i in generator:
    print(i)


# Fibonacci serisini hem normal fonksyion hem de Generator fonksiyon ile oluşturun.

def fib_list(max):
    sayilar = []
    a, b = 0, 1
    
    while (len(sayilar) < max):
        sayilar.append(b)
        a, b = b, a + b

    return sayilar

print(fib_list(10))


def fib_gen(max):
    a, b = 0, 1
    count = 0

    while (count < max):
        a, b = b, a + b
        yield b
        count += 1

for i in fib_gen(10):
    print(i)


# Performans testlerini yapın.

import sys # Bellekte kaplanan alanların karşılaştırılması.

list = [i**2 for i in range(10000)]
print(sys.getsizeof(list))

gen = (i**2 for i in range(10000))
print(sys.getsizeof(gen))


import time # İşlem hızlarının karşılaştırılması.

list_start_time = time.time()
sum([i**2 for i in range(5000000)])
list_elapsed_time = time.time() - list_start_time

gen_start_time = time.time()
sum((i**2 for i in range(50000000)))
gen_elapsed_time = time.time() - gen_start_time

print(list_elapsed_time)
print(gen_elapsed_time)
