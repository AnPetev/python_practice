def all_sublist(larger):
      res = []
      n = len(larger)
      for i in range(n + 1):
            for j in range(i + 1,n + 1):
                  res.append(larger[i:j])
      return res
      
#print(all_sublist([1,2,3,4]))


def is_sublist(larger,smaller):
      n = len(larger)
      m = len(smaller)
      for i in range(n - m + 1):
            if larger[i:i + m] == smaller:
                  return True
            return False
            
#print(is_sublist([1,2,3,4],[2,4]))



