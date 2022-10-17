
def sum(a, b):
      return a + b


def reduce(function, iterable, initializer=None):
      it = iter(iterable)
      if initializer is None:
            value = next(it)
      else:
            value = initializer
      for element in it:
            value = function(value, element)
      return value


# print(reduce(sum, [1, 2, 3, 4, 5]))

def reduce_for_itertools(iterable, func):
      res = []
      it = iter(iterable)
      value = next(it)
      for element in it:
            value = func(value, element)
            res.append(value)
      return res[-1]

# print(reduce_for_itertools([1,2,3,4,5], sum))


def multiply_with(n):
      def number(x):
            for i in range(1, 11):
                  print(i * n)
      return number


s = multiply_with(9)
# print(s(3))


board = [["8","3",".",".","7",".",".",".","."]
,["6",".",".","1","9","5",".",".","."]
,[".","9","8",".",".",".",".","6","."]
,["8",".",".",".","6",".",".",".","3"]
,["4",".",".","8",".","3",".",".","1"]
,["7",".",".",".","2",".",".",".","6"]
,[".","6",".",".",".",".","2","8","."]
,[".",".",".","4","1","9",".",".","5"]
,[".",".",".",".","8",".",".","7","9"]]

def valid_sudoku(board):
    column = [set() for i in range(9)]
    row = [set() for i in range(9)]
    square = [[set() for i in range(3)] for j in range(3)]
    for i in range(9):
        for j in range(9):
            if board[i][j] == ".":
                continue
            if (board[i][j] in row[i] or board[i][j] in column[j] or board[i][j] in square[i // 3][j // 3]):
                return False
            column[i].add(board[i][j])
            row[j].add(board[i][j])
            square[i // 3][j // 3].add(board[i][j])
    return True

print(valid_sudoku(board))





