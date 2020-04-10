# Grokking Algorithms. Aditya Bhargava

[Errata](http://adit.io/errata.html)

**Algorithm** is a set of instructions for accomplishing a task.  
**Big O notation** is special notation that tells you how fast an algorithm is.


## Common Big O run times

- O(log<sub>2</sub>n) - logarithmic time, binary search.
- O(n) - linear time, simple search.
- O(n * log<sub>2</sub>n) - a fast sorting algorithm, quick sort.
- O(n<sup>2</sup>) - a slow sorting algorithm, selection sort.
- O(n!) - a really slow sorting algorithm, the traveling salesperson.


### Functions growth comparation

log<sub>2</sub>n | n | n * log<sub>2</sub>n | n<sup>2</sup> | n!
------------------|---|----------------------|---------------|---
4 | 16 | 64 | 256 | ~ 2 * 10<sup>13</sup>
8 | 256 | 2 048 | 65 536 | ~ 8 * 10<sup>506</sup>
10 | 1 024 | 10 240 | 1 048 576 | ~ 5 * 10<sup>2639</sup>


## Binary Search

O(log<sub>2</sub>n)

```python
def binary_search(items, search_for):
    low_index = 0
    high_index = len(items) - 1

    while low_index <= high_index:
        middle_index = (low_index + high_index) // 2

        if items[middle_index] == search_for:
            return middle_index

        if items[middle_index] > search_for:
            high_index = middle_index - 1
        else:
            low_index = middle_index + 1

        return None


print(binary_search([1, 5, 6, 10, 12], 6))
# Output: 2
```


## Arrays and Linked Lists

Arrays are good at random reading (*random access*).  
Linked lists are good at writing (or deleting) at the beginnig or at the end of structure and at sequential reading whole structure (*sequential access*).

Operation | Arrays | Linked Lists
----------|--------|-------------
Reading | O(1) | O(n)
Insertion | O(n) | O(1)
Deletion | O(n) | O(1)


## Selection sort

O(n<sup>2</sup>)

```python
def find_smallest(items):
    index_of_smallest = 0

    for i in range(1, len(items)):
        if items[i] < items[index_of_smallest]:
            index_of_smallest = i

    return index_of_smallest


def selection_sort(items):
    sorted_items = []

    while len(items) > 0:
        sorted_items.append(items.pop(find_smallest(items)))

    return sorted_items


print(selection_sort([5, 3, 6, 2, 10]))
# Output: [2, 3, 5, 6, 10]
```


## Recursion

Recursion is when function calls itself. It has advantage of clear code, but has disadvantage of low performance, when call-stack grows large and occupies a lot of memory. However any recursion can be rewritten with loops.

```py
def factorial(number):
    # Base case.
    if number == 1:
        return 1

    # Recursive case.
    else:
        return number * factorial(number - 1)


print(factorial(5))
# Output: 120
```
