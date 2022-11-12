import math

value = dir(math)
print(value)

value = help(math)
print(value)

value = help(math.factorial)
print(value)

# Kare Kök Alma
value = math.sqrt(49)
print(value)

# Faktöriyelini Bulma
value = math.factorial(5)
print(value)

# Küçük Tam Sayıya Yuvarlama
value = math.floor(5.9)
print(value)

# Büyük Tam Sayıya Yuvarlama
value = math.ceil(5.9)
print(value)

# Yöntem 1
import math

value = math.factorial(5)
print(value)

# Yöntem 2
import math as islem

value = islem.factorial(5)
print(value)

# Yöntem 3
from math import *

value = factorial(5)
print(value)

# Yöntem 4
from math import factorial

value = factorial(5)
print(value)

# Devam...
from math import factorial,sqrt

value = factorial(5)
print(value)

value = sqrt(9)
print(value)
