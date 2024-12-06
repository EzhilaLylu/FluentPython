def make_upper(func):
    def inner_func(arg):  # def inner_func(*args, **kwargs):
        return func(arg).upper() # return func(*args, **kwargs).upper()  -- to support compatibility for all the type of functions irrespective of function signature
    return inner_func


@make_upper
def remove_vowel(in_data):
    vowels = list('aeiou')
    print(vowels)
    consonants = [char for char in in_data.lower() if char not in vowels]
    return ''.join(consonants)

print(remove_vowel('Ezhilarasi'))

# <h2>Data in Decorators</h2>
# Decorater function with shared variables
def running_average(func):
    data = {"total" : 0, "count" : 0} #Run once for every decoraters and data got created. Whenever decorated function call happens just the wrapper function getting called not the entire decorator
    def wrapper(*args, **kwargs):
        val = func(*args, **kwargs)
        data["total"] += val
        data["count"] += 1
        print("Average of {} so far: {:.01f}".format(
             func.__name__, data["total"] / data["count"]))
        return func(*args, **kwargs)
    return wrapper

"""
The decorator function itself is executed exactly once for every function it decorates. If you decorate N functions, running_average() is executed N times, so we get N different data dictionaries, each tied to one of the resulting decorated functions. This has nothing to do with how many times a decorated function is executed. The decorated function is, basically, one of the created wrapper() functions. That wrapper() can be executed many times, using the same data dictionary that was in scope when that wrapper() was defined.
"""

#<h2>Accessing Inner Data</h2>
def collectstats(func):
    data = {"total" : 0, "count" : 0}
    def wrapper(*args, **kwargs):
        val = func(*args, **kwargs)
        data["total"] += val
        data["count"] += 1
        return val
    wrapper.data = data #ties the data's current value with the wrapper function
    return wrapper

#decorator to count how many times a function being called
def countcalls(func):
    count = 0
    def wrapper(*args, **kwargs):
        nonlocal count #Notice nonlocal keyword
        count += 1
        print(f"# of calls: {count}")
        return func(*args, **kwargs)
    return wrapper


# Decorators That Take Arguments
def add(increment): #one more nested function when we add arguments to decorators
    def decorator(func):
        def wrapper(*args, **kwargs):
            return func(*args, **kwargs) + increment # increment will vary based on the argument passed
        return wrapper
    return decorator

@add(2) # add is the function that takes argument and return decorator function
def foo(x):
    return x ** 2

@add(4)
def bar(n):
    return n * 2


# Class-Based Decorators
class PrintLog:
    def __init__(self, func): # pass the function as arguments to constructor
        self.func = func
    def __call__(self, *args, **kwargs): # replace wrapper with __call__
        print(f"CALLING: {self.func.__name__}")
        return self.func(*args, **kwargs)
    
@PrintLog
def foo(x):
    print(x + 2)


# class based decorators with nonlocal variables
class CountCalls:
    def __init__(self, func):
        self.func = func
        self.count = 0 #count can be accessed outside decorator function
    def __call__(self, *args, **kwargs):
        self.count += 1
        print(f"# of calls: {self.count}")
        return self.func(*args, **kwargs)

@CountCalls
def foo(x):
    return x + 2

# Class-based version of the "add" decorator above.
class Add:
    def __init__(self, increment): # parameter accepted here
        self.increment = increment
    def __call__(self, func): # accepts function to be decorated
        def wrapper(n): # nested function
            return func(n) + self.increment
        return wrapper
    

# Decorators for Classes

def autorepr(cls): #accepts class
    def cls_repr(self):
        return f"{cls.__name__}()"
    cls.__repr__ = cls_repr # redefines the function implementation
    return cls # returns original class not a wrapper function

@autorepr
class Penny:
    value = 1

penny = Penny()
repr(penny)
'Penny()'