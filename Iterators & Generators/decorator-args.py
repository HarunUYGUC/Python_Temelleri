def dec_do_twice(count):
    def do_twice(func):
        def wrapper_do_twice(*args, **kwargs):
            for _ in range(count):
                func(*args, **kwargs)
        return wrapper_do_twice
    return do_twice

@dec_do_twice(count=2)
def hello():
    print("Hello")

@dec_do_twice(count=5)
def greet(name):
    print("Hello " + name)

hello()
greet("Ali")



print("*" * 10)

import time

def dec_speed_test(count):
    def speed_test(fn):
        def wrapper(*args, **kwargs):
            print(f"{fn.__name__} metotu çalışıyor...")

            for _ in range(count):
                start_time = time.perf_counter()
                result = fn(*args, **kwargs)
                end_time = time.perf_counter()
                run_time = end_time - start_time
                print(f"Geçen süre: {run_time}")

            return result
        return wrapper
    return speed_test

@dec_speed_test(count=2)
def sum_gen():
    return sum((x for x in range(10000000)))

@dec_speed_test(count=5)
def sum_list():
    return sum([x for x in range(10000000)])

print(sum_gen())
print(sum_list())
