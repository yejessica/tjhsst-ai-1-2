#Name: Jessica Ye
#Date: 12/3/2021
import random

icosahedronNums = [8,7,14,13,9,0,1,2,6,5,15,16,12,11,10,19,3,4,17,18]

neighbors = {}

rowone = icosahedronNums[:5]
rowTwo = icosahedronNums[5:15]
rowtwoodd = rowTwo[::2]
rowtwoeven = rowTwo[1:][::2]
# print(rowtwoeven)
for i in range(5):
    if (i+1) > 4:
        neighbors[rowone[i]] = [rowone[0], rowone[i-1], rowtwoeven[i]]
    else:
        neighbors[rowone[i]] = [rowone[i+1], rowone[i-1], rowtwoeven[i]]

rowthree = icosahedronNums[15:]
# print(rowthree)
for i in range(5):
    if (i+1) > 4:
        neighbors[rowthree[i]] = [rowthree[0], rowthree[i-1], rowtwoodd[i]]
    else:
        neighbors[rowthree[i]] = [rowthree[i+1], rowthree[i-1], rowtwoodd[i]]
counter = 0
for i in range(10):
    if i%2 == 0:
        neighbors[rowTwo[i]] = [rowTwo[i+1], rowTwo[i-1], rowthree[counter]]
    if i%2 == 1:
        if (i+1) > 9:
            neighbors[rowTwo[i]] = [rowTwo[0], rowTwo[i-1], rowone[counter]]
        else:
            neighbors[rowTwo[i]] = [rowTwo[i+1], rowTwo[i-1], rowone[counter]]
        counter+=1

# print (neighbors)
# listOfSets = []
# possibleVals = neighbors
posColors = ["A", "B", "C", "D"]

def check_complete(assignment):
    if len(assignment.keys()) == 20:
        return True
    else:

        return False

def solve(neighbors, posColors):
    recursive_backtracking({}, neighbors, posColors)

def recursive_backtracking(assignment, neighbors, posColors):
    # if check_complete(assignment):
    #     return assignment
    if len(assignment.keys()) == 20:
        return assignment
    assignmentKeys = list(assignment.keys())
    neighborsKeys = list(neighbors.keys())
    posVals = [x for x in neighborsKeys if x not in assignmentKeys]
    variable = posVals[random.randint(0, len(posVals)-1)]
    neighborColors = [assignment[i] for i in neighbors[variable] if i in assignment]
    # for i in neighbors(variable):
    #     if i in assignment:
    #         neighborColors.append(assignment[i])
    for value in posColors:
        if value not in neighborColors:
            assignment[variable] = value
            
            result = recursive_backtracking(assignment, neighbors, posColors)

            if result!=None: 
                # print(result)
                setA = [i for i in assignment.keys() if assignment[i]=='A']
                setB = [i for i in assignment.keys() if assignment[i]=='B']
                setC = [i for i in assignment.keys() if assignment[i]=='C']
                maxlen = max([setA, setB, setC], key=len)
                print(maxlen)
                return maxlen
                # return result
                
solve(neighbors, posColors)