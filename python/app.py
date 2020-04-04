import math

# escape sequances
print("Hello \"world" + '\n \'Hi "Guys"!')
print("*" * 20)

students_count = 1000                           # int
rating = 4.99                                   # float
x = 1 + 2j                                      # complex

is_published = True                             # bool

course_name = "     python    programming    "  # str

print(course_name.title())
print(course_name.strip())
print(course_name[7:10])
print(course_name[5])
print(course_name[5:11])
print(course_name[15:-4])
print(f"{students_count} {course_name.upper()}")
print(course_name.find("Pro"))
print(course_name.replace("p", "j"))
print("pro" in course_name)
print("swift" not in course_name)

print(10 / 3)
print(10 // 3)
print(10 % 3)
print(10 ** 3)

y = 10
y = y + 3
y += 3
# not y++

print(y)
print(round(3.4332, 2))
print(abs(-1))

print(math.ceil(5.234))

#a = input("Give me a number: ")
# print(type(a))
#b = int(a) + 1
#print(f"I've got {a} and come up with {b}")

# Falsy
# ""
# 0
# None
# else is True

if "bag" > "apple":
    print("Aha")
elif True:
    print("Ugu")
else:
    print("Nope")
print("Done")

age = 22
print("eligible" if age >= 18 else "not eligible")

high_income = True
good_credit_score = False
student = False

# short-circuit evaluation
if (high_income or good_credit_score) and not student:
    print("eligible")
else:
    print("not eligible")

# chaining comparison operators
age = 22
if 18 <= age < 65:
    print("that's ok")
else:
    print("it's a bad idea")

for number in range(1, 10, 2):
    print("Attempt", number, number * ".")

# for...else
succesful = True
for count in range(3):
    print("Attempt")
    if (succesful):
        print("Successful")
        break
else:
    print("Attempted 3 times and failed")

print("\n\n")

for i in range(5):
    for j in range(3):
        print(f"({i}, {j})")

print("\n\n")

# iterable:
# range
# string
# list

num = 100
while num > 0:
    print(num)
    num //= 2

print("\n\n")

m = 0
for t in range(1, 10):
    if t % 2 == 0:
        print(t)
        m += 1
print(f"We have {m} even numbers")
