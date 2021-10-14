# Python

[Source](https://codewithmosh.com/courses/417695)   

> **IMPORTANT TERMINOLOGY**
> DRY - Don't Repeat Yourself.
> Duck Typing - dynamically typed language definition (if it walks like a duck and quacks like a duck, it is a duck.).
> WEGI - Web Server Gate Interface.


> **FURTHER READING**
> [Selenium and Python](https://selenium-python.readthedocs.io/)
> [Pipenv: A Guide to the New Python Packaging Tool](https://realpython.com/pipenv-guide/)


> **REFERENCES**
> [Pipenv: Python Dev Workflow for Humans](https://pipenv.pypa.io/en/latest/)
> [Pipenv for Easer Virtual Environments](https://mattgosden.medium.com/pipenv-for-easier-virtual-environments-69e1e520cde8)


## Getting Started

Python - high-level cross-platform dynamic language.  


### VS Code extensions

* Python - Linting (pylint), Debugging, Formatting (autopep8).
* Code Runner - Runs code in terminal (Ctrl + Alt + N).


### Interpretation

* CPython (C, default): Python program - CPython - Python Bytecode - Python Virtual Machine - Machine Code.
* IronPython (C#): Python program (with C# code) - IronPython - C# Bytecode - C# Virtual Machine - Machine Code.


## Primitive Types

```py
# Numbers:
# int
count = 1000

# float
rating = 4.99

# complex
x = 1 + 2j


# bool
published = True


# string
greeting = "Hello, world!"
```


### Strings

```py
greeting = "   hello, world!"

print(greeting.title())
# Output:    Hello, World!

print(greeting.strip())
# Output: hello, world!

print(greeting[10:-1])
# Output: world

print(f"{greeting.strip().title()} " + "What's up?")
# Output: Hello, World! What's up?

print("It's me!")
# Output: It's me!

print('It\'s me!')
# Output: It's me!

print("\" \' \\ \n")
# Output:
# " ' \ 
#

print("Hello, world!".replace('Hello', 'Hi'))
# Output: Hi, world!

print(greeting.find('hello'))
# Output: True

print('hello' in greeting)
# Output: True

print('bye' not in greeting)
# Output: True

print('*' * 10)
# Output: **********
```


### Numbers

```py
dec = 10

# There is no operator ++, like dec++.
print(dec += 3)
# Output: 13

# Float.
print(dec / 3)
# Output: 3.3333333333333335

# Integer.
print(dec // 3)
# Output: 3

# Reminder.
print(dec % 3)
# Output: 1 (reminder)

# Power.
print(dec ** 3)
# Output: 1000

# Round with math rules.
print(round(3.1415, 3))
# Output: 3.142
```

```py
import math

# Round to closest int >= 3.1415.
print(math.ceil(3.1415))
# Output: 4
```


### Falsy values

* `''`
* `""`
* `0`
* `None`
* `[]`


## Control Flow


### If

```py
age = 22
regular_customer = False

# Short-curcuit condition evaluation.
if 18 <= age and age < 65 or regular_customer:
    print('eligible')
elif age < 18:
    print('too young')
else:
    print('too old')
# Output: eligible
```


### Ternary operator

```py
age = 22
regular_customer = False

print('eligible' if 18 <= age < 65 or regular_customer else 'not eligible')
# Output: eligible
```

> **NOTES**
> - `18 <= age < 65` - chaining comparison.


### For

```py
for number in range(1, 10, 2):
    print(number * '.')
# Output:
# .
# ...
# .....
# .......
# .........
```


### For else

```py
for char in "Hello":
    if (char == '!'):
        break
    print(char)
else:
    print('!')
    print('!')
# Output:
# 'H'
# 'e'
# 'l'
# 'l'
# 'o'
# '!'
# '!'
```


### While

```py
num = 100
while num > 0:
    print(num)
    num //= 2
# Output:
# 100
# 50
# 25
# 12
# 6
# 3
# 1
```


## Functions

```py
def get_greeting(first_name, last_name="Doe", number=1):
    return f"{number}. Hello, {first_name} {last_name}!"


print(get_greeting("John", "Smith", number=5))
# Output: 5. Hello, John Smith!
```

> **NOTES**
> - `first_name` and `last_name` are parameters, `"John"` and `"Smith"` are arguments.
> - All functions return `None` value by default.


### Tuple packing parameters

```py
# Numbers is a tuple = (2, 3, 4, 5).
def multiply(*numbers):
    total = 1
    for number in numbers:
        total *= number
    return total


print(multiply(2, 3, 4, 5))
# Output: 120
```

### Dictionary packing parameters

```py
# User is a dictionary - [ key1: value1, ..., keyN: valueN ].
def save_user(**user):
    print(user['name'])


save_user(id=1,
          name="John",
          age=22)
# Output: John
```


### Scope

```py
# Global scope variable.
message = "a"


def func1():
    # New local scope variable.
    message = "b"


def func2():
    # Access to global scope variable.
    global message
    message = "c"


func1()
print(message)
# Output: a
func2()
print(message)
# Output: c
```


## Data Structures


### Lists

```py
letters = ['a', 'b', 'c']

matrix = [[0, 1], [2, 4]]

zeros = [0] * 5
# [0, 0, 0, 0, 0]

combined = zeros + letters
# [0, 0, 0, 0, 0, 'a', 'b', 'c']

numbers = list(range(10))
# [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

chars = list("Hello!")
# ['H', 'e', 'l', 'l', 'o', '!']


letters[0] = 'A'
# ['A', 'b', 'c']

len(list(range(1, 5)))
# 4


print(letters[0])
# Output: a

print(letters[-1])
# Output: c

print(letters[0:1])
# Output: ['a']

print(list(range(20))[3:7:2])
# Output: [3, 5]

print(list(range(10))[::-2])
# Output: [9, 7, 5, 3, 1]
```


### List Unpacking

```py
numbers = list(range(10))


# List unpacking and packing to another list.
first, second, *other, last = numbers

print(first, second, other, last)
# Output: 0 1 [2, 3, 4, 5, 6, 7, 8] 9
```


### Iterating over List

```py
letters = ['a', 'b', 'c']


# Iterating through values.
for letter in letters:
    print(letter)
# Output:
# a
# b
# c

# Iterating through index-value tuples.
for letter in enumerate(letters):
    print(letter)
# Output:
# (0, 'a')
# (1, 'b')
# (2, 'c')

# Unpacking index-value tuples.
for index, letter in enumerate(letters):
    print(index, letter)
# Output:
# 0 a
# 1 b
# 2 c
```


### Adding or Removing Items

```py
letters = ['a', 'b', 'b', 'b', 'c']


letters.append('d')
# Output: ['a', 'b', 'b', 'b', 'c', 'd']

letters.insert(0, '-')
# Output: ['-', 'a', 'b', 'b', 'b', 'c', 'd']


letters.pop()
# Output: ['-', 'a', 'b', 'b', 'b', 'c']

letters.pop(1)
# Output: ['-', 'b', 'b', 'b', 'c']


letters.remove('c')
# Output: ['-', 'b', 'b', 'b']

del letters[0]
# Output: ['b', 'b', 'b']

del letters[1:3]
# Output: ['b']

letters.clear()
# Output: []
```


### Finding Items

```py
letters = ['a', 'b', 'c', 'a']


# Error
print(letters.index('d'))
# Output: ValueError: 'd' is not in list

# Needs check before get index if value is missing in the list.
if 'd' in letters:
    print(letters.index('d'))

# Another way to check.
print(letters.count('d'))
# Output: 0

print(letters.count('a'))
# Output: 2
```


### Sorting Lists

```py
numbers = [3, 51, 2, 8, 6]


numbers.sort()
print(numbers)
# Output: [2, 3, 6, 8, 51]

numbers.sort(reverse=True)
print(numbers)
# Output: [51, 8, 6, 3, 2]

# Without changing initial list.
print(sorted(numbers))
# Output: [2, 3, 6, 8, 51]

print(sorted(numbers, reverse=True))
# Output: [51, 8, 6, 3, 2]
```


### Sorting Complex Items

```py
items = [
    ('Product1', 10),
    ('Product2', 9),
    ('Product3', 12)
]


def sort_item(item):
    return item[1]


items.sort(key=sort_item)

print(items)
# Output: [('Product2', 9), ('Product1', 10), ('Product3', 12)]
```


### Lambda Functions, Map, Filter, Zip Functions and List Comprehension

```py
items = [
    ('Product1', 10),
    ('Product2', 9),
    ('Product3', 12)
]


def sort_item(item):
    return item[1]


items.sort(key=sort_item)
print(items)
# Output: [('Product2', 9), ('Product1', 10), ('Product3', 12)]

# The same result can be achived with Lambda functions.
items.sort(key=lambda item: item[1])
print(items)
# Output: [('Product2', 9), ('Product1', 10), ('Product3', 12)]


# Map function.
prices = list(map(lambda item: item[1], items))
print(prices)
# Output: [10, 9, 12]

# The same result can be achived with list comprehension.
prices = [item[1] for item in items]
print(prices)
# Output: [10, 9, 12]


# Filter function.
filtered = list(filter(lambda item: item[1] >= 10, items))
print(filtered)
# Output: [('Product1', 10), ('Product3', 12)]

# The same result can also be achived with list comprehension.
filtered = [item for item in items if item[1] >= 10]
print(filtered)
# Output: [('Product1', 10), ('Product3', 12)]


# Zip function.
print(list(zip(items, "Hello", range(10), items)))
# Output:
# [(('Product1', 10), 'H', 0, ('Product1', 10)),
#     (('Product2', 9), 'e', 1, ('Product2', 9)),
#     (('Product3', 12), 'l', 2, ('Product3', 12))]
```


### Stack and Queue

Stack - **LIFO** - **L**ast **I**n - **F**irst **O**ut
Use simple array `[1, 2, 3]`. Methods: `append(4)`, `pop()`. Top of the stack: `[-1]`.

Queue - **FIFO** - **F**irst **I**n - **F**irst **O**ut
Use class: `deque([1, 2, 3])`, Methods: `append(4)`, `popleft()`.


### Tuple

Tuples is a read only list, no methods to append, modify or remove items. *Immutable* type.

```py
point1 = (1, 2)
print(type(point1), point1)
# Output: <class 'tuple'> (1, 2)

point2 = 1, 2
print(type(point2), point2)
# Output: <class 'tuple'> (1, 2)

point3 = 1,
print(type(point3), point3)
# Output: <class 'tuple'> (1,)

point4 = 1, None
print(type(point4), point4)
# Output: <class 'tuple'> (1, None)

point5 = ()
print(type(point5), point5)
# Output: <class 'tuple'> ()

point6 = (1, 2) + (3, 4)
print(point6)
# Output: (1, 2, 3, 4)

point7 = (1, 2) * 3
print(point7)
# Output: (1, 2, 1, 2, 1, 2)

point8 = tuple([1, 2])
print(point8)
# Output: (1, 2)

point9 = tuple("Hello, world!")
print(point9)
# Output: ('H', 'e', 'l', 'l', 'o', ',', ' ', 'w', 'o', 'r', 'l', 'd', '!')

point10 = (1, 2, 3, 4, 5, 6)
print(point10[1:-1:2])
a, b, c, d, e, f = point10
if 10 in point10:
    print("Exists")
# Output: (2, 4)


# Swapping two variables with unpacking tuple.
x = 10
y = 11

x, y = y, x
# It is the same as:
p = (y, x)
x, y = p

print(x, y)
# Output: 10 11
```


### Array

Array performs faster than ordinary list on large ammount of items.
Use class `array("i", [1, 2, 3])`. Methods: `append(4)`, `insert(5, 3)`, `pop()`, `remove(2)`


### Set

Set is a collection of items with no duplicates.

```py
numbers = [1, 1, 2, 3, 4]
first = set(numbers)
second = {1, 5}


# Supports the same operation that lists do except for indexing.
second.add(6)
second.remove(6)
len(second)
if 1 in second:
    print("Yes")


# Also supports specific operations.
# Union.
print(first | second)
# Output: {1, 2, 3, 4, 5}

# Intersection.
print(first & second)
# Outputs: {1}

# Difference (items from the first set, which doesn't exist in the second set).
print(first - second)
# Output: {2, 3, 4}

# Semantic difference (items from first or second sets but not both).
print(first ^ second)
# Output: {2, 3, 4, 5}

# Set comprehension
print({x * 2 for x in range(5)})
# Output: {0, 2, 4, 6, 8}
```


### Dictionary

Dictionary is a collection of key value pairs.

```py
point = {'x': 1, 'y': 2}

# The same definition.
point = dict(x=1, y=2)

# Supports indexing.
point['x'] = 10
point['z'] = 20
if 'a' in point:
    print(point['a'])

# Have special indexing operation with default value.
print(point.get('a', 0))

# Supports del operatior.
del point['x']
print(point)


# Iterating over dictionary.
for key in point:
    print(key)
# Output:
# y
# z

for pair in point.items():
    print(pair)
# Output:
# ('y', 2)
# ('z', 20)

for key, value in point.items():
    print(key, value)
# Output:
# y 2
# z 20


# Dictionary comprehension
values = {x: x * 2 for x in range(5)}
print(values)
# Output: {0: 0, 1: 2, 2: 4, 3: 6, 4: 8}
```


### Generator object

Generator object doesn't store items in the memory, it generats them when it's necessary.

```py
from sys import getsizeof

values = (x * 2 for x in range(1000))
print("Generator object:", getsizeof(values), "bytes")
# Output: Generator object: 56 bytes

values = (x * 2 for x in range(100000))
print("Generator object:", getsizeof(values), "bytes")
# Output: Generator object: 56 bytes

values = [x * 2 for x in range(1000)]
print("List:", getsizeof(values), "bytes")
# Output: List: 4508 bytes

values = [x * 2 for x in range(100000)]
print("List:", getsizeof(values), "bytes")
# Output: List: 412228 bytes
```


### Unpacking operator

```py
numbers = [1, 2, 3]

# The same as ... in JavaScript.
print(*numbers)
# Output: 1 2 3

print(list(range(5)))
# Output: [0, 1, 2, 3, 4]

# Unpacking lists and other iterables with single *.
print([*range(5)])
# Output: [0, 1, 2, 3, 4]

print([*range(5), *"Hello"])
# Output: [0, 1, 2, 3, 4, 'H', 'e', 'l', 'l', 'o']

print({*range(5), *"Hello"})
# Output: {0, 1, 2, 3, 4, 'l', 'H', 'e', 'o'}

first = [1, 2]
second = [3]
print([*first, 'a', *second, *"Hi"])
# Output: [1, 2, 'a', 3, 'H', 'i']

# Unpacking dictionaries with double *.
first = {'x': 1}
second = {'x': 10, 'y': 2}
print({**first, **second, 'z': 3})
# Output: {'x': 10, 'y': 2, 'z': 3}
```


## Exceptions

```py
def calculate_xfactor(age):
    if age <= 0:
        # Throws exception.
        raise ValueError("Age can not be 0 or less.")
    return 10 / age


# Defines code block with exception handling.
try:
    file = open("app.py")
    age = int(input("Age: "))
    calculate_xfactor(age)
# Catches exceptions.
except (ValueError, ZeroDivisionError) as ex:
    print(type(ex))
    print(ex)
    print("You didn't enter a valid age.")
# Catches other exceptions.
except FileNotFoundError:
    print("File can not be found.")
# Works when no exceptions were thrown.
else:
    print("No exceptions were thrown")
# Works either any exceptions where thrown or not.
finally:
    file.close()


try:
    # The with statement is used to automatically release external resources,
    # either any exceptions where thrown or not. So we don't need finally
    # statement in this case.
    # This can be done when class supports Context Management Protocol
    # or (wich is the same) it has two methods: __enter__ and __exit__.
    with open("source.txt") as source, open("target.txt") as target:
        print("Files opened.")
except FileNotFoundError:
    print("Files can not be found.")
```

```py
from timeit import timeit


codeWithException = """
def calculate_xfactor(age):
    if age <= 0:
        raise ValueError("Age can not be 0 or less.")
    return 10 / age


try:
    calculate_xfactor(-1)
except ValueError as error:
    pass
"""


codeWithoutException = """
def calculate_xfactor(age):
    if age <= 0:
        return None
    return 10 / age


xfactor = calculate_xfactor(-1)
if xfactor == None:
    pass
"""


# Raising exceptions has its cost, so it should be done when it is really necessary.
print("Code with exception raising: ", timeit(codeWithException, number=10000))
print("Code without exception:      ", timeit(
    codeWithoutException, number=10000))
# Output:
# Code with exception raising:  0.014636099999999999
# Code without exception:       0.0062339999999999895
```

> **NOTES**
> - `pass` is a statement wich doesn't do anything and is used when we can't have an empty code block.


## Classes

```py
# Pascal naming convensions.
class Point:
    # Class attribute.
    default_color = "red"

    # In every method must be at least one parameter - self.
    def draw(self):
        # x, y - instance attributes.
        print(f"Point ({self.x}, {self.y})")

    # Constructor. And one of the Magic Methods in Python class.
    def __init__(self, x, y):
        self.x = x
        self.y = y

    # Class method.
    @classmethod
    def zero(cls):
        return cls(0, 0)

    # Magic Method is method with double underscore at the begining and end of
    # the name and wich is called automatically by Python interpreter
    # depending on how we use our objects or classes.
    def __str__(self):
        return f"({self.x}, {self.y})"

    # Equal.
    def __eq__(self, other):
        return self.x == other.x and self.y == other.y

    # Greater Than.
    # Python interpreter will use it for Less Than.
    def __gt__(self, other):
        return self.x > other.x and self.y > other.y

    # Addition.
    def __add__(self, other):
        return Point(self.x + other.x, self.y + other.y)


point = Point(1, 2)
print(type(point))
# Output: <class '__main__.Point'>
# NOTE: __main__ is a name of the module, where class Point is defined.

print(isinstance(point, Point))
# Output: True

# Objects in Python are dynamic. Similar to JavaScript.
# So we can define attributes whenever we need them.
point.z = 10

point.draw()
# Output: Point (1, 2)

print(Point.default_color)
print(point.default_color)
Point.default_color = "yellow"
print(Point.default_color)
print(point.default_color)
# Output:
# red
# red
# yellow
# yellow

# Factory method - creates new object. Demonstration of class methods.
point = Point.zero()
point.draw()
# Output: Point (0, 0)

print(point)
# Output: (0, 0)

print(point == Point(0, 0))
print(point > Point(1, 1))
print(point < Point(1, 1))
print(Point(2, 3) + Point(1, 1))
# Output:
# True
# False
# True
# (3, 4)
```

> **NOTES**
> - [A Guide To Python's Magic Methods](https://rszalski.github.io/magicmethods/)


### Making Custom Containers

```py
class TagCloud:
    def __init__(self):
        # Use double underscore to make attribute private.
        self.__tags = {}

    def print(self):
        print(self.__tags)

    def add(self, tag):
        self.__tags[tag.lower()] = self.__tags.get(tag.lower(), 0) + 1

    def __getitem__(self, tag):
        self.__tags.get(tag.lower(), 0)

    def __setitem__(self, tag, count):
        self.__tags[tag.lower()] = count

    def __len__(self):
        return len(self.__tags)

    def __iter__(self):
        return iter(self.__tags.items())


cloud = TagCloud()
cloud["python"] = 10
cloud.add("python")
cloud.add("python")
cloud.add("Python")
cloud.print()
print(len(cloud))
for tag, count in cloud:
    print(tag, count)
# Output:
# {'python': 13}
# 1
# python 13
```


### Properties

**Without decorators**

```py
class Product:
    def __init__(self, price):
        # Or self.price = price
        self.__set_price(price)

    def __get_price(self):
        return self.__price

    def __set_price(self, price):
        if price < 0:
            raise ValueError("Price cannot be negative")
        self.__price = price

    price = property(__get_price, __set_price)


product = Product(10)
print(product.price)
# Output: 10
```

**With decorators**

```py
class Product:
    def __init__(self, price):
        self.price = price

    @property
    def price(self):
        return self.__price

    @price.setter
    def price(self, price):
        if price < 0:
            raise ValueError("Price cannot be negative")
        self.__price = price


product = Product(10)
print(product.price)
# Output: 10
```


### Inheritance and Polymorphism

```py
# Base or Parent class.
class Animal:
    def __init__(self):
        # Attributes will be inhereted in Child Classes.
        self.age = 2

    # Method will be inhereted in Child Classes.
    def eat(self):
        print("eat")


# Sub or Child class.
class Mammal(Animal):
    def __init__(self):
        # Used to refer to Base class.
        super().__init__()
        self.weight = 10

    def walk(self):
        print("walk")


class Fish(Animal):
    def swim(self):
        print("swim")


m = Mammal()
m.eat()
# Output: eat

print(m.age, m.weight)
# Output: 2, 10


print(isinstance(m, Mammal))
# Output: True

print(isinstance(m, Animal))
# Output: True

# All classes are inhereted from class object.
print(isinstance(m, object))
# Output: True


print(issubclass(Mammal, Animal))
# Output: True

print(issubclass(Mammal, object))
# Output: True
```

```py
# Be careful with multi-level inheritance.
# Don't make too many unnecessary levels.
#
# Be careful with multiple inheritance.
# Don't do this with classes wich have something in common.
# Multiple inheritance can be done like this:
# class ChildClass(BaseClass1, BaseClass2, BaseClass3)
#
# Here is a good example of inheritance.

from abc import ABC, abstractmethod


class InvalidOperationError(Exception):
    pass


# ABC class is used to make Stream class abstract. ABC = Abstract Base Class.
class Stream(ABC):
    def __init__(self):
        self.opened = False

    def open(self):
        if self.opened:
            raise InvalidOperationError("Stream is already open.")
        self.opened = True

    def close(self):
        if not self.opened:
            raise InvalidOperationError("Stream is already closed.")
        self.opened = False

    @abstractmethod
    def read(self):
        pass


class FileStream(Stream):
    def read(self):
        print("Reading data from a file...")


class NetworkStream(Stream):
    def read(self):
        print("Reading data from a network...")


class MemoryStream(Stream):
    def read(self):
        print("Reading data from a memory...")


def read_data(stream):
    stream.open()
    # Polymorphism - specific reaction on the same function call by 
    # different objects connected with inheritance.
    #
    # Or. In other words.
    #
    # Polymorphism - the provision of a single interface
    # to entities of different types.
    #
    # Duck Typing can be used here. There is no need to have Stream class.
    stream.read()
    stream.close()


read_data(MemoryStream())
# Output: Reading data from a memory...
```

> **NOTES**
>
> Duck Typing - if it walks like a duck and quacks like a duck, it is a duck.
>
> Because Python is a dynamically typed language it doesn't check the type of objects. It only looks for the existence of certain methods in objects.
>
> So to achive polymorphic behavior it doesn't need base class. However having this base class is a good practice because of explicit common interface.


### Data classes

```py
from collections import namedtuple

Point = namedtuple('Point', ['x', 'y'])
p1 = Point(x=1, y=2)
p2 = Point(1, 2)
print(p1 == p2, p1.x)
# Output: True 1
```


## Modules and Packages

**Module** is a file that contains some Python code (functions, classes, variables, etc.).  
Every module have predefined attribures, like `__name__` - a name the module. The name of the module that starts our program is always `__main__`.

**Package** is a container (folder) for one or more modules.  
To make a package from directory it needs to put an empty file there called `__init__.py`. This file may contain any initialization code.  

```py
# Import code from packages (folders) and modules (files) syntax.
import folder_name.file_name

folder_name.file_name.function1()
folder_name.file_name.function2()


# Or.
from folder_name.file_name import function1, function2

function1()
function2()


# Or even.
from folder_name import file_name

file_name.function1()
file_name.function2()


# Package can contain any Sub-packages.
# Absolute import statement. Recomended.
from top_level_package.some_sub_package import some_module

some_module.function()


# Relative import statement.
# . means the current package.
# .. means one level up - package where current package is located.
from ..some_sub_package import some module

some_module.function()
```

### Module Search Path and `dir` Function

```py
from sys import path

# Path where Python is looking for modules to import.
print(path)
# Output:
# ['d:\\Code\\sandbox',
# 'C:\\Users\\anton\\AppData\\Local\\Programs\\Python\\Python38-32\\python38.zip',
# 'C:\\Users\\anton\\AppData\\Local\\Programs\\Python\\Python38-32\\DLLs',
# 'C:\\Users\\anton\\AppData\\Local\\Programs\\Python\\Python38-32\\lib',
# 'C:\\Users\\anton\\AppData\\Local\\Programs\\Python\\Python38-32',
# 'C:\\Users\\anton\\AppData\\Roaming\\Python\\Python38\\site-packages',
# 'C:\\Users\\anton\\AppData\\Local\\Programs\\Python\\Python38-32\\lib\\site-packages']

# List of attributes and methods in an object (e.g imported module).
print(dir(path))
# ['__add__', '__class__', '__contains__', '__delattr__', '__delitem__',
# '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__',
# '__getitem__', '__gt__', '__hash__', '__iadd__', '__imul__', '__init__',
# '__init_subclass__', '__iter__', '__le__', '__len__', '__lt__', '__mul__',
# '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__',
# '__reversed__', '__rmul__', '__setattr__', '__setitem__', '__sizeof__',
# '__str__', '__subclasshook__', 'append', 'clear', 'copy', 'count',
# 'extend', 'index', 'insert', 'pop', 'remove', 'reverse', 'sort']
```


## Python Standart Library


### Working with Path

```py
from pathlib import Path


# Absolute path. Raw string.
Path(r"C:\Program Files\Microsoft")

# Current folder.
Path()

# Related path.
Path("Folder\\__init__.py")

# Combining.
Path() / Path("Folder") / "__init__.py"

# Home directory of the current user.
Path.home()

path = Path(r"C:\app.py")
path.exists()
path.is_file()
path.is_dir()

print(path.name)
# Output: app.py

print(path.stem)
# Output: app

print(path.suffix)
# Output: .py

print(path.parent)
# Output: C:\

print(path.with_name("file.txt"))
# Output: C:\file.txt

print(path.with_suffix(".txt"))
# Output: C:\app.txt

print(path.absolute())
# Output: C:\app.py

```


### Working with Directories

```py
from pathlib import Path


path = Path(r"C:\directory")
path.exists()
path.mkdir()
path.rmdir()
path.rename(r"C:\dir")

print([item for item in Path("C:\\").iterdir() if item.is_file()])
# Output:
# [WindowsPath('C:/hiberfil.sys'),
# WindowsPath('C:/ngrok.exe'),
# WindowsPath('C:/pagefile.sys'),
# WindowsPath('C:/swapfile.sys')]

print([file for file in Path("C:\\").glob("*.exe")])
# Output: [WindowsPath('C:/ngrok.exe')]

# Search recursively.
print([file for file in Path("C:\\").glob("**/*.py")])

# Or use rglob().
print([file for file in Path("C:\\").rglob("*.py")])
```


### Working with Files

```py
from pathlib import Path
from time import ctime
import shutil

path = Path(r"C:\directory\file.txt")
path.exists()
path.rename(r"C:\directory\init.txt")

# Delete file (not move to Recycle Bin).
path.unlink()

# File status. Creation time.
print(ctime(path.stat().st_ctime))
# Output: Wed Apr 15 09:47:32 2020


# Read and write to binary file.
path.write_bytes()
path.read_bytes()

# Read and write to text file.
path.write_text("Hello, world!")
print(path.read_text())
# Output: Hello, world!


# Copy file.
source = Path(r"C:\directory\file.txt")
target = Path() / "init.txt"

target.write_text(source.read_text())

# Or using Shell Util.
shutil.copy(source, target)
```


### Working with Zip Files

```py
from pathlib import Path
from zipfile import ZipFile


# Write to Zip file.
with ZipFile(Path("files.zip"), "w") as zip:
    for path in Path().rglob('*.*'):
        zip.write(path)
        print(path)


# Read from Zip file.
with ZipFile(Path("files.zip")) as zip:
    print(zip.namelist())
    info = zip.getinfo(zip.namelist()[-1])
    print(info.file_size)
    print(info.compress_size)
    zip.extractall("extract")
```


### Working with CSV Files

**CSV** - Comma Separated Value.

```py
import csv


# Write to file.
with open("data.csv", "w") as file:
    writer = csv.writer(file)
    writer.writerow(["transaction_id", "product_id", "price"])
    writer.writerow([1000, 1, 5])
    writer.writerow([1001, 2, 15])


# Read from file.
with open("data.csv") as file:
    reader = csv.reader(file)
    for row in reader:
        print(row)
# Output: ['transaction_id', 'product_id', 'price']
# []
# ['1000', '1', '5']
# []
# ['1001', '2', '15']
# []

    # Or read them all as list.
    # print(list(reader))
# Output: [['transaction_id', 'product_id', 'price'],
# [],
# ['1000', '1', '5'],
# [],
# ['1001', '2', '15'],
# []]
```


### Working with JSON Files

```py
import json
from pathlib import Path

movies = [
    {"id": 1, "title": "Terminator", "year": 1989},
    {"id": 2, "title": "Kindergarten Cop", "year": 1990}
]


# Write to file.
data_to_write = json.dumps(movies)
Path("movies.json").write_text(data_to_write)


# Read from file.
read_data = Path("movies.json").read_text()
read_json = json.loads(read_data)
print(read_json[0]["title"])
# Output: Terminator
```


### Working with SQLite Database

```py
import sqlite3
import json
from pathlib import Path

movies = [
    {"id": 1, "title": "Terminator", "year": 1989},
    {"id": 2, "title": "Kindergarten Cop", "year": 1990}
]


# Write to database.
with sqlite3.connect("db.sqlite3") as connection:
    command = "INSERT INTO Movies VALUES(?, ?, ?)"
    for movie in movies:
        connection.execute(command, tuple(movie.values()))
    connection.commit()


# Read from database.
with sqlite3.connect("db.sqlite3") as connection:
    command = "SELECT * FROM Movies"
    cursor = connection.execute(command)
    for movie in cursor:
        print(movie)
# Output:
# (1, 'Terminator', 1989)
# (2, 'Kindergarten Cop', 1990)

    # Or get them all as list.
    # print(cursor.fetchall())
# Output: [(1, 'Terminator', 1989), (2, 'Kindergarten Cop', 1990)]
```

### Working with TimeStamps, DateTimes and TimeDeltas

```py
import time
from datetime import datetime


# Floating point number wich represents the number of seconds from the "begining of time".
print(time.time())
# Output: 1587006030.7655365


print(datetime(2020, 4, 16, 12, 41, 30))
# Output: 2020-04-16 12:41:30

print(datetime.now())
# Output: 2020-04-16 12:45:37.684226


# Format strings.
# %d - Day decimal number.
# %b - Month full name.
# %m - Month decimal number.
# %y - Year two digits.
# %Y - Yeat four digits.
# %H - Hour 24-hour clock.
# %I - Hour 12-hour clock.
# %p - am/pm.
# %M - Minutes.
# %S - Seconds.

print(datetime.strptime("2020/16/04 12:33:00 AM", "%Y/%d/%m %I:%M:%S %p"))
# Output: 2020-04-16 00:33:00

print(datetime.now().strftime("%Y/%d/%m %I:%M:%S %p"))
# Output: 2020/16/04 01:01:56 PM


# Convering from time to datetime.
print(datetime.fromtimestamp(time.time()))
# Output: 2020-04-16 13:01:56.921769
```

```py
from datetime import datetime, timedelta


dt1 = datetime(2018, 1, 1) + timedelta(days=1, seconds=1000)
print(dt1)
# Output: 2018-01-02 00:16:40

dt2 = datetime.now()
duration = dt2 - dt1
print(duration)
# Output: 835 days, 13:03:43.007117

print("days:", duration.days, "+ seconds:", duration.seconds,
      "= total seconds:", duration.total_seconds())
# Output: days: 835 + seconds: 47023 = total seconds: 72191023.007117
```


### Random values

```py
import random
import string


# Random float from 0 to 1.
print(random.random())
# Output: 0.9141889887876429

# Random int from 1 to 10.
print(random.randint(1, 10))
# Output: 2

# Random item from list.
print(random.choice([1, 2, 3, 4]))
# Output: 4

# Random items from list.
print(random.choices([1, 2, 3, 4], k=2))
# Output: [2, 4]

# Random password.
print("".join(random.choices(string.ascii_letters + string.digits, k=10)))
# Output: aa1N5A7n3u

# Shuffling array.
numbers = [1, 2, 3, 4]
random.shuffle(numbers)
print(numbers)
# Output: [2, 1, 3, 4]
```

### Browser and Emails

```py
import webbrowser

webbrowser.open("http://google.com")
webbrowser.open_new_tab("http://google.com")
```

```py
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.image import MIMEImage
from smtplib import SMTP
from pathlib import Path
from string import Template

# In file template.html we use $name.
template = Template(Path("template.html").read_text())
body = template.substitute({"name": "Anton"})

# Or the same.
# body = template.substitute(name="Anton")

# MIME - Multipurpose Internet Mail Extensions
message = MIMEMultipart()
message["from"] = "Anton Savchenko"
message["to"] = "anton.savchenko@mail.ru"
message["subject"] = "This is a test"

# Body may be a text or HTML.
message.attach(MIMEText(body, "html"))
message.attach(MIMEImage(Path("image.jpg").read_bytes()))

with SMTP(host="smtp.gmail.com", port=587) as smtp:
    # Hello message to SMTP-server
    smtp.ehlo()

    # TLS - Transport Layer Security.
    smtp.starttls()

    # In order to use this sign in code feature
    # "Allow less secure apps" should be ON in Google Account
    # https://myaccount.google.com/lesssecureapps
    smtp.login("anthony.savchenko@gmail.com", "password")
    smtp.send_message(message)
    print("Sent...")
# Output: Sent...
```


### Command-line arguments

```py
import sys
import string

if len(sys.argv) < 2:
    print("USAGE: python3 app.py message")
else:
    print("That's what you said after 'app.py': " + ", ".join(sys.argv[1:]))
```


### Run External Programs

```py
import subprocess

# Old school methods.
# subprocess.Popen()
# subprocess.call()
# subprocess.check_call()
# subprocess.check_output()

# Start OS command with parameters.
# NOTE: Still have questions how execute commands like 'dir' on Windows.
completed = subprocess.run(['python', '--version'],
                           capture_output=True,
                           text=True)

print("args:", completed.args)
print("returncode:", completed.returncode)
print("stderr:", completed.stderr)
print("stdout:", completed.stdout)
# Output:
# args: ['python', '--version']
# returncode: 0
# stderr: 
#stdout: Python 3.8.2


# Or start another Python script.
# Starts different process. It won't share variables and memory.
completed = subprocess.run(['python', 'other.py'],
                           capture_output=True,
                           text=True)

print("args:", completed.args)
print("returncode:", completed.returncode)
print("stderr:", completed.stderr)
print("stdout:", completed.stdout)
# Output :
# args: ['python', 'other.py']
# returncode: 0
# stderr: 
# stdout: Here it is.


# Or riise an CalledProcessError exception in case returncode is not 0.
# completed = subprocess.run(['python', 'other.py'],
#                            capture_output=True,
#                            text=True,
#                            check=True)
```


## Python Package Index (PyPI)

The [Python Package Index](https://pypi.org/) (PyPI) is a repository of software for the Python programming language.


### Pip

pip - tool to install packages from PyPI.

Symantic versioning: `M.n.p`, where:
- `M` is a major version,
- `n` is a minor version,
- `p` is a patch/bagfix version.

Pip version: `pip --version`.
Upgrade pip: `python -m pip install --upgrade pip`.
List of installed packages: `pip list`.
Install package: `pip install package-name`.
Install specific version: `pip install package-name==M.n.p`.
Install last compatible version: `pip install package-name==M.n.*`.
Or different syntax for the same result: `pip install package-name~=M.n.p`.
Or wild card with minor version: `pip install package-name==M.*`.
Uninstall package: `pip uninstall package-name`.
Install from text file: `pip install -r requirements.txt`
Save to text file: `pip freeze > requirements.txt`

*This method is classic but old-fashioned*


### Virtual Environment

Setup isolated virtual environment: `python -m venv env`. `env` - name of the environment.
Activate it: `env\Scripts\activate.bat`.
Deactivate it: `deactivate`.

*This method is classic but old-fashioned*


### Pipenv

pipenv - tool that combines `pip` and Virtual Environments into a single toolchain (equivalent to npm in JavaScript world). It`s a depandancy manager for Python projects.

Install pipenv: `pip install pipenv`.
Install package, create dependancy managment files (Pipfile and Pipfile.lock) and setup isolated virtual environment: `pipenv install package-name` or `pipenv install --dev package-name` or `pipenv install` (from `requirements.txt` or empty environment) or `pipenv --three`.
Lock versions to Pipfile.lock: `pipenv lock`
Get path to virtual environment directory: `pipenv --venv`.
Activate virtual environment: `pipenv shell`.
Deactivate it: `exit`.
List of installed dependencies: `pipenv graph`
Setup environment from Pipfile of a project: `pipenv install` or `pipenv install --dev`.
Setup environment from Pipfile.lock: `pipenv install --ignore-pipfile`
Show outdated packages: `pipenv update --outdated`
Update all depandencies: `pipenv update`
Update one dependency: `pipenv update package-name`
Run project: `pipenv run python main.py`


### Virtual Environment in VS Code

Setup code runner path: in VS Code *Settings* setup setting `code-runner.executorMap` - `python` to value `path-to-venv-dir\\Scripts\\python.exe`
Setup interpreter path: in VS Code *Settings* setup setting `python.pythonPath` to the same value.
Restart VS Code and select interpreter in left bottom corner. Install pylint.


### Pipfiles

Pipfile - latest available (if compatible) versions of application dependencies.
Pipfile.lock - exact versions of application dependencies to reproduce exact the sanme execution evironment on another machine.


### Publishing Packages

1. Setup tools: `pip install setuptools wheel twine`.
2. Make this structure:
    * `root`
        * `Package`
            * `__init__.py`
            * `other-files.py`
        * `setup.py` 
        * `LICENSE` ([Find appropriate license](https://choosealicense.com/))
        * `README.md`
3. Source for `setup.py`:
```py
import setuptools
from pathlib import Path


setuptools.setup(
    name="demo",
    version="1.0.0",
    author="Author",
    description="Description",
    long_description_content_type="text/markdown",
    long_description=Path("README.md").read_text(),
    packages=setuptools.find_packages(exclude=["data", "tests"]),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.8',
)
```
4. Make source and build distribution packages: `py setup.py sdist bdist_wheel`.
5. Upload to PyPI `twine upload dist/*`.


### Docstrings

```py
""" Short module description.

    Other description.
"""


class Class1:
    """ Class description. """

    def function1(self, param1):
        """
        Short function desctiption.

        Parameters:
        param1 (type): Description.

        Return:
        type: Description.
        """
        pass
```


## Popular Python Packages


### API

API - Application Programming Interface.  
REST - Representational State Transfer.

[Yelp](https://www.yelp.com/)

```py
# config.py


api_key = "key..."
```
```py
# app.py


import requests
import config


url = "https://api.yelp.com/v3/businesses/search"

headers = {
    "Authorization": "Bearer " + config.api_key
}
params = {
    "term": "Barber",
    "location": "NYC"
}
response = requests.get(url, headers=headers, params=params)
print(response)
businesses = response.json()["businesses"]
names = [business["name"] + "; " + str(business["rating"]) + " stars."
         for business in businesses if business["rating"] > 4.5]
[print(name) for name in names]
# Output:
# <Response [200]>
# Next Level Barber Shop; 5.0 stars.
# Gentlemen's Barbershop; 5.0 stars.
# The Barber Shop; 5.0 stars.
# The Kinsman Barber Shop; 5.0 stars.
# Otis & Finn Barbershop; 5.0 stars.
```


### Sending Text Messages

[Twilio](https://www.twilio.com/)

```py
# config.py


account_sid = "sid..."
auth_token = "token..."
```
```py
# app.py


from twilio.rest import Client


client = Client(account_sid, auth_token)
call = client.messages.create(
    to="+12345678901",
    from_="+12345678901",
    body="Hello, world!"
)
```


### Web Scraping

`pipenv install twilio`

```py
import requests
from bs4 import BeautifulSoup

response = requests.get("https://stackoverflow.com/questions")
soup = BeautifulSoup(response.text, "html.parser")

for question in soup.select(".question-summary"):
    title = question.select_one(".question-hyperlink").getText()
    votes = question.select_one(".vote-count-post").getText()
    print(f"{title} | {votes}")
```


### Browser Automation

`pipenv install selenium`

Browser drivers: [`selenium` package page](https://pypi.org/project/selenium/)

```py
from selenium import webdriver


browser = webdriver.Chrome()
browser.get("https://github.com")

browser.maximize_window()

sign_in_link = browser.find_element_by_link_text("Sign in")
sign_in_link.click()

username_box = browser.find_element_by_id("login_field")
username_box.send_keys("login...")
password_box = browser.find_element_by_id("password")
password_box.send_keys("password...")
password_box.submit()

assert "login..." in browser.page_source

profile_link = browser.find_element_by_class_name("user-profile-link")
link_label = profile_link.get_attribute("innerHTML")
assert "password..." in link_label

browser.quit()
```


### Working with PDFs

`pipenv install pypdf2`

```py
import PyPDF2


with open("Retainer Agreement.pdf", "rb") as file:
    reader = PyPDF2.PdfFileReader(file)
    print(reader.numPages)
    page = reader.getPage(0)
    page.rotateClockwise(90)
    writer = PyPDF2.PdfFileWriter()
    writer.addPage(page)
    with open("rotated.pdf", "wb") as output:
        writer.write(output)

merger = PyPDF2.PdfFileMerger()
file_names = ["Retainer Agreement.pdf", "rotated.pdf"]
for file_name in file_names:
    merger.append(file_name)
merger.write("combined.pdf")
```


### Working with Excel Spreadsheets

`pipenv install openpyxl`

```py
import openpyxl


# wb = openpyxl.Workbook()
wb = openpyxl.load_workbook("transactions.xlsx")
print(wb.sheetnames)
# Output: ['Sheet1']

# wb.create_sheet("Sheet2", 0)
# wb.remove_sheet(sheet)
sheet = wb["Sheet1"]

cell = sheet["A1"]
print("Cell", cell.coordinate, "Value", cell.value)
# Output: Cell A1 Value transaction_id

print("Row", cell.row, "Column", cell.column)
# Output: Row 1 Column 1

for row in range(1, sheet.max_row + 1):
    for column in range(1, sheet.max_column + 1):
        cell = sheet.cell(row, column)
        if cell.row == 4 and cell.column == 3:
            print(cell.value)
# Output: 7.95

column_cells = sheet["a"]
columns_cells = sheet["a:c"]
cells = sheet["a2:c4"]
cells = sheet[2:4]

sheet.append((1, 2, 3))

wb.save("transactions2.xlsx")
```

> **NOTES**
> Command Query Separation - principle in computer programming which states that function should either be a command (that perform an action to change the state of a system) or a query (that returns an answer to the caller without changing state or causing side effects) but not both.


### NumPy

`pipenv install numpy`

```py
import numpy as np


print(np.array([1, 2, 3]))
# Output: [1 2 3]

array = np.array([[1, 2, 7], [4, 5, 6]])
print(array)
# Output:
# [[1 2 7]
#  [4 5 6]]

print(array.shape)
# Output: (2, 3)

print(np.zeros((3, 4), dtype=int))
# Output:
# [[0 0 0 0]
#  [0 0 0 0]
#  [0 0 0 0]]

print(np.ones((3, 4), dtype=int))
# Output:
# [[1 1 1 1]
#  [1 1 1 1]
#  [1 1 1 1]]

print(np.full((3, 4), 5, dtype=int))
# Output:
# [[5 5 5 5]
#  [5 5 5 5]
#  [5 5 5 5]]

print(np.random.random((3, 4)))
# Output:
# [[0.35456708 0.1457123  0.37496737 0.32719519]
#  [0.29711852 0.71128895 0.91400756 0.07170448]
#  [0.417366   0.69871866 0.99237448 0.93075956]]

print(array[1, 2])
# Output: 6

print(array > 3)
# Output:
# [[False False  True]
#  [ True  True  True]]

print(array[array > 4])
# Output: [7 5 6]

print(np.sum(array))
# Output: 25

print(np.round(np.random.random((2, 2))))
# Output:
# [[0. 0.]
#  [1. 0.]]

dimensions_inch = np.array([1, 2, 3])
dimensions_cm = dimensions_inch * 2.54
print(dimensions_cm)
# Output: [2.54 5.08 7.62]
```


## Building Web Applications with Django

WSGI - Web Server Gate Interface.

**Main Commands**

Install django: `pipenv install django==2.1`.  
Activate virtual environment: `pipenv shell`.  
Install pylint-django: `pipenv install pylint-django`. And add line `load-plugins=pylint-django` in new file `.pylintrc` in the root of the project.  
Create new project: `django-admin startproject vidly .`.  
Start web server: `py manage.py runserver`. By defalut port is `8000`, but we can specify different one in the end of this command.  
Stop web server: `Ctrl` + `C`.  
Create new app: `py manage.py startapp movies`.  
Create migration files: `py manage.py makemigrations`.  
Apply migrations: `py manage.py migrate`.  
Look at SQL commands in migration: `py manage.py sqlmigrate movies 0001`.  
Create SuperUser: `py manage.py createsuperuser`.  

**Django project architecture**

MVC arcitectural pattern | django
-------------------------|-------
Model | Model
View | Template
Controller | View

**App structure**

View functions in `views.py` take request and return response.  
`urlpatterns` in `urls.py` map end-points to view functions or another url patterns.  
Models in `models.py` define app models.  
`migration` directory stores migrations.  
Registrations in `admin.py` add models to administration page.  
Templates are in `templates` folder.  

**Admin**

Credentials in first django project:  
Login: admin  
Email: anthony.savchenko@gmail.com  
Password: admin#21  

**Database API**

```py
# SELECT * FROM movies_movie
Movie.objects.all()

# SELECT * FROM movies_movie WHERE release_year = 1984
Movie.objects.filter(release_year=1984)

# SELECT * FROM movies_movie WHERE id = 1
Movie.objects.get(id=1)
```

**API**

Frameworks:
- `django-tastypie`
- `djangorestframework`

URL - Uniform Resource Locator.

**Deployment on Heroku**

Prerequisites:
- git,
- Heroku CLI,
- Heroku account,
- gunicorn web server: `pipenv install gunicorn`.
- Add static directory in the root directory and path to it into the `setting.py`: `STATIC_ROOT = os.path.join(BASE_DIR, 'static')`.
- Collect static files: `py manage.py collectstatic`.
- whitenoise for serving static files: `pipenv install whitenoise`.
- Add Middleware in `setting.py`: `'whitenoise.middleware.WhiteNoiseMiddleware',`.
- After creating Heroku app add it's name in `ALLOWED_HOSTS` in `settings.py`.

Deployment:
- `git init`.
- `git add .`.
- `git commit -m "Initial commit."`.
- `heroku login`.
- `heroku create`.
- `git push heroku master`.
- `heroku ps:scale web=1`.
- `heroku open`.

Adding changes:
- `git add .`.
- `git commit -m "Message."`.
- `git push heroku master`.


## Machine Learning with Python

Libraries:
- Numpy
- Pandas
- MatPlotLib
- Scikit-Learn

Tools:
- Anacondas
- Jupyter Noteboke

```py
import pandas as pd
df = pd.read_csv('vgsales.csv')
df.shape
df.describe()
df.values
df
```

```py
import pandas as pd
import joblib as jl
from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
from sklearn import tree


# 1. Import the Data.
music_data = pd.read_csv('music.csv')

# 2. Clean the Data.
X = music_data.drop(columns=['genre'])
y = music_data['genre']

# 3. Split the Data into Training/Test Sets.
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)

# 4. Create a Model (choose an algorithm).
model = DecisionTreeClassifier()

# 5. Train the Model.
model.fit(X_train, y_train)

# 6. Make Predictions.
predictions = model.predict(X_test)

# 7. Evaluate and Improve.
score = accuracy_score(y_test, predictions)
score


# Save to file.
jl.dump(model, 'music-recommender.joblib')

# Load from file.
model = jl.load('music-recommender.joblib')


# Visualize to file.
tree.export_graphviz(model,
                     out_file='music_recommender.dot',
                     feature_names=['age', 'gender'],
                     class_names=sorted(y.unique()),
                     label='all',
                     rounded=True,
                     filled=True)


# Show predictions.
predictions = model.predict([ [21, 1], [22, 0] ])
predictions
```