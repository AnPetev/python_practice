# problem 1
a = str(input("enter first number: "))
b = str(input("enter second number: "))
c = str(input("enter third number: "))
d = str(input("enter fourth number: "))
e = str(input("enter fifth number: "))

s = []
s.append(a)
s.append('+')
s.append(b)
s.append('+')
s.append(c)
s.append('+')
s.append(d)
s.append('+')
s.append(e)
k = ""
x = k.join(s)
print(str(x))

# problem 3
def palindrome(num):
    ans = num
    rev_num = 0
    while num != 0:
        rem = num % 10
        rev_num = rev_num * 10 + rem
        num = num // 10
    if rev_num == ans:
        return True
    return False
l = [x for x in range(100,1000) if palindrome(x)]
# print(l)

#problem 4
L = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47]
s = [x for x in range(2, 47) if x not in L]
print(s)
res = []
count = 0
ans = 0

for i in s:
    if i in s:
        count += 1
    ans = max(ans, count)
print(ans)


#problem 5
name = input("enter the name: ")
price = input("enter the price: ")
dict = {}
while name != '' and price != '':
    name = input("enter the name: ")
    price = input("enter the price: ")
dict = {name : price}
print(dict)

request = input("what do you want? ")
if request in dict:
    print(dict.values())

#problem 6
di = [{'name':'Todd', 'phone':'555-1414', 'email':'todd@mail.net'},
{'name':'Helga', 'phone':'555-1618', 'email':'helga@mail.net'}, {'name':'Princess', 'phone':'555-3141', 'email':''},
{'name':'LJ', 'phone':'555-2718', 'email':'lj@mail.net'}]
for i in di:
   for j in i['phone']:
       if '8' in j:
           print(i['name'])

for i in di:
    if i['email'] == '':
        print(i['name'])


#problem 7

matrix = [[1, 5, 2, 3, 14], [7, 5, 15, 9, 6], [5, 6, 11, 9, 7], [2, 7, 6, 7, 11], [10, 4, 15, 8, 9]]
dict = {}
for i in matrix:
    for j in i:
        if j in dict:
            dict[j] += 1
        else:
            dict[j] = 1
s = []
for value in dict.values():
    s.append(value)
print(s)
for i in s:
    if i >= 3:
        print(dict.keys())
print(s)
print(dict)




