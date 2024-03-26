# Name: Jessica Ye
# Date: 9/29/21
import random, time, math, heapq

class HeapPriorityQueue():
   # copy your HeapPriorityQueue() from Lab3
    def __init__(self):
        self.queue = ["dummy"]  # we do not use index 0 for easy index calulation
        self.current = 1        # to make this object iterable

    def next(self):            # define what __next__ does
        if self.current >=len(self.queue):
            self.current = 1     # to restart iteration later
            raise StopIteration
        
        out = self.queue[self.current]
        self.current += 1
    
        return out

    def __iter__(self):
        return self

    __next__ = next

    def isEmpty(self):
        return len(self.queue) == 1    # b/c index 0 is dummy

    def swap(self, a, b):
        self.queue[a], self.queue[b] = self.queue[b], self.queue[a]

    # Add a value to the heap_pq
    def push(self, value):
      self.queue.append(value)
      self.heapUp(len(self.queue[1:])-1)

    # helper method for push      
    def heapUp(self, k):
      # while (k > 1 and self.queue[k][0] < self.queue[math.floor(k/2)][0]):
      #    self.swap(k, math.floor(k/2))
      #    k = math.floor(k/2)
      parent = math.floor(k/2)
      if (k > 1 and self.queue[k][0] < self.queue[math.floor(parent)][0]):
         self.swap(k, math.floor(parent))
         # k = math.floor(k/2)
         self.heapUp(math.floor(parent))

    # helper method for reheap and pop
    def heapDown(self, k, size):
      if (k > size or k*2 > size):
         return
      
      maxChild = k*2
      if (maxChild+1<=size and self.queue[maxChild][0] > self.queue[maxChild+1][0]):
         maxChild = maxChild+1
      if (self.queue[k][0] > self.queue[maxChild][0]):
         self.swap(k, maxChild)
         self.heapDown(maxChild, size)
    
    # remove the min value (root of the heap)
    # return the removed value            
    def pop(self):
      # Your code goes here
      self.swap(1, -1)
      returnedVal = self.queue.pop(-1)
      if len(self.queue)>2:
         self.heapDown(1, len(self.queue[1:]))
      
      return returnedVal

      # make the queue as a min-heap          
      # never used  
    def reheap(self):
        for i in range(1, len(self.queue[1:])+1):
            self.heapDown(i, len(self.queue[1:]))

    # remove a value at the given index (assume index 0 is the root)
    # return the removed value   
    # never used
    def remove(self, index):
        removedVal = self.queue[index+1]
        self.queue.pop(index+1)

        self.reheap()
        return removedVal
        
def inversion_count(new_state, width = 4, N = 4):
    counter = 0

    for i in range(len(new_state)-1):
        # if s[i]!= '_':
        for j in range(i+1, len(new_state)):
            if (new_state[i]!= '_' and new_state[j]!='_' and new_state[i] > new_state[j]):
                counter += 1

    if (width % 2 == 1): #width is ODD
        # return inversion_countHelper(new_state) % 2 == 0
        return counter % 2 == 0
    else: #width is EVEN
        # s = list(new_state)
        blankIndex = new_state.index("_")
        
        if (math.floor(blankIndex/width))%2 == 1: #row even
            # return inversion_countHelper(new_state) % 2 == 1
            return counter % 2 == 1
        else:
            # return inversion_countHelper(new_state) % 2 == 0
            return counter % 2 == 0

def check_inversion():
   t1 = inversion_count("_42135678", 3, 3)  # N=3
   # print(t1)
   f1 = inversion_count("21345678_", 3, 3)
   # print(f1)
   t2 = inversion_count("4123C98BDA765_EF", 4) # N is default, N=4
   f2 = inversion_count("4123C98BDA765_FE", 4)
   return t1 and t2 and not (f1 or f2)


def getInitialState(sample, size):
   sample_list = list(sample)
   random.shuffle(sample_list)
   new_state = ''.join(sample_list)
   while not inversion_count(new_state, size, size): 
      random.shuffle(sample_list)
      new_state = ''.join(sample_list)
   return new_state
   
def swap(n, i, j):
   # Your code goes here
   # return n
   t = list(n)

   t[i],t[j] = t[j],t[i]
   return "".join(t)
      
'''Generate a list which hold all children of the current state
   and return the list'''
def generate_children(state, size=4):
   children = []
   blank = state.find('_')
   '''your code goes here'''
   # maxNumArr = size**2
   if not blank%size == 0: #left
      children.append(swap(state, blank, blank - 1))
   if not blank%size == size-1: #right
      children.append(swap(state, blank, blank + 1))
   # if not (blank < (size - 1) and (blank - size) < 0): #up
   if (blank >= size):
      children.append(swap(state, blank, blank - size))
   # if not (blank >= (size**2-size) and (blank+size) >= size**2): #down
   if (blank < (size**2-size)):
      children.append(swap(state, blank, blank + size))
      
   return children

def display_path(path_list, size):
   for n in range(size):
      for path in path_list:
         print (path[n*size:(n+1)*size], end = " "*size)
      print ()
   print ("\nThe shortest path length is :", len(path_list))
   return ""

''' You can make multiple heuristic functions '''
def dist_heuristic(state, back, orig):
   # Your code goes here
   # count = 0
   # return dist_heuristicBACK(state) if back else dist_heuristicFRONT(state)
   return dist_heuristicFRONT(state, orig) if back else dist_heuristicFRONT(state)

def dist_heuristicFRONT(state,goal = "_123456789ABCDEF", size=4):
   count = 0
   for i in range(len(goal)):
      # count = count + heurisiticHelper(goal[i], state, goal, size)
      count = count + abs(goal.index(goal[i])%size - state.index(goal[i])%size) + abs((goal.index(goal[i])//size) - (state.index(goal[i])//size))
   return count

def dist_heuristicBACK(state, goal = "_123456789ABCDEF", size=4):
   # Your code goes here
   count = 0
   for i in range(len(goal)):
      # count = count + heurisiticHelper(goal[i], state, goal, size)
      count = count + abs(state.index(goal[i])%size - goal.index(goal[i])%size) + abs((state.index(goal[i])//size) - (goal.index(goal[i])//size))
   return count

def check_heuristic():
   a = dist_heuristic("152349678_ABCDEF", "_123456789ABCDEF", 4)
   b = dist_heuristic("8936C_24A71FDB5E", "_123456789ABCDEF", 4)
   return (a < b) 

def a_star(start, goal="_123456789ABCDEF", heuristic=dist_heuristic, size = 4):
   # frontier = HeapPriorityQueue()
   add = []
   frontier = []
   explored = {start:['s']}
   # frontier.push((dist_heuristic(start), start, (start,)))
   # frontier.push((dist_heuristic(start), start, [start]))
   heapq.heappush(frontier, (dist_heuristic(start), start, [start]))
   while len(frontier)>0:
   # while not frontier.isEmpty():
      # print(frontier)
      # t = frontier.pop() #TUPLE!
      t = heapq.heappop(frontier)
      '''t[0] == path cost (int); t[1] == state (string); t[2] == path (list)'''
      
      if t[1] == goal:
         return t[2] #the path
      for a in generate_children(t[1]):
         if a not in t[2]:
            if a in explored:
               if t[1] in explored.get(a):
                  break
            newPath = [a]
            # newTuple = (sum(dist_heuristic(i) for i in t[2])+dist_heuristic(a), a, t[2]+newPath)

            
            newTuple = (len(t[2])+dist_heuristic(a), a, t[2]+newPath)
            # frontier.push(newTuple)
            heapq.heappush(frontier, newTuple)
            # explored[a] = t[1]

            if a in explored:
               add = explored.get(a) + [t[1]]
               del explored[a]
               explored[a] = add
               # print("YAY")
            else:
               explored[a] = [t[1]]

   # Your code goes here
   return None

def IDA(start, goal="_123456789ABCDEF"):
   frontier = []
   tuplePushed = (dist_heuristic(start, goal), start, [start])
   heapq.heappush(frontier, tuplePushed)
   explored = {start:['s']}
   # catalog[(dist_heuristic(start, goal), start, [start])] = start
   # print(frontier[0][2])
   for i in range(1, 1000):
      result = IDA_recur(frontier, start, goal, i, tuplePushed, explored)
      
      if result != None:
         return result


def IDA_recur(frontier, start, goal, limit, startTuple, explored):
   add = []
   if start == goal:
      return startTuple[2] #check??
   # estimate = len(frontier[0][2]) + dist_heuristic(start, goal)
   if startTuple[0] > limit:
      return None
   for a in generate_children(start):
      if ((dist_heuristic(a, goal)+len(startTuple[2])) < limit) and a not in startTuple[2]:
         if a in explored:
            print(explored.get(a))
            print(startTuple)
            if startTuple[1] in explored.get(a):
               break
         newPath = [a]
         newTuple = ((len(startTuple[2])+dist_heuristic(a, goal)), a, startTuple[2]+newPath)
         heapq.heappush(frontier, newTuple)
         if a in explored:
            add = explored.get(a) + [startTuple[1]]
            print (add)
            print(explored)
            del explored[a]
            explored[a] = add
         else:
            explored[a] = [startTuple[1]]
         result = IDA_recur(frontier, a, goal, limit, newTuple, explored)
         # print(result)
         # frontier.remove(newTuple)
         heapq.heappop(frontier)
         if result != None:
            return result

def solve(start, goal="_123456789ABCDEF", heuristic=dist_heuristic, size = 4):
   add = []

   f = [[], []]
   # p = [0, 0]
   explored = [{start:['s']}, {goal:['s']}]

   heapq.heappush(f[0], (dist_heuristic(start, False, start), start, [start]))
   heapq.heappush(f[1], (dist_heuristic(goal, True, start), goal, [goal]))
   
   while len(f[0])>0 or len(f[1])>0:
      for i in range(2):
         t = heapq.heappop(f[i])

         # print(t)
         '''t[0] == path cost (int); t[1] == state (string); t[2] == path (list)'''
        
         if t[1] == goal and i == 0:
            return t[2]  #the path
         if t[1] == start and i == 1:
            return t[2][::-1]

         for a in generate_children(t[1]):
            # print(explored[i])
            if a not in t[2] and a in explored[i]:
               if t[1] in explored[i].get(a):
                  break
            # newPath = [a]
            # newTuple = (sum(dist_heuristic(i) for i in t[2])+dist_heuristic(a), a, t[2]+newPath)

            
            # newTuple = (len(t[2])+dist_heuristic(a, i, start), a, t[2]+newPath)
               # print(dist_heuristic(a, i))
            # frontier.push(newTuple)
            # heapq.heappush(f[i], newTuple)
            heapq.heappush(f[i], (len(t[2])+dist_heuristic(a, i, start), a, t[2]+[a]))
            # explored[a] = t[1]

            if a in explored[i]:
               add = explored[i].get(a) + [t[1]]
               del explored[i][a]
               explored[i][a] = add
               # print("YAY")
            else:
               explored[i][a] = [t[1]]

   # Your code goes here
   return None

def main():
    # A star
   # print ("Inversion works?:", check_inversion())
   # print ("Heuristic works?:", check_heuristic())
   #initial_state = getInitialState("_123456789ABCDEF", 4)

   initial_state = input("Type initial state: ")
   if inversion_count(initial_state):
      cur_time = time.time()
      # path = (a_star(initial_state))
      path = (solve(initial_state))
      # path = (IDA(initial_state))
      if path != None: display_path(path, 4)
      else: print ("No Path Found.")
      print ("Duration: ", (time.time() - cur_time))
   else: print ("{} did not pass inversion test.".format(initial_state))
   
if __name__ == '__main__':
   main()


''' Sample output 1

Inversion works?: True
Heuristic works?: True
Type initial state: 152349678_ABCDEF
1523    1523    1_23    _123    
4967    4_67    4567    4567    
8_AB    89AB    89AB    89AB    
CDEF    CDEF    CDEF    CDEF    

The shortest path length is : 4
Duration:  0.0


Sample output 2

Inversion works?: True
Heuristic works?: True
Type initial state: 2_63514B897ACDEF
2_63    _263    5263    5263    5263    5263    5263    5263    5263    52_3    5_23    _523    1523    1523    1_23    _123    
514B    514B    _14B    1_4B    14_B    147B    147B    147_    14_7    1467    1467    1467    _467    4_67    4567    4567    
897A    897A    897A    897A    897A    89_A    89A_    89AB    89AB    89AB    89AB    89AB    89AB    89AB    89AB    89AB    
CDEF    CDEF    CDEF    CDEF    CDEF    CDEF    CDEF    CDEF    CDEF    CDEF    CDEF    CDEF    CDEF    CDEF    CDEF    CDEF    


The shortest path length is : 16
Duration:  0.005014657974243164


Sample output 3

Inversion works?: True
Heuristic works?: True
Type initial state: 8936C_24A71FDB5E

8936    8936    8936    893_    89_3    8943    8943    8_43    84_3    8423    8423    8423    8423    8423    8423    8423    8423    8423    8423    8423    8423    8423    8423    8423    8423    8423    8423    8423    8423    8423    _423    4_23    4123    4123    4123    4123    _123    
C_24    C2_4    C24_    C246    C246    C2_6    C_26    C926    C926    C9_6    C916    C916    C916    C916    C916    C916    C916    C916    C916    _916    9_16    91_6    916_    9167    9167    9167    9167    9167    9167    _167    8167    8167    8_67    8567    8567    _567    4567    
A71F    A71F    A71F    A71F    A71F    A71F    A71F    A71F    A71F    A71F    A7_F    A_7F    AB7F    AB7F    AB7F    AB7_    AB_7    A_B7    _AB7    CAB7    CAB7    CAB7    CAB7    CAB_    CA_B    C_AB    C5AB    C5AB    _5AB    95AB    95AB    95AB    95AB    9_AB    _9AB    89AB    89AB    
DB5E    DB5E    DB5E    DB5E    DB5E    DB5E    DB5E    DB5E    DB5E    DB5E    DB5E    DB5E    D_5E    D5_E    D5E_    D5EF    D5EF    D5EF    D5EF    D5EF    D5EF    D5EF    D5EF    D5EF    D5EF    D5EF    D_EF    _DEF    CDEF    CDEF    CDEF    CDEF    CDEF    CDEF    CDEF    CDEF    CDEF    

The shortest path length is : 37
Duration:  0.27825474739074707


Sample output 4

Inversion works?: True
Heuristic works?: True
Type initial state: 8293AC4671FEDB5_
8293    8293    8293    8293    8293    8293    8293    8293    82_3    8_23    8423    8423    8423    8423    8423    8423    8423    8423    8423    8423    8423    8423    8423    8423    8423    8423    8423    8423    8423    8423    8423    8423    _423    4_23    4123    4123    4123    4123    _123    
AC46    AC46    AC46    AC46    AC46    _C46    C_46    C4_6    C496    C496    C_96    C9_6    C916    C916    C916    C916    C916    C916    C916    C916    C916    _916    9_16    91_6    916_    9167    9167    9167    9167    9167    9167    _167    8167    8167    8_67    8567    8567    _567    4567    
71FE    71F_    71_F    7_1F    _71F    A71F    A71F    A71F    A71F    A71F    A71F    A71F    A7_F    A_7F    AB7F    AB7F    AB7F    AB7_    AB_7    A_B7    _AB7    CAB7    CAB7    CAB7    CAB7    CAB_    CA_B    C_AB    C5AB    C5AB    _5AB    95AB    95AB    95AB    95AB    9_AB    _9AB    89AB    89AB    
DB5_    DB5E    DB5E    DB5E    DB5E    DB5E    DB5E    DB5E    DB5E    DB5E    DB5E    DB5E    DB5E    DB5E    D_5E    D5_E    D5E_    D5EF    D5EF    D5EF    D5EF    D5EF    D5EF    D5EF    D5EF    D5EF    D5EF    D5EF    D_EF    _DEF    CDEF    CDEF    CDEF    CDEF    CDEF    CDEF    CDEF    CDEF    CDEF    

The shortest path length is : 39
Duration:  0.7709157466888428

2A8956C341FED_7B

'''
