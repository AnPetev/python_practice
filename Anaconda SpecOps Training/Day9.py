import random

#create file which consists of random numbers in range(1,200)
file = open('output.txt', 'w')
res = []
for line in range(4 * 100):
      value = random.randint(1, 201)
      file.write(f" {value} ")
      res.append(value)


#Counting the frequency of each chosen element
dict = {}
for num in res:
      if num in dict:
            dict[num] += 1
      else:
            dict[num] = 1

for key, value in dict.items():
      print(key, value)

#Sorting,then adding in the new file
s = sorted(res)
sorted_file = open('sorted.txt', 'w')
for num in s:
      sorted_file.write(f" {num} ")
      
