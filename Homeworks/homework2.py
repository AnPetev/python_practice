from random import randint
# weight = float(input("Enter the number in kilograms: "))
# total_weight = weight * 2.2
# print

for i in range(50):
    res = []
    m = randint(3,6)
    # print(m)

def sub(x, y):
    s = abs(x - y)
    sum = x + y
    return s / sum

# x = int(input("Enter the first number: "))
# y = int(input("Enter the second number: "))
# print(sub(x, y))

# year = int(input("Enter the year: "))
def leap_year(year):

    if year % 400 == 0 and year % 100 == 0:
        return True
    elif year % 100 != 0 and year % 4 == 0:
        return True
    else:
        return False
count = 0
# for y in range(1600, year):
#     if leap_year(y) == True:
#         count += 1
# print(count)

def perfect_number(num):
    res = []
    sum = 0
    for n in range(1, num):
        if num % n == 0:
            res.append(n)
    for i in range(0, len(res)):
        sum += res[i]
    if sum == num:
        return True
    return False

def all_divisors():
    i = 0
    res = []
    while i < 10000:
        if perfect_number(i) == True:
            res.append(i)
        i += 1
    return res

# print(all_divisors())

