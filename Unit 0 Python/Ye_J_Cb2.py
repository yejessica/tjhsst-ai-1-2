#Jessica Ye
#8/30/21

def string_times(str, n):
  return str*n

def front_times(str, n):
  return str[:3]*n

def string_bits(str):
  return str[::2]

def string_splosion(str):
  return "".join(str[:i] for i in range(len(str)+1))

def last2(str):
  return sum(str[i:i+2] in str[-2:] for i in range(len(str)-2))

def array_count9(nums):
  return nums.count(9)

def array_front9(nums):
  return 9 in nums[:4]

def array123(nums):
  return (1,2,3) in zip(nums,nums[1:],nums[2:])

def string_match(a, b):
  return sum(a[i:i+2]==b[i:i+2] for i in range(len(b)-1)) 

def make_bricks(small, big, goal):
  return goal-min(big,goal//5)*5<=small

def lone_sum(a, b, c):
  return a*(b==c and c==a)+sum({a,b,c})*2-a-b-c

def lucky_sum(a, b, c):
  return (13 not in [a,b,c])*c + (13 not in [a,b])*b + (a!=13)*a

def no_teen_sum(a, b, c):
  return sum((i not in [13,14,17,18,19])*i for i in [a,b,c])

def round_sum(a, b, c):
  return sum((x+5)//10*10 for x in [a,b,c])

def close_far(a, b, c):
  return (abs(b-a)<2)+(abs(c-b)<2)+(abs(a-c)<2)==1

def make_chocolate(small, big, goal):
  return (goal-min(big,goal//5)*5+1)*(goal-min(big,goal//5)*5<=small)-1

def double_char(str):
  return "".join(c*2 for c in str)

def count_hi(str):
  return str.count("hi")

def cat_dog(str):
  return str.count('cat')==str.count('dog')

def count_code(str):
  return sum('co'==str[i:2+i]and'e'==str[i+3] for i in range(len(str)-3))

def end_other(a, b):
  return a.lower().endswith(b.lower()) or b.lower().endswith(a.lower())

def xyz_there(str):
  return str.count(".xyz")<str.count("xyz")

def count_evens(nums):
  return sum(~i%2 for i in nums)

def big_diff(nums):
  return max(nums)-min(nums)

def centered_average(nums):
  return sum(sorted(nums)[1:-1])//(len(nums)-2)

def sum13(nums):
  return sum(n for i, n in enumerate(nums) if n!=13 and (nums[i-1]!=13 or i==0))

def sum67(nums):
  return sum(n*(6 not in nums[:i+1] or (7 in nums[:i] and nums[i-1::-1].index(7)<nums[i-1::-1].index(6) and n!=6)) for i, n in enumerate(nums))

def has22(nums):
  return (2,2) in zip(nums,nums[1:])