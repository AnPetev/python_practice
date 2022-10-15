from random import randint
# function implementations
def range_(start, stop, step):
    i = 0
    if start == 0 and step == 0:
        while i < stop:
            print(i)
            i += 1
    elif step == 0:
        while start < stop:
            print(start)
            start += 1
    elif step > 0:
        while start < stop:
            print(start)
            start += step
    elif step < 0:
        while start > stop:
            print(start)
            start += step

# start_ = int(input("enter the start: "))
# stop_ = int(input("enter the end: "))
# step_ = int(input("enter the step: "))
# print(range_(start_, stop_, step_))

# map function
def func(a):
    return a * 2

def map_(func, iterable):
    res = [None] * len(iterable)
    for i in range(len(iterable)):
        res[i] = func(iterable[i])
    return res

# print(map_(func, [1,2,3]))

# filter function
def predicate(a):
    if a % 2 == 0:
        return True
    else:
        return False

def filter_(pred, sequence):
    res = []
    for i in range(len(sequence)):
        if predicate(sequence[i]):
            res.append(sequence[i])
    return res

# print(filter_(predicate, [1,2,5,8,9,7]))


def zip_(ls1, ls2):
    s = []
    i, j = 0, 0
    while i != len(ls1) and j != len(ls2):
        s.append((ls1[i], ls2[j]))
        i += 1
        j += 1

    return s

# print(zip_(['type1', 'type2'], [1, 2, 3]))

def enumerate_(ls, start):
    res = []
    i = 0
    while i != len(ls):
        res.append((start, ls[i]))
        i += 1
        start += 1
    return res

# print(enumerate_("John", 2))



def merge(l1, l2):
    res = []
    i, j = 0, 0
    while i < len(l1) and j < len(l2):
        if l1[i] < l2[j]:
            res.append(l1[i])
            i += 1
        else:
            res.append(l2[j])
            j += 1
    while i < len(l1):
        res.append(l1[i])
        i += 1
    while j < len(l2):
        res.append(l2[j])
        j += 1
    return res


# print(merge([1, 5, 6], [2, 3, 4]))


def is_sorted(lst):
    res = sorted(lst)
    if res == lst:
        return True
    else:
        return False

# print(is_sorted([1, 2, 5, 0, 9]))


tic_tac = [[0, 1, 2],
           [0, 0, 2],
           [1, 0, 0]]

def choose_random(tic_tac):
    res = []
    for i in range(len(tic_tac)):
        for j in range(len(tic_tac)):
            if tic_tac[i][j] == 0:
                res.append(([i, j]))
    print(res)
    q = randint(0, len(res) - 1)
    print(q)
    k = []
    k.append(res[q])
    print(k)
    x, y = k[0][0], k[0][1]
    print(x)
    print(y)
    tic_tac[x][y] = 2
    return tic_tac

# print(choose_random(tic_tac))

# def verbose(num):
#     single_digit = {1:'one', 2:'two', 3:'three', 4:'four',5:'five',6:'six',7:'seven',8:'eight',9:'nine'}
#     two_digit = {10:'ten',20:'twenty', 30:'thirty',40:'forty',50:'fifty', 60:'sixty',70:'seventy',
#                  80:'eighty',90:'ninety'}
#     three_digit = {100:'hundred',200:'two hundred',300:'three hundred',400:'four hundred',500:'five hundred',
#                    600:'six hundred', 700:'seven hundred', 800:'eight hundred', 900:'nine hundred'}
#     if num < 10:
#         print(single_digit[num])
#     elif num > 10 and num < 99:


print(verbose(6))







