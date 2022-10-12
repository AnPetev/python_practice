from random import randint


# time = int(input("enter the time: "))
# t = input("am or pm?: ")
# ahead = int(input("how many hours do you want?: "))
# if t == "am":
#       print(time + ahead)

questions = [
             "What star is in the center of the solar system?:",
             "What is the 3rd planet of the solar system?:",
             "What can be broken, but is never held?:",
             "What part of the body you use to smell?:",
             "How many days in one year?:",
             "How many letters in the alphabet?:",
             "Rival of Intel?:",
             "No.8 element on periodic element?:",
             "What is the galaxy that contains our solar system?:",
             "What animal is the king of the jungle?:"
             ]
             
             
answers = [
           "Sun",
           "Earth",
           "Promise",
           "Nose",
           "365",
           "26",
           "AMD",
           "Oxygen",
           "Milky Way",
           "Lion"
           ]

def player():
     
      score = 0
      for i in range(1,5):
            q = randint(0, 9)
            ans = input(questions[q])
            for j in range(len(answers)):
                  if ans.lower() == answers[j].lower():
                        score += 1
                        break
                  else:
                        continue
      return score
      

# print(player()) 

def rotate(ls):
      for i in range(len(ls) - 1, -1, -1):
            for j in range(len(ls) - 1, -1, -1):
                  print(ls[i][j], end = " ")
            print()
      
a = [[1, 2, 3, 4],
     [5, 6, 7, 8],
     [9, 10, 11, 12],
     [13, 14, 15, 16]]
     
# print(rotate(a))
  
def rotate_matrix(ls):
      n = 4
      i = n - 1
      while i >= 0:
            j = n - 1
            while j > 0:
                  print(ls[i][j], end = " ")
                  j = j -1
            print()
            i = i - 1
            
# print(rotate_matrix(a))      
 
 
m = [[0, 'M', 0, 'M', 0],     
     [0, 0, 'M', 0, 0],     
     [0, 0, 0, 0, 0],     
     ['M', 'M', 0, 0, 0],     
     [0, 0, 0, 'M', 0]]

# for i in range(len(m)):
#       for j in range(len(m)):
#             if m[i][j] == 0:
#                   m[i][j] = 1
                  
# for i in range(len(m)):
#       for j in range(len(m)):
#             print(m[i][j], end = " ")
#       print()

      
      
      
      