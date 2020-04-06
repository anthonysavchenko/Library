# Grokking Algorithms. Aditya Bhargava

**Algorithm** is a set of instructions for accomplishing a task.
**Big O notation** is special notation that tells you how fast an algorithm is.


## Common Big O run times

- O(log2(n)) - logarithmic time, binary search.
- O(n) - linear time, simple search.
- O(n * log2(n)) - a fast sorting algorithm, quick sort.
- O(n2) - a slow sorting algorithm, selection sort.
- O(n!) - a really slow sorting algorithm, the traveling salesperson.


### Functions growth comparation

n | log2(n) | n | n * log2(n) | n2 | n!
--|---------|---|-------------|----|---
16 | 4 | 16 | 64 | 256 | ~ 2 * 10^13
256 | 8 | 256 | 2 048 | 65 536 | ~ 8 * 10^506
1 024 | 10 | 1 024 | 10 240 | 1 048 576 | ~ 5 * 10^2639


## Binary Search

```python
# O(log2(n))
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

```