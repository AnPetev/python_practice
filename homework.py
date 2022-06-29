import math
import time
def show(name):
    return name


# name1 = input('Enter your name:')
# print(show(name1))
# add = input('Enter your address:')
# print(show(add))
def info(name):
    return name


# m = input('Enter your name:')
# print(f'Hello from {info(m)}')
def square(length, width):
    return length * width

# length = float(input('Enter the length:'))
# width = float(input('Enter the width:'))
# print(f'The square is {square(length,width)} m^2')


def space_square(length,width):
    return length * width
def funt_to_akr(num):
    return num / 43560
# length = float(input('Enter the length:'))
# width = float(input('Enter the width:'))
# print(f'The square of space is {funt_to_akr(space_square(length,width))}')


def prices(count,volume):
    if volume <= 1:
        return round((count * 0.10),2)
    return round((count * 0.25),2)

# bottle_count = int(input('Enter the count:'))
# bottle_volume = float(input('Enter the volume:'))
# print(f'The total price is $ {prices(bottle_count,bottle_volume)}')
def order(sum):
    tax = round(((sum * 20) / 100),2)
    tip = round(((sum * 18) / 100),2)
    total_sum = sum - (tax + tip)
    return tax,tip,total_sum

# total_sum = int(input('How much is my order_sum:'))
# print(f'The tax is {order(sum)[0]}')
# print(f'The tip is {order(sum)[1]}')
# print(f'The total_sum is {order(sum)[2]}')

def sum_num(n):
    i = 0
    sum = 0
    while i < n:
        sum += i
        i += 1
    return sum
# num = int(input('Enter the number:'))
# print(sum_num(num))

def weight(suv,trifle):
     return suv * 75 + trifle * 112

# count_souvenir = int(input('How many souvenir do you want?'))
# count_trifle = int(input('How many trifle do you want?'))
# print(weight(count_souvenir,count_trifle))

def account(value):
        value = value + (value * 4) / 100
        print(value)
        total = value

        total = total + (total * 4) / 100
        print(total)
        tmp = total

        tmp = tmp + (tmp * 4) / 100
        print(tmp)

# val = int(input('How much do you want to insert?'))
# print(account(val))

def math_actions(a,b):
    print(a + b)
    print(a - b)
    print(a / b)
    print(a // b)
    print(a % b)
    print(math.log(a,10))

# a = int(input('Enter the number one:'))
# b = int(input('Enter the number second:'))
# math_actions(a,b)

def height(fut,inches):
    return fut * 12 * 2.54

# fut = float(input('How many fut is?'))
# inches = float(input('How many inches is?'))
# print(height(fut,inches))

def distance(fut):
    print(fut * 12)
    print(fut * 0.33333333)
    print(fut * 0.000189394)

# fut = float(input('Enter the fut count:'))
# distance(fut)

def area(r):
    return math.pi * (r ** 2),4/3 * math.pi * (r ** 3)

# r = float(input('Enter the r:'))
# print(area(r))

def volume_cylinder(r,h):
    return math.pi * (r ** 2) * h

# r = float(input('The r is:'))
# h = float(input('The h is:'))
# print(round(volume_cylinder(r,h)),1)

def fall(height):
     a = 9.8
     v = 0
     return math.sqrt(v ** 2 + 2 * a * height)

# h = float(input('Enter the height:'))
# print(fall(h))

def triangle(h,rib):
    return (h * rib) / 2

# h = float(input('Enter the height:'))
# rib = float(input('Enter the rib:'))
# print(triangle(h,rib))

def triangle_(s1,s2,s3):
    s = (s1 + s2 + s3) / 2
    return math.sqrt(s * (s - s1) * (s - s2) * (s - s3))

# s1 = float(input('the first is:'))
# s2 = float(input('the second is:'))
# s3 = float(input('the third is:'))
# print(triangle_(s1,s2,s3))

def time(day,hour,minute,seconds):
    return day * 86400 + hour * 3600 + minute * 60 + seconds

# day = int(input('Enter the day count:'))
# hour = int(input('Enter the hour count:'))
# minute = int(input('Enter the minute count:'))
# seconds = int(input('Enter the seconds count:'))
# print(time(day,hour,minute,seconds))


def print_month(month):
      if month == 'december' or month == 'march' or month == 'may' or month == 'jule' \
         or month == 'september' or month == 'november':
            return 31
      elif month == 'february':
            return 28 or 29
      else:
            return 30
# m = str(input('Enter the month:'))
# print(print_month(m))

def vowel_or_not(char):
      if char == 'a' or char == 'e' or char == 'i' or char == 'o' or char == 'u':
            print('Its a vowel')
      elif char == 'y':
            print('Its a vowel or consonant')
      else:
            print('Its a consonant')
            
# m = str(input('Enter the char:'))
# print(vowel_or_not(m))

def season(name,day):
      if name == 'march' or name == 'april' or name == 'may':
            print('Its a spring')
      elif name == 'june' or name == 'jule' or name == 'august':
            print('Its a summer')
      elif name == 'september' or name == 'october' or name == 'november':
            print('Its a autumn')
      else:
            print('Its a winter')
            
# month = str(input('Enter the month:'))
# day = int(input('Enter the day:'))
# print(season(month,day))

def mid(*args):
    sum = 0
    for num in args:
        if num == 0:
            raise 'error'
        sum += num
    n = len(args)
    mid_val = sum / n
    return mid_val

# lst = [1,2,3,4,5]
# print(mid(*lst))

def temperature(fahrenheit):
      res = []
      celsius = float((fahrenheit - 32) / 1.8)
      if celsius % 10 == 0:
            res.append(celsius)
      return res

# m = int(input('Enter the fahrenheit:'))
# print(temperature(m))

def game():
    for n in range(100):
        if n % 3 == 0 and n % 5 == 0:
            print("Fizzbuzz")
            continue
        elif n % 3 == 0:
            print("fizz")
            continue
        elif n % 5 == 0:
            print("buzz")
            continue
        print("fizzbuzz")

#print(game())