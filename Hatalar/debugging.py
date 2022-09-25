import pdb

one = "one"
two = "two"
pdb.set_trace()

sonuc = one + two
print(sonuc)


three = " three "
sonuc += three
print(sonuc)



def add_numbers(a, b, c):
    import pdb; pdb.set_trace()
    return (a + b + c)

add_numbers(1, 2, 3)
