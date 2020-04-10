from pprint import pprint

sentence = "This is a common interview question"
char_frequency = {}

for char in sentence:
    if char in char_frequency:
        char_frequency[char] += 1
    else:
        char_frequency[char] = 1

pprint(char_frequency)
# Output:
# {' ': 5,
#  'T': 1,
#  'a': 1,
#  'c': 1,
#  'e': 3,
#  'h': 1,
#  'i': 5,
#  'm': 2,
#  'n': 3,
#  'o': 3,
#  'q': 1,
#  'r': 1,
#  's': 3,
#  't': 2,
#  'u': 1,
#  'v': 1,
#  'w': 1}

char_frequency_sorted = sorted(char_frequency.items(),
                               key=lambda item: item[1],
                               reverse=True)

print(char_frequency_sorted[0])
# Output: ('i', 5)
