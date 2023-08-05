def do_twice(func):
    def wrapper_do_twice(*args, **kwargs):
        func(*args, **kwargs)
        func(*args, **kwargs)
    
    return wrapper_do_twice

@do_twice
def hello():
    print("Hello")

@do_twice
def greet(msg):
    print(f"Hello {msg}")

def return_greeting(name):
    print("Greeting Function")
    return f"Hello, {name}"

hello()
greet("Word")
return_greeting("Leon S. Kennedy")
print(return_greeting("Leon S. Kennedy"))


print("*" * 10)

def do_twice(func):
    def wrapper_do_twice(*args, **kwargs):
        return func(*args, **kwargs)
    
    return wrapper_do_twice

@do_twice
def return_greeting(name):
    print("Greeting Function")
    return f"Hello, {name}"

print(return_greeting("Leon S. Kennedy"))
