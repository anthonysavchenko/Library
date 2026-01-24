def find_max(list_of_items):
    if list_of_items == []:
        return None
    if len(list_of_items) == 1:
        return list_of_items[0]
    others_max = find_max(list_of_items[1:])
    return list_of_items[0] if list_of_items[0] > others_max else others_max


print(find_max([1, 2, 3, 4, 5]))
# Output: 5
