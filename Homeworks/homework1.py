def even_or_odd(num):
    if num % 2 == 0:
        return True
    return False
# input = input('Enter the number: ')
# print(even_or_odd(int(input)))

def vowel_or_consonant(ch):
    if ch in ('a','e','i','o','u'):
        print('its a vowel')
    else:
        print('its a consonant')

# input = input('Enter a character: ')
# print(vowel_or_consonant(input))


def nth_fib_number_rec(n):
    if n == 0:
        return 0
    if n == 1:
        return 1

    return nth_fib_number_rec(n - 1) + nth_fib_number_rec(n - 2)

# n = input('Enter the number: ')
# print(nth_fib_number(int(n)))

def nth_fib_number(n):
    a = 0
    b = 1
    while n != 0:
        tmp = a
        a = a + b
        b = tmp
    return b

# n = input('Enter a number: ')
# print(nth_fib_number_rec(int(n)))

def sum_of_digits(num):
    sum = 0
    while num != 0:
        rem = num % 10
        sum += rem
        num = num // 10
    return sum
# num = input('Enter the number: ')
# print(sum_of_digits(int(num)))


for i in range(0, 5):
   print('*', end = ' ')
print('\n')
for j in range(0, 2):
    print('   *   ', end = ' ')
print('\n')
for j in range(0, 2):
    print('   *   ', end = ' ')
print('\n')
for j in range(0, 2):
    print('   *   ', end = ' ')
print('\n')
for i in range(0, 5):
   print('*', end = ' ')
print('\n')


