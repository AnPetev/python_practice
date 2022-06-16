def f_rec(n):
      if (n < 3):
            return n
      return f_rec(n-1)+f_rec(n-2)+f_rec(n-3)
      

def f_iter(n):
      a = 0
      b = 1
      c = 2
      while n > 0
            tmp = a
		a = a + b + c
		b = tmp
		n -= 1
	return b
