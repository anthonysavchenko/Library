def count_items(list_of_items):
    if list_of_items == []:
        return 0
    else:
        return 1 + count_items(list_of_items[:-1])


print(count_items([1, 2, 3, 4, 5]))
# Output: 5
