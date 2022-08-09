
#problem №1
file = open('input.txt', 'r')
lines = file.read()
nums = lines.split()
sum_ = 0
for line in nums:
        if line.isdigit() == True:
            sum_ += int(line)
print(sum_)


# problem  №2
file = open('text.txt', 'r')
for line in file:
    output = line.title()
    print(output)
    
# problem №3
def count_freq(lst):
    dict = {}
    for num in lst:
        if (num in dict):
            dict[num] += 1
        else:
            dict[num] = 1
    for key, value in dict.items():
        print(key,value)

#lst = [1,1,1,5,5,5,3,3,1,4,4,5]
#count_freq(lst)

#problem №4
file = open('data.txt', 'r')
txt = file.read()
count_symbols = len(txt)
print(count_symbols)

#problem №6
file = open('count.txt', 'r')
d = dict()
for line in file:
      words = line.split()
      for word in words:
            if word in d:
                  d[word] = d[word] + 1
            else:
                  d[word] = 1
print(d1)

#problem №7
def square(lst):
    res = []
    for num in range(0,len(lst)):
        lst[num] = lst[num] * lst[num]
        res = sorted(lst)
    return res
#lst = [4,6,9,2,11]
#print(square(lst))

#problem №8
def sum_of_digits(num):
    sum = 0
    while num != 0:
        rem = num % 10
        sum += rem
        num = num // 10
    return sum

# print(sum_of_digits(437))

#problem №9
def sub(num):
    sum = 0
    mul = 1
    while num != 0:
        rem = num % 10
        sum += rem
        mul *= rem
        num = num // 10
    return mul - sum

# print(sub(1234))

#problem №10
def odd(start, end):
    count = (end - start) // 2
    if start % 2 != 0 or end % 2 != 0:
        count += 1
    return count

print(odd(3,7))
