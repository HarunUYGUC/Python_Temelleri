import numpy as np

# Python List
py_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]

# Numpy Array
np_array = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9])

print(type(py_list))
print(type(np_array))

py_multi = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
np_multi = np_array.reshape(3 ,3) 
# py_multi de yapmak istediğimizi np_multi de bu şekilde kolaylıkla yapabiliriz.

print(py_multi)
print(np_multi)

print(np_array.ndim) # 1 Boyutlu Dizi olduğu için cevap 1.
print(np_multi.ndim) # 2 Boyutlu Dizi olduğu için cevap 2.

print(np_array.shape) # (9,) şeklinde bir dizi.
print(np_multi.shape) # (3, 3) şeklinde bir dizi.
