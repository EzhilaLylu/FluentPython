class Person:
    def __init__(self, firstname, lastname):
        self.firstname = firstname
        self.lastname = lastname

    @property #blocks method call like fullname(); could access as attribute only.. fullname is read-only. We cannot modify it.. @property automatically defines a getter, but not a setter
    def fullname(self):
        return self.firstname + " " + self.lastname
    
#with getter and setter
class Person:
    def __init__(self, firstname, lastname):
        self.firstname = firstname
        self.lastname = lastname

    @property
    def fullname(self):
        return self.firstname + " " + self.lastname

    @fullname.setter
    def fullname(self, value):
        self.firstname, self.lastname = value.split(" ", 1) #notice the vlaue modified

# Property Patterns
# This property pattern says, “You can read the value of this attribute, but you cannot change it”
class Coupon:
    def __init__(self, amount):
        self._amount = amount
    
    @property
    def amount(self):
        return self._amount
    
# Validation
class Ticket:
    def __init__(self, price):
        self.price = price #uses the setter to initialize the value
    
    @property
    def price(self):
        return self._price
    
    @price.setter
    def price(self, new_price):
        # Only allow non-negative prices.
        if new_price < 0: #assigns value based on condition
            raise ValueError("Nice try")
        self._price = new_price
        

"""
The Factory Patterns
Idea is providing a handy, simplified way to create useful, potentially complex objects
    - Where the object’s type is fixed, but we want to have several different ways to create it. This is called the Simple Factory Pattern
    - Where the factory dynamically chooses one of several different types. This is called the Factory Method Pattern
"""

# Simple Factory Pattern
import re
class Money:
    def __init__(self, dollars, cents):
        self.dollars = dollars
        self.cents = cents
    
    @classmethod
    def from_pennies(cls, total_cents):
        dollars = total_cents // 100
        cents = total_cents % 100
        return cls(dollars, cents)
    
    @classmethod
    def from_string(cls, amount):
        match = re.search(
            r'^\$(?P<dollars>\d+)\.(?P<cents>\d\d)$', amount)
        if match is None:
            raise ValueError(f"Invalid amount: {amount}")
        dollars = int(match.group('dollars'))
        cents = int(match.group('cents'))
        return cls(dollars, cents)
    
m1 = Money.from_pennies(312) #creating Money objects using Classmethods
m2 = Money.from_string('$123.23')


# Dynamic Type: The Factory Method Pattern
"""
The idea is that the factory will create an object, but will choose its type from one of several possibilities, dynamically deciding at runtime based on some criteria
"""
import abc
class ImageReader(metaclass=abc.ABCMeta):
    def __init__(self, path):
        self.path = path
    @abc.abstractmethod
    def read(self):
        pass # Subclass must implement.
    def __repr__(self):
        return f"{self.__class__.__name__}({self.path})"

class GIFReader(ImageReader):
    def read(self):
        # Read a GIF

class JPEGReader(ImageReader):
    def read(self):
        # Read a JPEG

class PNGReader(ImageReader):
    def read(self):
        # Read a PNG


def extension_of(path):
    # returns "png", "gif", "jpg", etc.
    position_of_last_dot = path.rfind('.')
    return path[position_of_last_dot+1:]

def get_image_reader(path):
    image_type = extension_of(path)
    if image_type == 'gif':
        reader_class = GIFReader
    elif image_type == 'jpg':
        reader_class = JPEGReader
    elif image_type == 'png':
        reader_class = PNGReader
    else:
        raise ValueError(f"Unknown extension: {image_type}")
    return reader_class(path)



# The Observer Pattern 
"""
Observes the event of action and informs the observer so it can take action on the event
"""
# pub-sub for mental model

class Publisher:
    def __init__(self):
        self.subscribers = dict()
    
    def register(self, who, callback=None): #with callback argument Publisher is making itself flexible and do not post constraints on consumer to follow the same method name
        if callback is None:
            callback = who.update
        self.subscribers[who] = callback
    
    def dispatch(self, message):
        for callback in self.subscribers.values():
            callback(message)

# This subscriber uses the standard "update"
class SubscriberOne:
    def __init__(self, name):
        self.name = name
    
    def update(self, message):
        print(f'{self.name} got message "{message}"')

# This one wants to use "receive"
class SubscriberTwo:
    def __init__(self, name):
        self.name = name
    
    def receive(self, message):
        print(f'{self.name} got message "{message}"')

"""
The above code monitors single event
"""

#Observer with multiple events

class Publisher:
    def __init__(self, channels):
        # Create an empty subscribers dict
        # for every channel
        self.channels = { channel : dict()
                          for channel in channels }

    def register(self, channel, who, callback=None):
        if callback is None:
            callback = who.update
        subscribers = self.channels[channel]
        subscribers[who] = callback

    def dispatch(self, channel, message):
        subscribers = self.channels[channel]
        for callback in subscribers.values():
            callback(message)

pub = Publisher(['lunch', 'dinner'])

# Three subscribers, of the original type.
bob = Subscriber('Bob')
alice = Subscriber('Alice')
john = Subscriber('John')

# Two args: channel name & subscriber
pub.register("lunch", bob)
pub.register("dinner", alice)
pub.register("lunch", john)
pub.register("dinner", john)

pub.dispatch("lunch", "It's lunchtime!")
pub.dispatch("dinner", "Dinner is served")



#MAgic methods
class Angle:
    def __init__(self, value):
        self.value = value % 360

    def __add__(self, other): #notice it takes one argument other the self.. a + b => a is self and b is other
         return Angle(self.value + other.value)
    

"""
Method	Operation
__add__()  a + b
__sub__()  a - b
__mul__()  a * b
__truediv__()  a / b (floating-point division)
__mod__()  a % b
__pow__()  a ** b
__lshift__()  a << b
__rshift__()  a >> b
__and__()  a & b
__xor__()  a ^ b
__or__()  a | b
__eq__   ==
__lt__()  less than (<)
__le__()  less than or equal (\<=)
__gt__()  greater than (>)
__ge__()  greater than or equal (>=)
"""

>>> repr(Angle(75))
'Angle(75)'
>>> print('{!r}'.format(Angle(30) + Angle(45))) #notice how !r in print invokes repr instead of str
Angle(75)
>>> print(f"{Angle(30) + Angle(45)!r}")
Angle(75)


"""
__gt__() and __lt__() are reflections of each other. What that means is that, in many cases, you only have to define one of them. Suppose you implement __gt__() but not __lt__(), then do this:

>>> a1 = Angle(3)
>>> a2 = Angle(7)
>>> a1 < a2
True
This works thanks to some just-in-time introspection the Python runtime does. The a1 < a2 is translated to a1.__lt__(a2). If Angle.__lt__() is indeed defined, that method is executed, and the expression evaluates to its return value.

a1 < a2 is true if and only if a2 > a1. For this reason, if __lt__() does not exist, but __gt__() does, then Python will rewrite the angle comparison: a1.__lt__(a2) becomes a2.__gt__(a1). This is then evaluated, and the expression a1 < a2 is set to its return value. There are some situations where you will need to define both, for example, if the comparison is based on several member variables.

"""