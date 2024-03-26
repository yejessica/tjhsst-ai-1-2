# Name: Jessica Ye
# Period: 5

from tkinter import *
from graphics import *
import random

def check_complete(assignment, vars, adjs):
   # check if assignment is complete or not. Goal_Test 
   ''' your code goes here '''
   assignmentKeys = list(assignment.keys())
   varsKeys = list(vars.keys())

   # print(assignmentKeys, varsKeys)
   if not assignmentKeys:
      return False
   if len(assignmentKeys) != len(varsKeys):
      return False
   for val in assignmentKeys:
      for a in adjs[val]:
         if assignment[val] == assignment[a]:
            return False
      
   return True

def select_unassigned_var(assignment, vars, adjs):
   # Select an unassigned variable - forward checking, MRV, or LCV
   # returns a variable
   ''' your code goes here '''

   varsKeys = list(vars.keys())
   returned = varsKeys[random.randint(0, len(varsKeys)-1)]
   # print(returned)
   return returned

   
def isValid(value, var, assignment, variables, adjs):
   # value is consistent with assignment
   # check adjacents to check 'var' is working or not.
   ''' your code goes here '''
   for a in adjs[var]:
      if a in assignment:
         if assignment[a] == value:
            return False
   return True

def backtracking_search(variables, adjs, shapes, frame): 
   return recursive_backtracking({}, variables, adjs, shapes, frame)

def recursive_backtracking(assignment, variables, adjs, shapes, frame):
   # Refer the pseudo code given in class.
   if check_complete(assignment, variables, adjs) == True: return assignment
   var = select_unassigned_var(assignment, variables, adjs)

   # print (var)

   for value in variables[var]:
      if isValid(value, var, assignment, variables, adjs):
         assignment[var] = value
         # print (value)
         draw_shape(shapes[var], frame, value)
         result = recursive_backtracking(assignment, variables, adjs, shapes, frame)
         if result!=None:
            return result
         del assignment[var]

   ''' your code goes here '''
   return None

# return shapes as {region:[points], ...} form
def read_shape(filename):
   infile = open(filename)
   region, points, shapes = "", [], {}
   for line in infile.readlines():
      line = line.strip()
      if line.isalpha():
         if region != "": shapes[region] = points
         region, points = line, []
      else:
         x, y = line.split(" ")
         points.append(Point(int(x), 300-int(y)))
   shapes[region] = points
   return shapes

# fill the shape
def draw_shape(points, frame, color):
   shape = Polygon(points)
   shape.setFill(color)
   shape.setOutline("black")
   shape.draw(frame)
   space = [x for x in range(9999999)] # give some pause
   
def main():
   regions, variables, adjacents  = [], {}, {}
   # Read mcNodes.txt and store all regions in regions list
   ''' your code goes here '''
   with open('mcNodes.txt','r') as f:
      for line in f:
         regions.append(line.strip())
   f.close()
   # Fill variables by using regions list -- no additional code for this part
   for r in regions: variables[r] = {'red', 'green', 'blue'}

   # Read mcEdges.txt and fill the adjacents. Edges are bi-directional.
   ''' your code goes here '''
   temp = []
   for r in regions:
      adjacents[r] = []
   # print (adjacents)
   with open('mcEdges.txt', 'r') as f:
      for line in f:
         first = line.strip().split()[0]
         second = line.strip().split()[1]
         
         temp = adjacents.get(first)
         # print(temp)
         temp.append(second)
         del adjacents[first]
         adjacents[first] = temp

         temp = adjacents.get(second)
         # print(temp)
         temp.append(first)
         del adjacents[second]
         adjacents[second] = temp
         
   # print (adjacents)
   # Set graphics -- no additional code for this part
   frame = GraphWin('Map', 300, 300)
   frame.setCoords(0, 0, 299, 299)
   shapes = read_shape("mcPoints.txt")
   for s, points in shapes.items():
      draw_shape(points, frame, 'white')
   # print (variables, adjacents)
   # solve the map coloring problem by using backtracking_search -- no additional code for this part  
   solution = backtracking_search(variables, adjacents, shapes, frame)
   print (solution)
   
   mainloop()

if __name__ == '__main__':
   main()
   
''' Sample output:
{'WA': 'red', 'NT': 'green', 'SA': 'blue', 'Q': 'red', 'NSW': 'green', 'V': 'red', 'T': 'red'}
By using graphics functions, visualize the map.
'''