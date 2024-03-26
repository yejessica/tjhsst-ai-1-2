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
#    print(csp)
   return csp


csp = sudoku_csp()

def sudoku_neighbors(csp_table):
    neighbors = {}
    for arr in csp_table:
        for num in arr:
            if num not in neighbors:
                neighbors[num] = arr
            else:
                neighbors[num] = neighbors.get(num) + arr
    # print (neighbors)

sudoku_neighbors(csp)


dictt = {1: [2,4,6,7,7], 2: [2,2,2,2,2], 3:[4,1]}
print(sorted(dictt, key = dictt.get))
print ( [2,2,2,2,2]<[4,1])