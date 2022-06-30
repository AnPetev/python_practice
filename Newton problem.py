
def pow(base,exp):
      if exp > 0:
            return base**exp
      if exp < 0:
            return 1 / (base**exp)
      if base == 0 and exp < 0:
            return 'Animast e'
      if exp == 0:
            return 1
            
#print(pow(2,6))

def guess_enough(value,target):
      if (value**3 - target) < 0.0001:
            return True
      return False
def improve(root,target):
      return (root + target / root) /2
def sqrt(n):
      root = 1
      while not guess_enough(root,n):
            root = improve(root,n)
      return root
      
#print(sqrt(5)) 


            
            