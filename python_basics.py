"""
A closure is a function that remembers values from its enclosing scope,
even after that scope has finished executing.
"""

def make_increment():
    count = 0
    
    def increment():
        nonlocal count
        count += 1
        print(f"{count=}")
    return increment

inc = make_increment()
inc()
inc()

print("=== Inspecting Closures ===")
print(f"Function name: {inc.__name__}")
print(f"Closure variables: {inc.__closure__}")
print(f"Closure cell contents: {inc.__closure__[0].cell_contents}")


### decorators ###

from functools import wraps

def simple_decorator(func):
    @wraps(func) # preserver func name and docstrings
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        return result
    return wrapper


@simple_decorator
def greet(name):
    """Greets a person by name."""
    return f"Hi, {name}!"

print(greet("ac"))


# another level of nested def func for params
def simple_decorator2(param1, param2="param2"):
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            print(param1, param2)
            result = func(*args, **kwargs)
            return result
        return wrapper
    return decorator


@simple_decorator2(param1="param1")
def greet2(name):
    """Greets a person by name."""
    return f"Hi, {name}!"

print(greet2("ac2"))