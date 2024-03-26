import sys; args = sys.argv[1:]
# puzzles = open(args[0], "r").read().splitlines()
puzzles = open("puzzles.txt", "r").read().splitlines()
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
   # print(csp)
   # boxes = [[] for i in range(9)]
   # print(csp, len(csp))
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
   # variables = {}
   # for c in range(len(puzzle)):
   #    if puzzle[c] == ".":
   #       temp = ["1", "2","3","4","5","6","7","8", "9"]
   #       for n in neighbors[c]:
   #          if puzzle[n] != "." and puzzle[n] in temp and not len(temp) == 1:
   #             # print(puzzle[elem])
   #             temp.remove(puzzle[n])
   #       variables[c] = temp
   #    # print(variables)
   # return variables

   variables = {}
   for v in range(len(puzzle)):
      resultant = []
      if puzzle[v] == '.':
         temp = ["1", "2","3","4","5","6","7","8", "9"]
         # print(neighbors[v])
         subtractList = [puzzle[elem] for elem in neighbors[v]]
         resultant = list(set(temp) - set(subtractList)) + list(set(subtractList) - set(temp))
         if '.' in resultant: resultant.remove('.')
   
         variables[v] = (resultant)

   return variables

# Optional helper function
def initialize_ds(puzzle, neighbors): 
   return initial_variables(puzzle, neighbors), puzzle

# optional helper function
def select_unassigned_var(assignment, variables, neighbors): #done
   varKeys = list(variables.keys())
   # if len(varKeys) <= 1:
   #    return varKeys[0]
   # if not varKeys:
   #    return None
   # return varKeys[random.randint(0, len(varKeys)-1)]]
   # varVals = list(variables.values())
   # minNum = 10
   # counter = 0
   # for i in (varKeys):
   #    if len(variables[i]) < minNum:
   #       minNum = len(variables[i])
   #       counter = i
   # return counter
   # possibleVals = {}
   # for i in variables:
   #    if len(variables[i]) <= 1:
   #       return i
   #    possibleVals[i] = len(variables[i])
   possibleVals = dict((i, len(variables[i])) for i in varKeys)
   # print(possibleVals)
   minNum = min(possibleVals, key=possibleVals.get)
   # print(minNum)
   # minNum = min(list(variables.values()))
   return minNum

   # minNum = min(variables, key=variables.get)
   # print(minNum)
   # return minNum

   # neighborVals = dict((i, len(neighbors[i])) for i in varKeys)
   # minNum = min(neighborVals, key=neighborVals.get)
   # return minNum

   # neighborVals = dict((i, len(neighbors[i])) for i in varKeys)
   # minNum = max(neighborVals, key=neighborVals.get)
   # return minNum

def isValid(value, var_index, assignment, neighbors):
   # for neighbor in neighbors[var_index]:
   #    if assignment[neighbor] == value and neighbor!= var_index:
   #       return False
   # arr = [(assignment[n]==value and n!=var_index) for n in neighbors[var_index]]
   # print(arr)
   return True not in [(assignment[n]==value and n!=var_index) for n in neighbors[var_index]]
   # return True

# optional helper function
def update_variables(value, var_index, assignment, variables, neighbors): #done
   variables = {}
   for v in range(len(assignment)):
      resultant = []
      if assignment[v] == ".":
         temp = ["1", "2","3","4","5","6","7","8", "9"]
         # print(neighbors[v])
         subtractList = [assignment[elem] for elem in neighbors[v]]
         resultant = list(set(temp) - set(subtractList)) + list(set(subtractList) - set(temp))
         if '.' in resultant: resultant.remove('.')
     
         variables[v] = (resultant)

      # elif assignment[v] != "." and v in variables:
      #    # print(variables[v])
      #    del variables[v]
      #    continue

   return variables
      

def check_complete(assignment, csp_table):
   if assignment.find('.') != -1:
      return False
   for box in csp_table:
      if len(set([assignment[i] for i in box])) != 9: return False
   return True

def solve(puzzle, neighbors, csp_table):
   # initialize_ds function is optional helper function. You can change this part. 
   # variables, puzzle, q_table = initialize_ds(puzzle, neighbors)  # q_table is quantity table {'1': number of value '1' occurred, ...}
   variables, puzzle = initialize_ds(puzzle, neighbors)
   # print("neighbors", neighbors)
   return recursive_backtracking(puzzle, variables, neighbors, csp_table) #q_table is last blank if needed

# optional helper function: you are allowed to change it
def recursive_backtracking(assignment, variables, neighbors, csp_table):
   if not assignment.find('.') != -1: return assignment

   possibleVals = dict((i, len(variables[i])) for i in list(variables.keys()))
   var = min(possibleVals, key=possibleVals.get)

   # var = select_unassigned_var(assignment, variables, neighbors)

   for value in variables[var]:
      assignment = assignment[:var] + str(value) + assignment[var+1:]
      # isValid = True not in [(assignment[n]==value and n!=var) for n in neighbors[var]]
      # if isValid(value, var, assignment[:var] + str(value) + assignment[var+1:], neighbors):
      if True not in [(assignment[n]==value and n!=var) for n in neighbors[var]]:
         # assignment = assignment[:var] + str(value) + assignment[var+1:]
         
         variables1 = update_variables(value, var, assignment, variables, neighbors)
         result = recursive_backtracking(assignment, variables1, neighbors, csp_table)

         if result!=None:
            return result
         assignment = assignment[:var] + "." + assignment[var+1:]
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