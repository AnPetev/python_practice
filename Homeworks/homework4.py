import dis

#1
file = open('bararan.txt', 'r')
s = {}
s = file.readlines()
for word in s:
      print(word)



#2
st = 'hello'
print(st.__contains__('l'));
print(st.capitalize())
print(st.count('l'))
print(st.index('o'))
print(','.join(st))
print(st.replace('lo', 'da'))
print(st.split())

ls = [1,5,4,9,6,3,1]
ls.append(5)
print(ls)
print(ls.copy())
print(ls.count(1))
ls.reverse()
print(ls)
print(ls.pop())
ls.sort()
print(ls)
ls.insert(2,11)
print(ls)

dict = {'age':19, 'year':2003, 'name':'John'}
dict1 = {'age' : 22}
for i in dict.items():
      print(i)
for key in dict.keys():
      print(key)
for value in dict.values():
      print(value)
dict.update(dict1)
print(dict)
print(dict.get('age'))
print(dict.popitem())
el = dict.pop('year')
print(el)


#3
def myfunc(alist):
    return len(alist)
    
dis.dis(myfunc)
