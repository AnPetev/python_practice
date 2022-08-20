def big_number(num1, num2):
    n, m = len(num1) - 1, len(num2) - 1
    res = []
    rem = 0
    rem1, rem2 = 0, 0
    while n >= 0 or m >= 0:
        if n >= 0:
            rem1 = int(num1[n])
        else:
           rem1 = 0
        if m >= 0:
            rem2 = int(num2[m])
        else:
            rem2 = 0
        ans = rem + rem1 + rem2
        res.append(ans % 10)
        rem = ans // 10
        n -= 1
        m -= 1
    if rem:
        res.append(rem)
    res.reverse()
    return res



str1 = "123456"
str2 = "112369"
print(big_number(str1, str2))