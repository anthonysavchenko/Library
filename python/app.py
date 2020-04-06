# def fizz_buzz(input):
#     if (input % 3 == 0) and (input % 5 == 0):
#         return "FizzBuzz"
#     if input % 3 == 0:
#         return "Fizz"
#     if input % 5 == 0:
#         return "Buzz"
#     return input


# print(fizz_buzz(15))


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
