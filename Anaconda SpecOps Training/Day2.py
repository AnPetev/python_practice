def sum(num):
    total = 0
    for num in range(1000):
        if num % 3 == 0 or num % 5 == 0:
            total += num
    return total
#print(sum(10))

def sum_of_even_fib(n):
    a = 0
    b = 1
    sum = 0
    while n < 4000000:
        tmp = a + b
        if tmp % 2 == 0:
            sum += tmp
        a = b
        b = tmp
    return sum

#print(sum_of_even_fib(4))