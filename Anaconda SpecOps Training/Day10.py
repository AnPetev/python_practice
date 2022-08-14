#problem1
def remove_dublicates(nums):
    for num in nums:
        if nums.count(num) > 1:
            nums.remove(num)
    return nums

# print(remove_dublicates([1,2,2,2,6,9,9]))

#problem2
def merge_sorted_array(nums1, nums2):
    m = len(nums1)
    n = len(nums2)
    a = sorted(nums1)
    b = sorted(nums2)
    i = 0
    j = 0
    res = []
    while i < m and j < n:
        if a[i] < b[j]:
            res.append(a[i])
            i += 1
        else:
            res.append(b[j])
            j += 1
    while i < m:
        res.append(a[i])
        i += 1
    while j < n:
        res.append(b[j])
        j += 1
    nums1 = res
    return nums1

# print(merge_sorted_array([1,2,3], [2,5,6]))

#problem3
def contains_dublicate(lst):
    nums = sorted(lst)
    print(nums)
    for i in range(0, len(nums)):
        if nums[i] == nums[i + 1]:
            return True
    return False

# print(contains_dublicate([1,2,5,2,8,9,9,4]))

#problem4
def single_number(lst):
    for num in lst:
        if lst.count(num) == 1:
            return num

# print(single_number([1,2,1]))

#problem5
def missing_number(lst):
    for num in range(len(lst) + 1):
        if num not in lst:
            return num

# print(missing_number([0,1,2,3,5]))

#problem6
def find_max_ones(lst):
    count = 0
    ans = 0
    for num in range(0, len(lst)):
        if lst[num] == 0:
            count = 0
        elif lst[num] == 1:
            count += 1
            ans = max(ans, count)
    return ans

# print(find_max_ones([1,1,0,1,1,1]))

#problem7
def array_partition(lst):
    res = 0
    s = sorted(lst)
    for num in range(0, len(s), 2):
        res += s[num]
    return res

# print(array_partition([6,2,6,5,1,2]))

#problem 8
def prime(n):
    if n <= 1:
        return False
    for num in range(2, n):
        if n % num == 0:
            return False
    return True

def largest_factor(n):
    res = []
    for num in range(1,n + 1):
        if n % num == 0 and prime(num):
            res.append(num)
    return max(res)

# print(largest_factor(6))

#problem 9
def palindrome(n):
    rev = 0
    tmp = n
    while n > 0:
        rem = n % 10
        rev = rev * 10 + rem
        n = n // 10
    if tmp == rev:
        return True
    return False

def largest_product():
    largest = 0
    for i in range(100, 1000):
        for j in range(100, 1000):
            if palindrome(i * j) and i * j > largest:
                largest = i * j
    return largest

# print(largest_product())

#problem10
def smallest_multiple():
    max_num = 100000
    num = 1
    res = 1
    while num < max_num:
        for i in range(1, 21):
            if num % i != 0:
                break
            else:
                res = num
        num += 1
    return res

# print(smallest_multiple())

#problem 11
def sum_square_difference():
    sum = 0
    tmp = 0
    for num in range(1, 100):
        num = num ** 2
        sum += num
    for num in range(1, 100):
        tmp += num
        res = tmp ** 2
    return sum - res

# print(sum_square_difference())

#problem 12
def n_th_prime(n):
    a = 1
    c = 0
    while c < n:
        a += 1
        for i in range(2, a + 1):
            if a % i == 0:
                break
        if i == a:
            c += 1
    return a

# print(n_th_prime(6))


