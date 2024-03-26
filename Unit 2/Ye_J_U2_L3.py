# Name: Jessica Ye
# Date: 11/15/21
import random
# variables1 = {}
def check_complete(assignment, csp_table):
   if assignment.find('.') != -1: return False
   for box in csp_table:
      if len(set([assignment[i] for i in box])) != 6: return False
   return True
   # return True
   
def select_unassigned_var(assignment, variables, csp_table):

   # t = []
   # for i in range(81):
   #    if assignment[i] == ".":
   #       t.append(i)
   # if len(t)>0:
   #    return t[random.randint(0, len(t)-1)]
   # else:
   #    return ""
   varKeys = list(variables.keys())
   if not varKeys:
      return None
   # return varKeys[random.randint(0, len(varKeys)-1)]]
   # varVals = list(variables.values())
   minNum = 10
   counter = 0
   for i in (varKeys):
      if len(variables[i]) < minNum:
         minNum = len(variables[i])
         counter = i
   return counter

def isValid(value, var_index, assignment, variables, csp_table):
   for box in csp_table:
      # print (triangle)
      if var_index in box:
         # print(triangle)
         for pos in box:
            if assignment[pos] == str(value) and pos!=var_index:
               return False

   return True

def ordered_domain(var_index, assignment, variables, csp_table):
   return []

def update_variables(value, var_index, assignment, variables, csp_table):
   variableKeys = list(variables.keys())
   
   for v in range(len(assignment)):
      # temp = variables[v]
      # for arr in csp_table:
      #    if v in arr:
      #       for elem in arr:
      #          if assignment[elem] in temp and elem!=v:
      #             # print(puzzle[elem])
      #             temp.remove(assignment[elem])
      if assignment[v] == ".":
         temp = ["1", "2","3","4","5","6","7","8", "9"]
         for arr in csp_table:
            if v in arr:
               for elem in arr:
                  if assignment[elem] in temp and elem!=v:
                     # print(puzzle[elem])
                     temp.remove(assignment[elem])
      # variables[c] = temp
         variables[v] = temp

      if assignment[v] != "." and v in variables:
         # print(variables[v])
         del variables[v]
         continue
   # print("Funct", variables)
   # print(assignment)
   # print(variables)
   return variables
         
   # return {}

   # return {}

def backtracking_search(puzzle, variables, csp_table): 
   # global variables1
   return recursive_backtracking(puzzle, variables, csp_table)

def recursive_backtracking(assignment, variables, csp_table):
   # global variables1
   # variables1 = variables
   if check_complete(assignment, csp_table) == True:
      return assignment
   var = select_unassigned_var(assignment, variables, csp_table)

   if var == None:
      return assignment
   # possibleVals = [1,2,3,4,5,6]

   for value in variables[var]:
      if isValid(value, var, assignment[:var] + str(value) + assignment[var+1:], variables, csp_table):
         assignment = assignment[:var] + str(value) + assignment[var+1:]
         variables1 = update_variables(value, var, assignment, variables, csp_table)
         # print(variables1)
         result = recursive_backtracking(assignment, variables1, csp_table)
         if result!=None:
            return result
         assignment = assignment[:var] + "." + assignment[var+1:]
   # return None
   return None

def display(solution):
   result = ""
   for i in range(len(solution)):
      result += solution[i] + " "
      if i % 9 == 2: result += "  "
      if i % 9 == 5: result += "  "
      if i % 9 == 8: 
         result += "\n"
         if (i//9)%3 == 2: result += "\n"
   # return ""
   return result

def sudoku_csp():
   csp = [[] for i in range(27)]
   colNum = 0
   rowNum = 0
   counter = 0
   for i in range(81):
      csp[i%9].append(i)
      csp[(i//9)+9].append(i)
      colNum = (i%9)//3
      rowNum = (i//9)//3
      if i==27: counter=2
      # print("counter", counter)
      if i==54: counter=4
      # print(colNum+rowNum+counter+18)
      boxNum = colNum+rowNum+counter+18
      csp[boxNum].append(i)
      
   # boxes = [[] for i in range(9)]
   # print(csp, len(csp))
   return csp

def initial_variables(puzzle, csp_table):
   variables = {}
   for c in range(len(puzzle)):
      if puzzle[c] == ".":
         temp = ["1", "2","3","4","5","6","7","8", "9"]
         for arr in csp_table:
            if c in arr:
               for elem in arr:
                  if puzzle[elem] != "." and puzzle[elem] in temp:
                     # print(puzzle[elem])
                     temp.remove(puzzle[elem])
         variables[c] = temp

      # print (variables)
   return variables
   # return {}
   
def main():
   puzzle = input("Type a 81-char string:") 
   while len(puzzle) != 81:
      print ("Invalid puzzle")
      puzzle = input("Type a 81-char string: ")
   csp_table = sudoku_csp()
   variables = initial_variables(puzzle, csp_table)
   print ("Initial:\n" + display(puzzle))
   solution = backtracking_search(puzzle, variables, csp_table)
   if solution != None: print ("solution\n" + display(solution))
   else: print ("No solution found.\n")
   
if __name__ == '__main__': main()
