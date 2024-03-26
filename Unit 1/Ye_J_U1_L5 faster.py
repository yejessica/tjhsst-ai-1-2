# Name: Jessica Ye
# Date: 10/4/21
import time

def generate_adjacents(current, words_set):
   ''' words_set is a set which has all words.
   By comparing current and words in the words_set,
   generate adjacents set of current and return it'''

   # TODO 1: adjacents
   adj_set = set()
   # print (words_set) 
   posWord = ""

   for c in "abcdefghijklmnopqrstuvwxyz":
      for i in range(len(current)):
         # print(current[:i]+c+current[i+1:])]
         
         posWord = current[:i]+c+current[i+1:]

         if (posWord in words_set and posWord != current):
            # print(posWord, "yes")
            adj_set.add(posWord)
   
   # print (adj_set)
   return adj_set

def check_adj(words_set):
   # This check method is written for words_6_longer.txt
   adj = generate_adjacents('listen', words_set)
   target =  {'listee', 'listel', 'litten', 'lister', 'listed'}
   return (adj == target)

def bi_bfs(start, goal, words_set):
   '''The idea of bi-directional search is to run two simultaneous searches--
   one forward from the initial state and the other backward from the goal--
   hoping that the two searches meet in the middle. 
   '''
   # TODO 2: Bi-directional BFS Search
   exploredFront, exploredBack = {start: 's'}, {goal: 's'}
   front, back = [start], [goal]
   # back = [goal]
   # if start == goal: return []
   # if len(front) == 0 or len(back) == 0:
   
   if len(front) == 0 or len(back) == 0:
      return()
   # while len(front) != 0 or len(back) != 0:
   while len(front) != 0 and len(back) != 0:
      frontPop = front.pop(0)

      # print (frontPop)
      backPop = back.pop(0)

      if (frontPop == goal):
         # return front #check??
         return display_path(frontPop, exploredFront, start, True)
      if (backPop == start):
         # return back[::-1]
         return display_path(backPop, exploredBack, goal, False)
      for f in generate_adjacents(frontPop, words_set):
         if f not in exploredFront:
            front.append(f)
            exploredFront[f] = frontPop
      for b in generate_adjacents(backPop, words_set):
         if b not in exploredBack:
            back.append(b)
            exploredBack[b] = backPop
   
   # return None
   return (["No Solution"], 0)

def display_path(n, explored, beg, front): #CHECK IF CORRECT!!
    l = []
   #  print(explored[n])
    while explored[n] != "s":
        l.append(n)
        n = explored[n]
    l.append(beg)

    if front:
    # print()
      l = l[::-1]

   #  print(l)
    return (l)


# def display_path2(n, explored, goal): #CHECK IF CORRECT!!
#     l = []
#     while explored[n] != "s":
#         l.append(n)
#         n = explored[n]
#     l.append(goal)
#     return (l)

def main():
   filename = input("Type the word file: ")
   words_set = set()
   file = open(filename, "r")
   for word in file.readlines():
      words_set.add(word.rstrip('\n'))
   # print ("Check generate_adjacents():", check_adj(words_set))
   # print(generate_adjacents("hornet", words_set))
   initial = input("Type the starting word: ")
   goal = input("Type the goal word: ")
   cur_time = time.time()
   path = (bi_bfs(initial, goal, words_set))
   if path != None:
      print (path)
      print ("The number of steps: ", len(path))
      print ("Duration: ", time.time() - cur_time)
   else:
      print ("There's no path")
 
if __name__ == '__main__':
   main()

'''
Sample output 1
Type the word file: words.txt
Type the starting word: listen
Type the goal word: beaker
['listen', 'listed', 'fisted', 'fitted', 'fitter', 'bitter', 'better', 'beater', 'beaker']
The number of steps:  9
Duration: 0.0

Sample output 2
Type the word file: words_6_longer.txt
Type the starting word: listen
Type the goal word: beaker
['listen', 'lister', 'bister', 'bitter', 'better', 'beater', 'beaker']
The number of steps:  7
Duration: 0.000997304916381836

Sample output 3
Type the word file: words_6_longer.txt
Type the starting word: vaguer
Type the goal word: drifts
['vaguer', 'vagues', 'values', 'valves', 'calves', 'cauves', 'cruves', 'cruses', 'crusts', 'crufts', 'crafts', 'drafts', 'drifts']
The number of steps:  13
Duration: 0.0408782958984375

Sample output 4
Type the word file: words_6_longer.txt
Type the starting word: klatch
Type the goal word: giggle
['klatch', 'clatch', 'clutch', 'clunch', 'glunch', 'gaunch', 'paunch', 'paunce', 'pawnce', 'pawnee', 'pawned', 'panned', 'panged', 'ranged', 'ragged', 'raggee', 'raggle', 'gaggle', 'giggle']
The number of steps:  19
Duration:  0.0867915153503418
'''

