""" Decorator Fonksiyon, hazırlamış olduğumuz bir fonksiyondan önce ya da sonra otomatik olarak çalıştırılmasını
istediğiniz bir kod varsa işimize çok yarayacaktır. """

def gunaydin():
    print("Hoş geldiniz.") # Her iki fonksiyonda da tekrarlayan kod satırları.
    print("Günaydın. Benim adım Harun.")
    print("Görüşmek üzere.") # Her iki fonksiyonda da tekrarlayan kod satırları.

def iyigunler():
    print("Hoş geldiniz.") # Her iki fonksiyonda da tekrarlayan kod satırları.
    print("İyi günler. Benim adım Harun.")
    print("Görüşmek üzere.") # Her iki fonksiyonda da tekrarlayan kod satırları.



# Bu tekrarlayan kod satırlarıyla bir fonksiyon oluşturursak aynı kod satırlarını tekrar yazmamıza gerek kalmaz.

def selamlama(fn):
    def wrapper():
        print("Hoş geldiniz.")
        fn()
        print("Görüşmek üzere.")

    return wrapper

# Alttaki iki fonksiyonu bu şekilde yapmak yerine Decorators kullanarak diğerindeki gibi daha kolay bir şekilde de yapabiliriz.

def gunaydin():
    print("Günaydın. Benim adım Harun.")

def iyigunler():
    print("İyi günler. Benim adım Harun.")

g = selamlama(gunaydin)
g()
i = selamlama(iyigunler)
i()

print("*" * 10)
# Bu şekilde yapılabilir.

def selamlama(fn):
    def wrapper(ad):
        print("Hoş geldiniz.")
        fn(ad)
        print("Görüşmek üzere.")

    return wrapper

@selamlama
def gunaydin(ad):
    print(f"Günaydın. Benim adım {ad}.")

@selamlama
def iyigunler(ad):
    print(f"İyi günler. Benim adım {ad}.")

gunaydin("Harun")
iyigunler("Crane")
