def map_(func,data):
      res = [None] * len(data)
      for i in range(len(data)):
            res[i] = func(data[i])
      return res
      
def filter_(pred,data):
      res = [None] * len(data)
      for i in range(len(data)):
            if pred(i):
                  res[i] = data[i]
      return res

def triple(n):
     return 3 * n
     
def sum_(a,b,c):
      return a + b +c
def mul_(a,b,c):
      return a * b * c
#this function applies func function on data1,data2,data3
def map3(func, data1, data2, data3):
      res = [None] * len(data1)
      for i in range(len(data1)):
            res[i] = func(data1[i],data2[i],data3[i])
      return res
def func(a,b):
      return a ** b
 #this function returns base**exp
def map2(func, data1, data2):
      res = [None] * len(data1)
      for i in range(len(data1)):
            res[i] = func(data1[i],data2[i])
      return res
      
print(map_(triple,[1,3,4,5,8]))
print(map3(sum_,[1,2,3],[4,5,6],[7,8,9]))
print(map3(mul_,[1,2,3],[4,5,6],[7,8,9]))
print(map2(func,[10,20,30,40,50],[1,2,3,4,5]))