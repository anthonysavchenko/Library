# Python

Python - high-level cross-platform language.
[Official documentation](https://www.python.org)


## VS Code extensions

* Python - Linting (pylint), Debugging, Formatting (autopep8).
* Code Runner - Runs code in terminal (Ctrl + Alt + N).


## Interpretation

* CPython (C, default): Python program - CPython - Python Bytecode - Python Virtual Machine - Machine Code.
* IronPython (C#): Python program (with C# code) - IronPython - C# Bytecode - C# Virtual Machine - Machine Code.


## Types

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


## Strings

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


## Math

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


## Falsy values:

* `''`
* `""`
* `0`
* `None`
* `[]`


## If

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

**Notes:**
- `18 <= age < 65` - chaining comparison.


## For

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


## While

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

**Notes:**
- `first_name` and `last_name` are parameters, `"John"` and `"Smith"` are arguments.
- All functions return `None` value by default.


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


## Lists

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


#### Sorting Complex Items

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


## Lambda Functions, Map, Filter, Zip Functions and List Comprehension

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


## Stack and Queue

Stack - **LIFO** - **L**ast **I**n - **F**irst **O**ut
Use simple array `[1, 2, 3]`. Methods: `append(4)`, `pop()`. Top of the stack: `[-1]`.

Queue - **FIFO** - **F**irst **I**n - **F**irst **O**ut
Use class: `deque([1, 2, 3])`, Methods: `append(4)`, `popleft()`.


## Tuple

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


## Array

Array performs faster than ordinary list on large ammount of items.
Use class `array("i", [1, 2, 3])`. Methods: `append(4)`, `insert(5, 3)`, `pop()`, `remove(2)`


## Set

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


## Dictionary

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


## Generator object

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


## Unpacking operator

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

print({*range(5), *"Hello"})
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

**Notes:**
- `pass` is a statement wich doesn't do anything and is used when we can't have an empty code block.
