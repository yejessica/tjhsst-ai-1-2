# Name: Jessica Ye
# Date: 11/10/21
import random
def check_complete(assignment, differences, variables):
    assignmentKeys=list(assignment.keys())
    differenceVals = list(differences.values())
    if not assignmentKeys:
        return False
    if len(assignmentKeys)!=len(variables):
        return False
    for i in differenceVals:
        # print("diffVals", differenceVals)
        if differenceVals.count(i) >1:
            return False

    return True
   
def select_unassigned_var(assignment, variables):

#    t = []
#    for i in range(len(variables)):
#       if variables[i] not in assignment:
#          t.append(variables[i])

#    return t[random.randint(0, len(t)-1)]
    return variables[random.randint(0, len(variables)-1)]
    # pass
   
def isValid(value, var_name, assignment, differences):
   """ your code goes here """
   assignmentKeys=list(assignment.keys())
   differenceVals = list(differences.values())

   for a in assignmentKeys:
       if a!=var_name:
           if assignment[a] == value: return False
           diff = abs(assignment[a]-value)
        #    print("dff", diff)
        #    print("diffdict", differences)
           if diff in differenceVals: return False #check if right

   return True

def backtracking_search(variables): 
   return recursive_backtracking({}, {}, variables)

def recursive_backtracking(assignment, differences, variables):
   """ your code goes here """
   if check_complete(assignment, differences, variables) == True: return assignment
   var = select_unassigned_var(assignment, variables)
   possibleVals = [0,1,2,3,4,5,6,7,8,9,10,11]

   for value in possibleVals:
      if isValid(value, var, assignment, differences):
        assignment[var] = value
        assignmentKeys = list(assignment.keys())
        # print(assignmentKeys)
        differences={}
        for i in range(len(assignmentKeys)):
            for j in range(i+1, len(assignmentKeys)):
                diff = abs(assignment[assignmentKeys[i]] - assignment[assignmentKeys[j]])
                differences[assignmentKeys[i]+assignmentKeys[j]] = diff
        # print(differences)
        # print("val", var)
        # print(assignment)
        result = recursive_backtracking(assignment, differences, variables)
        if result!=None:
            return result
        # print(assignmentKeys)
        del assignment[var]
        differenceKeys = list(differences.keys())
        for d in differenceKeys:
            if var in d:
                del differences[d]
        assignmentKeys.remove(var)
        
   return None


def main():
    variables = ["TA", "A", "B", "C", "D"]
    solution = backtracking_search(variables)
    print(solution)

if __name__ == '__main__':
   main()
   
