sum1 = 0
sum2 = 0
for num in range(1, 100):
    sum1 += num
    res1 = sum1 ** 2
for num in range(1,100):
    num = num ** 2
    sum2 += num
# print( res1 - sum2)

def is_palindrome(num):
    rev_num = 0
    k = num
    while num > 0:
        rem = num % 10
        rev_num = rev_num * 10 + rem
        num = num // 10
    if rev_num == k:
        return True
    else:
        return False

# print(is_palindrome(121))
