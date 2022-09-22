# Global Scope
from hashlib import new
from tkinter import N
from types import new_class


x = "Global X"

def function():
    # Local Scope
    x = "Local X"
    print(x)

function()
print(x)


# Global Scope
x = "Global X"

def function():
    # Local Scope
    # x = "Local X"
    print(x)

function()
print(x)

################

# Global
name = "Çınar"

def changeName(new_name):
    # Local
    name = new_name
    print(name)

new_name = input("Yeni İsminizi Yazınız: ")
changeName(new_name)

print(name)


name = "Global String"

def greeting():
    name = "Çınar"
    
    def hello():
        print(f"Hello, {name}")
    
    hello()

greeting()
print(name)



name = "Global String"

def greeting():
    name = "Çınar"
    
    def hello():
        name = "Ada"
        print(f"Hello, {name}")
    
    hello()

greeting()
print(name)


x = 50

def test(x):
    print(f"x: {x}")

    x = 100
    print(f"changed x to: {x}")

test(x)
print(x)


x = 50

def test():
    global x
    print(f"x: {x}")

    x = 100
    print(f"changed x to: {x}")

test()
print(x)
