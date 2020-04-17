# Grokking Algorithms. Aditya Bhargava

[Errata](http://adit.io/errata.html)


## Introduction to algorithms

**Algorithm** is a set of instructions for accomplishing a task.  
**Big O notation** is special notation that tells you how fast an algorithm is.


### Common Big O run times

- O(log<sub>2</sub>n) - logarithmic time, binary search.
- O(n) - linear time, simple search.
- O(n * log<sub>2</sub>n) - a fast sorting algorithm, quick sort.
- O(n<sup>2</sup>) - a slow sorting algorithm, selection sort.
- O(n!) - a really slow sorting algorithm, the traveling salesperson.


### Functions growth comparation

log<sub>2</sub>n | n | n * log<sub>2</sub>n | n<sup>2</sup> | n!
-----------------|---|----------------------|---------------|---
4 | 16 | 64 | 256 | ~ 2 * 10<sup>13</sup>
8 | 256 | 2 048 | 65 536 | ~ 8 * 10<sup>506</sup>
10 | 1 024 | 10 240 | 1 048 576 | ~ 5 * 10<sup>2639</sup>


### Binary Search

O(log<sub>2</sub>n)

```py
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


## Selection sort


### Arrays and Linked Lists

Arrays are good at random reading (*random access*).  
Linked lists are good at writing (or deleting) at the beginnig or at the end of structure and at sequential reading whole structure (*sequential access*).

Operation | Arrays | Linked Lists
----------|--------|-------------
Reading | O(1) | O(n)
Insertion | O(n) | O(1)
Deletion | O(n) | O(1)


### Selection sort

O(n<sup>2</sup>)

```py
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


## Quick Sort

**Divid-and-conquer (D&C)** is a general recursive technique for solving problems. It works by breaking a problem down into smaller and smaller pieces.

**Inductive proof** is way to prove that algorithm works. It has two streps: the base case and the inductive case. Like recursion.

Constants in Big O notation can matter sometimes. That's why quicksort is faster than merge sort.

O(n * log<sub>2</sub>n) in best and average case, but O(n<sup>2</sup>) in worth case.

```py
def quick_sort(items):
    if len(items) < 2:
        return items
    else:
        pivot = items[len(items) // 2]
        less = [i for i in items[1:] if i <= pivot]
        greater = [i for i in items[1:] if i > pivot]
        return quick_sort(less) + [pivot] + quick_sort(greater)


print(quick_sort([1, 4, 19, 12, 8]))
# Output: [1, 4, 8, 12, 19]
```

## Hash Tables

Hash Table (hash map, map, dictionary or associative array) - a data structure wich applies hash function to keys to store values in array.

**Hash function**
- Maps keys to values.
- Should be consistent (should return the same value for one key every time).
- Should map different keys to different values.
- Should return values in known range, not less or greater.

**Collision**: two keys give the same value. The simplest way to solve this is to use a linked list.

To avoid collisions:
- Low load factor (number of items / number of slots). Resize (make array twice bigger) when load factor > 0.7.
- Good hash funcion. Wich distributes values in the array evenly.

**Performance of hash table**
Operation | Avarage case | Worst case
----------|--------------|-----------
Search | O(1) | O(n)
Insert | O(1) | O(n)
Delete | O(1) | O(n)


## Breadth-First Search (BFS)

BFS finds:
- whether there is a way from one node to another,
- shortest way in case it exists.

O(V + E), where:
- V for number of vertices,
- E for number of edges.

```py
from collections import deque


def breadth_first_search(graph, start, search_for, debug=False):
    # deque - double-ended queue.
    queue = deque(((start,),))
    searched = []
    while queue:
        route = queue.popleft()
        print("   poped:", route)
        if not route[-1] in searched:
            if route[-1] == search_for:
                if debug:
                    print("searched:", searched)
                    print("  answer:", route)
                return route
            else:
                [queue.append((*route, node)) for node in graph[route[-1]]]
                if debug:
                    [print("appended:", (*route, node))
                     for node in graph[route[-1]]]
                searched.append(route[-1])
    if debug:
        print("searched:", searched)
    return False


# Graph can be a dictionary (wich is hash table).
# graph = {}
# graph["you"] = ["alice", "bob", "claire"]
# graph["bob"] = ["anuj", "peggy"]
# graph["alice"] = ["peggy"]
# graph["claire"] = ["thom", "jonny"]
# graph["anuj"] = []
# graph["peggy"] = []
# graph["thom"] = []
# graph["jonny"] = []

# Or it can be a tuple.
# graph[0] = (1, 2, 6)
# graph[1] = (3, 0)
# graph[2] = (5,)
# graph[6] = (7, 4)
# graph[3] = ()
# graph[4] = ()
# graph[5] = ()
# graph[7] = ()

# Or the same tuple.
graph = ((1, 2, 6), (3, 0), (5,), (), (), (), (7, 4), ())

breadth_first_search(graph, 0, 4, debug=True)
```

**Topological sort** - sort of list of graph vertices in order of their dependancy from each other.
**Tree** - graph with edges directed one way without back ups.


## Dijkstra's algorithm
