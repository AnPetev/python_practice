def bubble_sort(lst):
    for i in range(0,len(lst)):
        swapped = False
        for j in range(i + 1,len(lst)):
            if lst[i] > lst[j]:
                lst[i], lst[j] = lst[j], lst[i]
                swapped = True
        if not swapped:
            break
    return lst

# print(bubble_sort([1,7,3,5,9,0]))

def selection_sort(lst):
    for i in range(0, len(lst)):
        min_index = i
        for j in range(i + 1, len(lst)):
            if lst[j] < lst[min_index]:
                min_index = j
        lst[i], lst[min_index] = lst[min_index], lst[i]
    return lst

# print(selection_sort([4,2,6,9,2,0]))

def insertion_sort(lst):
    for i in range(1, len(lst)):
        j = i
        while j > 0 and lst[j] < lst[j - 1]:
            lst[j], lst[j - 1] = lst[j - 1], lst[j]
            j -= 1
    return lst

# print(insertion_sort([2,3,1,8,7]))

def merge_two_lists(lst1, lst2):
    a = sorted(lst1)
    b = sorted(lst2)
    i = 0
    j = 0
    res = []
    while i < len(a) and j < len(b):
        if a[i] < b[j]:
            res.append(a[i])
            i += 1
        else:
            res.append(b[j])
            j += 1
    while i < len(a):
        res.append(a[i])
        i += 1
    while j < len(b):
        res.append(b[j])
        j += 1
    return res

# print(merge_two_lists([1,5,8,2], [6,7,9,3]))

def merge_sort(lst):
    if len(lst) <= 1:
        return
    mid = len(lst) // 2
    left = lst[:mid]
    right = lst[mid:]
    merge_sort(left)
    merge_sort(right)
    lst = merge_two_lists(left, right)
    return lst

# print(merge_sort([1,5,3,2,9,7]))
