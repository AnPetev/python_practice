from random import randint
def word():
    res = []
    m = input('Enter the words:')
    res.append(m)
    while m != '':
        m = input('Enter the word:')
        if m not in res:
            res.append(m)
    return res[:-1]

#print(word())

def dividors(num):
    res = []
    for i in range(1,num):
        if num % i == 0:
            res.append(i)
    return res

#print(dividors(12))

def perfect_number(num):
    lst = dividors(num)
    sum = 0
    for i in lst:
        sum += i
    if sum == num:
        return True
    return False
#print(perfect_number((28)))

def zip(data1,data2):
    res = []
    for i in range(len(data1)):
          res.append(data1[i])
          res.append(data2[i])
    return res

#print(zip([1,2,3],[4,5,6]))

def palindrome(sentence):
    for i in range(0,int(len(sentence)/2)):
        if sentence[i] == sentence[len(sentence)-i-1]:
            return 'Is palindrome'
        return 'Isnot palindrome'

#m = str(input('Enter your sentence:'))
#print(palindrome((m)))

# def display():
#     m = input('Enter numbers:')
# 
#     sum1 = sum(lst)
#     mid = sum1 / len(lst)
#     left = []
#     right = []
#     for i in lst:
#         if i <= mid:
#             left.append(i)
#         if i > mid:
#             right.append(i)
#     return mid,left,right

#print(display())
def random():
    lst = []
    for i in range(0,6):
        tmp = randint(1,49)
        if tmp not in lst:
            lst.append(tmp)
        res = sorted(lst)
    return res

#print(random())
def sorted_or_not(lst):
    res = sorted(lst)
    if res:
        return True
    elif res == reverse(lst):
        return True
    else:
        return False

#m = input('Enter the numbers:')
#print(sorted_or_not(m))





