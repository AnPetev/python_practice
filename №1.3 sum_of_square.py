

def max_of_three_numbers(a,b,c):
      if a > b and a > c:
            if b > c:
                  return a**2 + b**2
            elif c > b:
                  return a**2 + c**2
      if b > a and b > c:
            if a > c:
                  return b**2 + a**2
            elif c > a:
                  return b**2 + c**2
      if c > a and c > b:
            if a > b:
                  return c**2 + a**2
            elif b > a:
                  return c**2 + b**2
            
      
      