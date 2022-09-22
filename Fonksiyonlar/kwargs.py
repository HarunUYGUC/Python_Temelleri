def displayUser(*args):
    print(type(args))

displayUser()


def displayUser(*args):
    return type(args)

print(displayUser())

# Bu iki kullanım da aynı görevi görür.

def displayUser(*args):
    print(type(args))
    print(args)

displayUser()


def displayUser(**kwargs):
    print(type(kwargs))
    print(kwargs)

displayUser()


def displayUser(**kwargs):
    print(type(kwargs))
    print(kwargs)

displayUser(username="sadikturan", email="info@sadikturan.com")


def displayUser(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}: {value}")

displayUser(username="sadikturan", email="info@sadikturan.com", country="Türkiye")


def myFunc(a, b, c, *args, **kwargs):
    print(a)
    print(b)
    print(c)
    print(args)
    print(kwargs)

myFunc(10, 20, 30, 40, 50, 60, key1 = "value 1", key2 = "value  2")
