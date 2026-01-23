def sum_items(*numbers):
    if numbers == ():
        return 0
    else:
        return numbers[0] + sum_items(*numbers[1:])


print(sum_items(1, 2, 3, 4, 5))
# Output: 15
