import sys; args = sys.argv[1:]
puzzles = open(args[0], "r").read().splitlines()
# puzzles = open("puzzles.txt", "r").read().splitlines()
import time

def sudoku_csp(n=9): #done
   csp = [[] for i in range(n*3)]
   colNum = 0
   rowNum = 0
   counter = 0
   for i in range(81):
      csp[i%n].append(i)
      csp[(i//n)+n].append(i)
      colNum = (i%n)//3
      rowNum = (i//n)//3
      if i==27: counter=2
      # print("counter", counter)
      if i==54: counter=4
      # print(colNum+rowNum+counter+18)
      boxNum = colNum+rowNum+counter+18
      csp[boxNum].append(i)
   return csp

def sudoku_neighbors(csp_table): # {0:[0, 1, 2, 3, 4, ...., 8, 9, 18, 27, 10, 11, 19, 20], 1:
   neighbors = {}
   for arr in csp_table:
      for num in arr:
         if num not in neighbors:
               neighbors[num] = arr
         else:
               neighbors[num] = list(set(neighbors.get(num) + arr))
   # print(neighbors)
   return neighbors

def initial_variables(puzzle, neighbors): #done

   variables = {}
   for v in range(len(puzzle)):
      resultant = []
      if puzzle[v] == '.':
         temp = ["1", "2","3","4","5","6","7","8", "9"]
         # print(neighbors[v])
         # subtractList = [puzzle[elem] for elem in neighbors[v]]
         # resultant = list(set(temp) - set(subtractList)) + list(set(subtractList) - set(temp))
         resultant = [x for x in temp if x not in [puzzle[elem] for elem in neighbors[v]]]
         if '.' in resultant: resultant.remove('.')
         if len(resultant) == 1:
            puzzle = puzzle[:v] + resultant[0] + puzzle[v+1:]
            continue
   
         variables[v] = (resultant)

   return variables, puzzle

# Optional helper function
def initialize_ds(puzzle, neighbors): 
   q_table = {'1':0,'2':0,'3':0,'4':0,'5':0,'6':0,'7':0,'8':0,'9':0}
   for c in puzzle:
      if c!='.': q_table[c] += 1

   vari, puzzles = initial_variables(puzzle, neighbors)
   # print(q_table)
   return vari, puzzles, q_table

# optional helper function
# def select_unassigned_var(assignment, variables, neighbors): #done
#    varKeys = list(variables.keys())
#    possibleVals = dict((i, len(variables[i])) for i in varKeys)
#    # print(possibleVals)
#    minNum = min(possibleVals, key=possibleVals.get)
#    # print(minNum)
#    # minNum = min(list(variables.values()))
#    return minNum

# def isValid(value, var_index, assignment, neighbors):

#    return True not in [(assignment[n]==value and n!=var_index) for n in neighbors[var_index]]


# optional helper function
def update_variables(value, var_index, assignment, variables, neighbors): #done
   # print(variables)
   '''
   variables = {}
   for v in range(len(assignment)):
      resultant = []

      if assignment[v] == ".":
         temp = ["1", "2","3","4","5","6","7","8", "9"]
         # print(neighbors[v])
         subtractList = [assignment[elem] for elem in neighbors[v]]
         # resultant = list(set(temp) - set(subtractList)) + list(set(subtractList) - set(temp))
         resultant = [x for x in temp if x not in subtractList]
         if '.' in resultant: resultant.remove('.')
     
         variables[v] = (resultant)
   '''
   assignment1 = assignment[:var_index] + str(value) + assignment[var_index+1:]
   valid = True not in [(assignment1[n]==value and n!=var_index) for n in neighbors[var_index]]
   if not valid:
      return {}, valid
   # variables1 = dict(variables)
   variables1 = {k:vals for k,vals in variables.items()}
   for v in range(len(assignment1)):
      if v in variables1 and assignment1[v] != '.': 
         del variables1[v]
      elif assignment1[v] == '.' and v in neighbors[var_index]:
         resultant = [x for x in variables1.get(v)]
         if value in resultant: 
            resultant.remove(value)
            variables1[v] = resultant

   
   return variables1, valid
      

# def check_complete(assignment, csp_table):
#    if assignment.find('.') != -1:
#       return False
#    for box in csp_table:
#       if len(set([assignment[i] for i in box])) != 9: return False
#    return True

def solve(puzzle, neighbors, csp_table):
   # initialize_ds function is optional helper function. You can change this part. 
   # variables, puzzle, q_table = initialize_ds(puzzle, neighbors)  # q_table is quantity table {'1': number of value '1' occurred, ...}
   variables, puzzle, q_table = initialize_ds(puzzle, neighbors)
   # print("neighbors", neighbors)
   return recursive_backtracking(puzzle, variables, neighbors, csp_table, q_table) #q_table is last blank if needed

# optional helper function: you are allowed to change it
def recursive_backtracking(assignment, variables, neighbors, csp_table, q_table):
   if assignment.find('.') == -1: 
      return assignment
   # if not variables:
   #    return assignment
   possibleVals = {i: len(variables[i]) for i in variables.keys()}
   # possibleVals = {}
   # check = False
   # for i in list(variables.keys()):
   #    if len(variables[i]) == 1:
   #       var = i
   #       check = True
   #       break
   #    possibleVals[i] = len(variables[i])

   # if not check: 
   var = min(possibleVals, key=possibleVals.get)
   
   q_tableCUT = {key:val for key, val in q_table.items() if val != 9}
   order = [val for val in variables[var] if val in sorted(q_tableCUT, key=q_tableCUT.get)[::-1]]

   for value in order:
      variables1, valid = update_variables(value, var, assignment, variables, neighbors)
      if valid:
         tempassignment = assignment[:var] + str(value) + assignment[var+1:]
         # assignment = assignment[:var] + str(value) + assignment[var+1:]
         
         q_table[value] += 1
         
         result = recursive_backtracking(tempassignment, variables1, neighbors, csp_table, q_table)

         if result!=None: 
            return result
         # assignment = assignment[:var] + "." + assignment[var+1:]
         else: q_table[value] -= 1
   return None

# sum of all ascii code of each char - (length of the solution * ascii code of min char)
def checksum(solution): #done
   # arr = [ord(c) for c in solution] 
   asciiSum = sum([ord(c) for c in solution]) - (len(solution)*ord(min(solution)))
   return asciiSum

def main():
   csp_table = sudoku_csp()   # rows, cols, and sub_blocks
   neighbors = sudoku_neighbors(csp_table)   # each position p has its neighbors {p:[positions in same row/col/subblock], ...}
   start_time = time.time()
   # print(solve("783294165.46137298912658347459763812861425739327981456234579681175846923698312574", neighbors, csp_table))
   # print(solve("48.3............71.2.......7.5....6....2.58.............1.76...3.....4......5....", neighbors, csp_table))
   for line, puzzle in enumerate(puzzles):
      line, puzzle = line+1, puzzle.rstrip()
      print ("{}: {}".format(line, puzzle)) 
      solution = solve(puzzle, neighbors, csp_table)
      if solution == None:print ("No solution found."); break
      print ("{}{} {}".format(" "*(len(str(line))+2), solution, checksum(solution)))
   print ("Duration:", (time.time() - start_time))

if __name__ == '__main__': main()
# Required comment: Your name, Period #, 2022
# Check the example below. You must change the line below before submission.
# Jessica Ye, Period 6, 2023