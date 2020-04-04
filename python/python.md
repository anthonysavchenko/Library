# Python
Python - high-level cross-platform language.

## VS Code extensions:
* Python - Linting (pylint), Debugging, Formatting (autopep8).
* Code Runner - Runs code in terminal (Ctrl + Alt + N).

## Interpretation:
* CPython (C, default): Python program - CPython - Python Bytecode - Python Virtual Machine - Machine Code.
* IronPython (C#): Python program (with C# code) - IronPython - C# Bytecode - C# Virtual Machine - Machine Code.

## Types
```python
count = 1000               # int
rating = 4.99              # float
x = 1 + 2j                 # complex

published = True           # bool

greeting = "Hello, world!" # string
```

## Strings
```python
greeting = "   hello, world!"

print(greeting.title())                                  #    Hello, World!
print(greeting.strip())                                  # hello, world!
print(greeting[10:-1])                                   # world
print(f"{greeting.strip().title()} " + "How are you?")   # Hello, world! How are you?
print("It's me!")                                        # It's me!
print('It\'s me!')                                       # It's me!
print("\" \' \\ \n")                                     # " ' \ <new line character>
print("Hello, world!".replace("Hello", "Hi"))            # Hi, world!
print(greeting.find("hello"))                            # True
print("hello" in greeting)                               # True
print("bye" not in greeting)                             # True
print("*" * 10)                                          # **********
```

## Math
```python
dec = 10

print(dec += 3)            # 13 (there is no operator ++, like dec++)
print(dec / 3)             # 3.3333333333333335 (float)
print(dec // 3)            # 3 (integer)
print(dec % 3)             # 1 (reminder)
print(dec ** 3)            # 1000 (power)
print(round(3.1415, 2))    # 3.14 (math rules)
```
```python
import math

print(math.ceil(3.1415))   # 4 (closest int >= 3.1415)
```

## Falsy values:
* `""`
* `0`
* `None`

## If


## For


## While

