#problem 1
def build_an_array(target, n):
    res = []
    ans = 0
    for num in range(1,n + 1):
        if num in target:
            res.append('push')
            ans = max(len(res), ans)
        else:
            res.append('push')
            res.append('pop')
    return res[:ans]

#print(build_an_array([1, 3], 5))

#problem 2
def intersection(num1, num2):
    res = []
    for i in range(0,len(num1)):
        for j in range(0,len(num2)):
            if num1[i] == num2[j] and num1[i] not in res:
                res.append(num1[i])
    return res

#print(intersection([1,2,5,3], [2,6,5,9]))

#problem 3
def degree_an_array(lst):
    dict = {}
    for num in lst:
        if num in dict:
            dict[num] += 1
        else:
            dict[num] = 1
    for key, value in dict.items():
        print(key, value)

# print(degree_an_array([1,2,2,5,6,6,6]))

#problem 4
def sort_array_by_parity(lst):
     start = 0
     end = len(lst) - 1
     while start < end:
         if lst[start] % 2 > lst[end] % 2:
             lst[start], lst[end] = lst[end], lst[start]
         if lst[start] % 2 == 0:
             start += 1
         if lst[end] % 2 == 1:
             end -= 1
     return lst

#print(sort_array_by_parity([3,5,2,4,7]))

#problem 5
def sum_of_unique_elements(lst):
    dict = {}
    res = []
    sum = 0
    for num in lst:
        if num in dict:
            dict[num] += 1
        else:
            dict[num] = 1
    for num in dict:
        if dict[num] < 2:
            res.append(num)
    for i in res:
        sum += i
    return sum

# print(sum_of_unique_elements([1,2,2,3]))

#problem 6
def strstr(haystack, needle):
    if needle in haystack:
        return haystack.index(needle)
    return -1
# print(strstr('hello','lo'))

#problem 7
def length_of_lat_word(word):
    ans = 0
    new_word = word.strip()
    for str in range(len(new_word)):
        if new_word[str] == " ":
            ans = 0
        else:
            ans += 1
    return ans

# print(length_of_lat_word(' hello world '))

#problem 8
def palindrome(str):
    s = str.split()
    for num in range(0, (int(len(s) / 2))):
        if s[num] == s[len(s) - num -1]:
            return True
    return False

# print(palindrome('A man, a plan, a canal: Panama'))

#problem 9
def unique_emails(emails):
    s = set()
    for email in emails:
        start, end = email.split('@')
        if '+' in start:
            start = start[:start.index('+')]
        s.add(start.replace('.', '') + '@' + end)
    return len(s)


# print(unique_emails(["test.email+alex@leetcode.com", "test.e.mail+bob.cathy@leetcode.com",
# "testemail+david@lee.tcode.com"]))
#problem 10
def first_position(nums, target):
    res = -1
    start = 0
    end = len(nums) - 1
    while start <= end:
        mid = (start + end) // 2
        if nums[mid] < target:
            start = mid + 1
        elif nums[mid] > target:
            end = mid - 1
        else:
            end = mid - 1
            res = mid
    return res
def last_position(nums,target):
    res = -1
    start = 0
    end = len(nums) - 1
    while start <= end:
        mid = (start + end) // 2
        if nums[mid] < target:
            start = mid + 1
        elif nums[mid] > target:
            end = mid - 1
        else:
            start = mid + 1
            res = mid
    return res

# print(f'the first position is {first_position([1,2,2,2,3,5],2)} the last position is {last_position([1,2,2,2,3,5],2)}')









