sayilar = [1, 2, 3, 4, 5]
s = "Hello"

def my_for(iterable, func):
    iterator = iter(iterable)

    while True:
        try:
            sayi = next(iterator)
            func(sayi)
        except StopIteration:
            break
    
    print("*********")

my_for(sayilar, print)
my_for(s, print)


def kare_al(x):
    print(x**2)

my_for(sayilar, kare_al)




class Counter:
    def __init__(self, _start, _stop):
        self.start = _start
        self.stop = _stop

    def __iter__(self):
        return self
    
    def __next__(self):
        if (self.start <= self.stop):
            x = self.start
            self.start += 1
            return x
        else:
            raise StopIteration

for i in Counter(10, 20):
    print(i)

# iterator = iter(Counter(20, 22))

# print(next(iterator))
# print(next(iterator))
# print(next(iterator))

# iterator = iter(Counter(20, 22))

# while True:
#     try:
#         print(next(iterator))
#     except StopIteration:
#         break
