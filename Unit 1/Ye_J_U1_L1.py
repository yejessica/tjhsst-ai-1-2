import random

def getInitialState():
   x = "_12345678"
   l = list(x)
   random.shuffle(l)
   y = ''.join(l)
   return y
   
'''precondition: i<j
   swap characters at position i and j and return the new state'''
def swap(state, i, j): #   '''your code goes here'''
   temp = list(state)
   indexI = state[i]
   indexJ = state[j]
   temp[i] = indexJ
   temp[j] = indexI
   # print("state", state)
   # print("final", "".join(temp))
   return "".join(temp)
   # return ""
   
'''Generate a list which hold all children of the current state
   and return the list'''
def generate_children(state): #   '''your code goes here'''
   arr = []
   blank = state.index("_")
   if blank<6:
      arr.append(swap(state, blank, blank+3))
   if blank>2:
      arr.append(swap(state, blank, blank-3))
   if blank!=0 and blank!=3 and blank!=6:
      arr.append(swap(state, blank, blank-1))
   if blank!=2 and blank!=5 and blank!=8:
      arr.append(swap(state, blank, blank+1))
   return arr
   
def display_path(n, explored): #key: current, value: parent
   l = []
   while explored[n] != "s": #"s" is initial's parent
      l.append(n)
      n = explored[n]
   print ()
   l = l[::-1]
   for i in l:
      print (i[0:3], end = "   ")
   print ()
   for j in l:
      print (j[3:6], end = "   ")
   print()
   for k in l:
      print (k[6:9], end = "   ")
   print ("\n\nThe shortest path length is :", len(l))
   return ""

'''Find the shortest path to the goal state "_12345678" and
   returns the path by calling display_path() function to print all steps.
   You can make other helper methods, but you must use dictionary for explored.'''
def BFS(initial_state):
   goal = "_12345678"
   Q = [initial_state]
   explored = {initial_state:'s'}
   if len(Q)==0:
      return ()
   while len(Q)!=0:
      s = Q.pop(0)
      if (s==goal):
         return(display_path(s, explored))
      for a in generate_children(s):
         if a not in explored:
            Q.append(a)
            explored[a]=s
            # print("Q", Q)
            # print("Explored", explored)
   # '''Your code goes here'''
   return ("No solution")

'''Find the shortest path to the goal state "_12345678" and
   returns the path by calling display_path() function to print all steps.
   You can make other helper methods, but you must use dictionary for explored.'''
def DFS(initial):
   goal = "_12345678"
   Q = [initial]
   explored = {initial:'s'}
   if len(Q)==0:
      return ()
   while len(Q)!=0:
      s = Q.pop()
      if (s==goal):
         return(display_path(s, explored))
      for a in generate_children(s):
         if a not in explored:
            Q.append(a)
            explored[a]=s

   '''Your code goes here'''
   return ("No solution")


def main():
   initial = getInitialState()
   # initial = "_42135678" 
   print ("BFS start with:\n", initial[0:3], "\n", initial[3:6], "\n", initial[6:], "\n")
   print (BFS(initial))
   print ("DFS start with:\n", initial[0:3], "\n", initial[3:6], "\n", initial[6:], "\n")
   print (DFS(initial))

if __name__ == '__main__':
   main()
