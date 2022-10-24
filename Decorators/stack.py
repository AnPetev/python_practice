def Stack(func):
      def wrap(*args):
            print("trying to call" + " " + func.__name__ +" " + "function")
            func(*args)
            print("the" + " " + func.__name__ + " " + "function called" )
      return wrap
      
      
st = []   
@Stack
def push(elem):
      st.append(elem)
      print(st)
      
@Stack
def pop():
      st.pop()
@Stack
def peek():
      print(st[0])
      
@Stack
def top():
      print(st[-1])
      
@Stack
def size():
      print(len(st))
      
@Stack
def isempty():
      if len(st) == 0:
            print("stack is empty")
      else:
            print("stack is not empty")
            
@Stack
def clear():
      global st
      st = []
      print(st)

@Stack
def show():
      print(st)


push(5)
push(2)
clear()
show()

      
