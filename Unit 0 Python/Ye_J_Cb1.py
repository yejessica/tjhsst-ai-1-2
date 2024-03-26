# Jessica Ye
# 8/25/2021

def sleep_in(weekday, vacation):
  return (not weekday or vacation)

def monkey_trouble(a_smile, b_smile):
  return (a_smile == b_smile)

def sum_double(a, b):
  return (a + b) *2 if a == b else (a + b)

def diff21(n):
  return abs(n-21)*2 if n>21 else abs(n-21)

def parrot_trouble(talking, hour):
  return talking and (hour < 7 or hour > 20)

def makes10(a, b):
  return (a == 10 or b == 10 or (a + b) == 10)

def near_hundred(n):
  return (abs(n-100) <= 10 or abs(n-200) <= 10)

def pos_neg(a, b, negative):
  return (a < 0 and b < 0) if negative else ((a < 0 and b > 0) or (a > 0 and b < 0))

def hello_name(name):
  return ("Hello " + name + "!")

def make_abba(a, b):
  return a + b + b + a

def make_tags(tag, word):
  return '<' + tag + '>' + word + '</' + tag + '>'

def make_out_word(out, word):
  return out[0 : int(len(out)/2)] + word + out[int(len(out)/2) : len(out)]

def extra_end(str):
  return (str[-2:] *3)

def first_two(str):
  return str if len(str) <= 2 else str[:2]

def first_half(str):
  return str[0:int(len(str)/2)]

def without_end(str):
  return str[1:len(str)-1]

def first_last6(nums):
  return nums[0] == 6 or nums[-1] == 6

def same_first_last(nums):
  return (len(nums) >= 1 and nums[0] == nums[-1])

def make_pi(arg):
  return [int("3141592653589793238462643383279"[element]) for element in range(0, arg)]

def common_end(a, b):
  return (a[0] == b[0] or a[-1] == b[-1])

def sum3(nums):
  return sum(nums)

def rotate_left3(nums):
  return ([nums[i-len(nums)+1] for i in range(len(nums))] )

def reverse3(nums):
  return ([nums[-i-1] for i in range(len(nums))]) #str[::-1]

def max_end3(nums):
  return ([nums[0] for i in range(len(nums))] if nums[0] > nums[-1] else [nums[-1] for i in range(len(nums))])

def cigar_party(cigars, is_weekend):
  return (cigars >= 40 and cigars <= 60 and is_weekend == False) or (cigars >= 40 and is_weekend == True)

def date_fashion(you, date):
  return 0 if (you <= 2 or date <= 2) else 2 if (you >= 8 or date >= 8) else 1

def squirrel_play(temp, is_summer):
  return False if (temp > 90 and is_summer == False) or (temp < 60) or (temp > 100 and is_summer == True) else True

def caught_speeding(speed, is_birthday):
  return 2 if (speed >= 81 and is_birthday == False) or (speed >= 86 and is_birthday == True) else 1 if (speed >= 61 and is_birthday == False and speed <= 80) or (speed >= 66 and is_birthday == True and speed <= 85) else 0
  
def sorta_sum(a, b):
  return a + b if (a + b) <= 9 or (a + b) >= 21 else 20

def alarm_clock(day, vacation):
  return "7:00" if day >= 1 and day <= 5 and vacation == False else "10:00" if ((day == 0 or day == 6) and vacation == False) else "10:00" if (day >= 1 and day <= 5 and vacation == True) else "off"

def love6(a, b):
  return True if (a == 6 or b == 6) or (a + b == 6) or (abs(a - b) == 6) else False

def in1to10(n, outside_mode):
  return True if (n >= 1 and n <= 10 and outside_mode == False) or (outside_mode == True and (n <= 1 or n >= 10)) else False
