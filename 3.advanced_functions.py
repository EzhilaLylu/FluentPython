# Accepting and Passing Variable Arguments
def takes_any_args(*args):
    print(type(args)) # args is always tuple


def normal_function(a, b, c):
    print(f"a: {a} b: {b} c: {c}")


# argument unpacking
numbers = (7, 5, 3)
normal_function(*numbers)

#variable keyword arguments
def print_kwargs(**kwargs):
    for key, value in kwargs.items(): # kwargs is always dictionary
        print(f"{key} -> {value}")

# keyword unpacking
numbers = {"a": 7, "b": 5, "c": 3}
normal_function(**numbers)


# Combining Positional and Keyword Arguments
def general_function(*args, **kwargs):
    for arg in args:
        print(arg)
    for key, value in kwargs.items():
        print(f"{key} -> {value}")

"""
There’s one last point to understand, on argument ordering. When you def the function, you specify the arguments in this order:
    - Positional arguments (nonkeyword) arguments
    - The *args nonkeyword variable arguments
    - The **kwargs keyword variable arguments
"""

# Functions as Objects
# In Python, functions are simply objects—just as much as an integer, or a string, or an instance of a class is an object
# The value of key is a function taking one argument—an element in the list—and returning a value for comparison
def max_by_key(items, key):
    biggest = items[0]
    for item in items[1:]:
        if key(item) > key(biggest):
            biggest = item
    return biggest

values = [3, -2, 7, -1, -20]
max_by_key(values, abs)
nums = ["12", "7", "30", "14", "3"]
max_by_key(values, int) # int, abs are functions passed as object. Note that they are int not int()


# Key Functions in Python
# The value of key is a function taking one argument—an element in the list—and returning a value for comparison
max(nums)
max(nums, key=int)
min(values)
min(values, key=abs)
sorted(values)
sorted(values, key=abs)


from operator import itemgetter, attrgetter, methodcaller #examples of key function