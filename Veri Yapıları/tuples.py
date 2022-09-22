_list = [1, 2, 3]
_tuple = (1, 2, 3)
_tuple2 = (4, 5, 6)

print(type(_list))
print(type(_tuple))

print(_list[1])
print(_tuple[1])

print(len(_list))
print(len(_tuple))

_list[0] = 5
"""
_tuple[0] = 5 # Böyle bir şey yapılamaz çünkü Tuple'daki bilgiler değiştirilemez.
"""

"""
_list.append(3)
_tuple.append(3) # Böyle bir şey yapılamaz çünkü Tuple'daki bilgiler değiştirilemez.
"""

print(_tuple.count(2))


print(_tuple + _tuple2)

_t = tuple([1, 2, 3])
print(type(_t))
