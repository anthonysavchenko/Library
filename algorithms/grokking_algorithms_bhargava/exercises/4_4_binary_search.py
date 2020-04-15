def binary_search(list_of_items, search_for):
    if list_of_items == []:
        return -1
    if len(list_of_items) == 1:
        return 0 if search_for == list_of_items[0] else -1
    else:
        middle_index = len(list_of_items) // 2
        if (search_for <= list_of_items[middle_index - 1]):
            return binary_search(list_of_items[:middle_index], search_for)
        else:
            return middle_index + binary_search(list_of_items[middle_index:], search_for)


print(binary_search([1, 2, 3, 4, 5], 4))
# Output: 3
