from random import randint
def reverse(num):
    rev_num = 0
    while num > 0:
        remainder = num % 10
        rev_num = (rev_num * 10) + remainder
        num = num // 10
    return rev_num


# n = int(input('Enter your number:'))
# print(reverse(n))


# tup = (1,2,3,4)
# print(list(tup))
# for i in range(0,len(tup)):
#    print(tup[i])
#
def sum_of_min_max(data):
    max_el = max(data)
    min_el = min(data)
    sum = max_el + min_el
    return sum
# lst = [1,2,5,8,4,31]
# print(f'The sum of max and min elements is {sum_of_min_max(lst)}')


def even_indices(data):
    res = []
    for i in range(0,len(data)):
        if (data[i] % 2) == 0:
            res.append(data.index(data[i]))
    return res

# lst = [1,5,9,7,6,4]
# print(even_indices(lst))


def reverse(word):
   for i in range(len(word) - 1,-1,-1):
       print(word[i],end = "")
   print("\n")

# m = input('Enter the word:')
# print(reverse(m))

def prime(n):
    if n < 1:
        return False
    for i in range(2,n):
        if n % i == 0:
            return False
    return True

def smallest_prime(n):
    if prime(n):
        return n
    return smallest_prime(n+1)
# m = int(input('enter the number:'))
# print(smallest_prime(m))

def get_median(data):
    n = len(data)
    if n % 2 != 0:
        return data[n // 2]
    return float((data[int((n-1) / 2)] + data[int(n / 2)]) / 2)


# lst = [4,2,6,9,5,8]
# tmp = sorted(lst)
# print(get_median(tmp))

def leap_year(year):
    if year % 400 == 0:
        return True
    if year % 100 == 0:
        return False
    if year % 4 == 0:
        return True
    return False

def count_days(month,year):
    if month in {1,3,5,7,8,10,12}:
        return 31
    if month == 2:
        if leap_year(year):
            return 29
        return 28
    return 30

# year = int(input('Enter the year:'))
# month = input('Enter the month:')
# print(count_days(year,month))

# def random_passwd(n):
#     for i in range(0,n):
#         tmp = randint(33,126)
#         ord(tmp)
#     return tmp

def same_parity(n,*args):
    # res = []
    # for i in args:
    #     if i % n == 0:
    #         res.append(i)
    # return res
    return [num for num in args if num % n == 0]


n = int(input('Enter the number:'))
lst = [4,2,6,9]
print(same_parity(n,*lst))





