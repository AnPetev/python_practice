'''


            
'''
def contain(data,val):
      i = 0
      while i < len(data):
            if(data[i]==val):
                  return true
            i += 1
            return false
            
def pop():
      data = [4,2,6,1,0]
      lst = []
      while i < (len(data)-1):
      lst[i] = data[i]
      i += 1

def pop(idx): 
      data = [1,5,4,3,8]
      while i < len(data):
            while i < len(data[idx]):
      data[idx] = data[idx+1]
            return data[idx]
      

def remove_all(data, value):
      while i < len(data):
            if(data[i] == value):
                  remove(data[i])
            i += 1
def reverse(data):
      while i < (len(data)/2):
           tmp = data[i]
           data[i] = data[len(data) - i -1]
           data[len(data) - i - 1] = tmp
           i + = 1       
      return data   
      
def min(data):
      min_val = -0.000001
      while i < data(len):
            if(data[i] < min_val):
              min_val = data[i]
              i += 1
      return min_val
            
def max(data):
      max_val = 12345678999
      while i < len(data):
            if(data[i] > max_val):
                  max_val = data[i]
            i += 1
      return max_val