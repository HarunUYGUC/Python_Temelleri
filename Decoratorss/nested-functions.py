def greeting(name):
    print("Hello", name)

# greeting("Ali")
# print(greeting)

sayHello = greeting # Adreslerini aynı yaptık. Yani sayHello değişkeni artık bir greeting fonksiyonu oldu.

print(sayHello)
print(greeting)

greeting("ali")
sayHello("ali")

del sayHello # sayHello fonksiyonunu silsek bile greeting fonksiyonu ve içerisindeki veriler kalmaya devam eder.
print(greeting)



""" Encapsulation """
def outer(num1):
    print("outer")

    def inner_increment(num1):
        print("inner")
        return num1 + 1
    
outer(10) # Dıştaki fonksiyon çalışır fakat içteki fonksiyon çalışmaz.
print("***************")

def outer(num1):
    print("outer")

    def inner_increment(num1):
        print("inner")
        return num1 + 1
    
    num2 = inner_increment(num1) # Dıştaki fonksiyonun içerisinde tanımladığımız içteki fonksiyonu
    print(num1, num2) # dıştaki fonksiyonun scope alanı içerisinde kullanırsak dıştaki fonksiyonu 
# çağırdığımız anda içteki fonksiyonu da çağırmış oluruz.
outer(10)

# inner_increment(10) şeklinde bir kullanımı burada yapamayız çünkü outer fonksiyonunun scope alanı 
# içerisinde olduğu için outer üzerinden kullanılabilir bir fonksiyondur.
 

""" Recursive Functions """
def factorial(number):
    # Girdiğimiz değer bu iki if not filtresini de geçemezse inner fonksiyonuna ulaşamaz.

    if not isinstance(number, int): # isinstance metotu, gönderdiğimiz verinin belirttiğimiz sınıfa ait olup olmadığını kontrol eder.
        raise TypeError("Number must be an integer!")
    
    if not (number >= 0):
        raise ValueError("Number must ve zero or positive!")

    def inner_factorial(number):
       if (number <= 1):
          return 1
       
       return number * inner_factorial(number - 1) # Recursive Functions. Fonksyionun kapsam alanı 
    
    return inner_factorial(number) # içerisinde tekrar aynı fonksiyonu çağırdık. (Özyinelemeli Fonksiyonlar)

try:
    print(factorial(5))
    print(factorial(4))
    print(factorial(1.5))
    print(factorial(-2))
except Exception as ex:
    print(ex)
