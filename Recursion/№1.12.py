def pascal(m,n):
      if m == n or n == 1:
            return 1
      return pascal(m - 1,n - 1) + pascal(m - 1,n)