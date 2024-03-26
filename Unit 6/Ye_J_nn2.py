import sys; args = sys.argv[1:]
myFile = open(args[0], 'r')
import math, random

# t_funct is symbol of transfer functions: 'T1', 'T2', 'T3', or 'T4'
# input is a list of input (summation) values of the current layer
# returns a list of output values of the current layer
# def transfer(t_funct, input):
#    if t_funct == 'T3': return [1 / (1 + math.e**-x) for x in input]
#    elif t_funct == 'T4': return [-1+2/(1+math.e**-x) for x in input]
#    elif t_funct == 'T2': return [x if x > 0 else 0 for x in input]
#    else: return [x for x in input]
def transfer(t_funct, input):
    # pass
    if t_funct == "T1":
        return input
    elif t_funct == "T2":
        if input > 0.0:
            return input
        else:
            return 0.0
    elif t_funct == "T3":
        answer = 1/(1+math.exp(-1*input))
        return answer
    elif t_funct == "T4":
        answer = (2/(1+math.exp(-1*input))) - 1
        return answer
    else:
        pass
# returns a list of dot_product result. the len of the list == stage
# dot_product([x1, x2, x3], [w11, w21, w31, w12, w22, w32], 2) => [x1*w11 + x2*w21 + x3*w31, x1*w12, x2*w22, x3*w32] 
'''DONE'''
def dot_product(input, weights):
   # return [sum([input[x]*weights[x+s*len(input)] for x in range(len(input))]) for s in range(stage)]
   # print("myinput", input)
   # print("should be dot producting with", weights)
   a = sum([i*j for (i, j) in zip(input, weights)])

   # print(a)
   # print("my answer", a)
   return a

# Complete the whole forward feeding for one input(training) set
# return updated   x_vals and error of the one forward feeding
def ff(ts, xv, weights, t_funct, expected):

   '''DIFFERENT VARIABLE MEANINGS
   ts (original inputs) = testing set
   xv = the x_vals
   weights = the weights inputted
   t_funct = T1,T2,T3,T4 ETC
   '''
      
   #[[5.0, 8.0, 2.0, 0.0, 1.0, 2.0, 2.0, 2.0, 3.0, 7.0, 5.0, 4.0, 4.0, 3.0, 2.0], [0.0, 1.0, 7.0, 5.0, 4.0, 3.0], [0.5, -1.0]]
   # print (weights)

   count = 0

   finalAnswer = []

   while count < (len(weights)-1):
      splitStage = lambda weightsUsed, x: [weightsUsed[i:i+x] for i in range(0, len(weightsUsed), x)]
      dividedWeights = splitStage(weights[count], len(xv[count]))
      # print ("Divided Weights", dividedWeights)

      newInputs = []
      for i in range(len(dividedWeights)):
         # print("what are the input vals", xv[count])
         newInputs.append(transfer(t_funct, dot_product(xv[count], dividedWeights[i])))
         # print("newInputs",newInputs)
      
      xv.append(newInputs)
      
      # print("newInput_vals", xv)

      count+=1
 
   finalAnswer = []
   for i in range(len(weights[-1])):
      tempp = [weights[-1][i]]
      finalAnswer.append(dot_product([xv[-1][i]], tempp))

   xv.append(finalAnswer)
   # print(finalAnswer)
   # err = sum([(ts[-1-i] - xv[-1][i])**2 for i in range(len(xv[-1]))]) / 2
   # print(xv)
   err = sum([.5*(expected - xv[-1][i])**2 for i in range(len(xv[-1]))]) #ts[-1] contains the target value (either 0 or 1) and xv[-1] contains the final values
   # print(err)
   # if ts[-1] == 0:
   #    print("expected val 0", 0-xv[-1][0])
   # print(xv)
   
   return xv, err

# Complete the back propagation with one training set and corresponding x_vals and weights
# update E_vals (ev) and negative_grad, and then return those two lists
def bp(ts, xv, weights, negative_grad, expected):   

   ''' bp coding goes here '''
   # print(negative_grad)
   # negative_grad = [[] for x in xv]
   # print(ts)
   for i in range(len(xv)):
      tempi = int(-(i)-1)
      if i == 0:
         # print("hello xv", xv)
         negative_grad[-1] = [expected-xv[i-1][0]] #ts[-1] is the expected value - either 0 or 1
      elif i<len(xv)-1:
         negative_grad[tempi] = [weights[tempi+1][i]*xv[tempi][i]*(1-xv[tempi][i])*negative_grad[tempi+1][0] for i in range(len(xv[tempi]))]
      else:
         break 
   # print("xv", xv)
   # print('negative_grad', negative_grad)
   # print('weights', weights)
   # print('test', ts)
   return negative_grad

# update all weights and return the new weights
# Challenge: one line solution is possible
def update_weights(weights, xv, negative_grad, alpha):

   ''' update weights (modify NN) code goes here '''
   newWeights = [[] for i in weights]

   # print(negative_grad)
   for i in range(len(newWeights)):
      for j in range(len(xv[i+1])):
         # print("xv[j]", xv[i+1][j])
         # print(xv[i+1])
         # print("xv[i]", xv[i])
         newWeights[i].extend([negative_grad[i][j]*xv[i][x]*alpha+weights[i][x if j == 0 else x+len(weights[i])//len(xv[i+1])] for x in range(len(xv[i]))])
         # print(newWeights)        
 
   return newWeights

def main():
   t_funct = 'T3' # we default the transfer(activation) function as 1 / (1 + math.e**(-x))
   ''' work on training_set and layer_count '''
   # setWithSymbol = [[float(number) for number in i] for i in [section.split() for section in myFile.read().split('\n')]]
   training_set = [[float(number) for number in i if number!='=>'] for i in [section.split() for section in myFile.read().split('\n')]]
   expected = [training_set[k].pop() for k in range(len(training_set))]
   # print(training_set)
   for k in range(len(training_set)):
      training_set[k].append(1.0)
   # numberOfOutputs = len(setWithSymbol) - setWithSymbol.index('=>')
   # print (training_set) #[[1.0, -1.0, 1.0], [-1.0, 1.0, 1.0], [1.0, 1.0, 1.0], [-1.0, -1.0, 1.0], [0.0, 0.0, 0.0]]
   # graderlayer_counts = [len(training_set[0])-1, 2, 1, 1] 
   layer_counts = [len(training_set[0]), 2, 1, 1] # set the number of layers 
   # print ('layer counts', layer_counts) # This is the first output. [3, 2, 1, 1] with the given x_gate.txt

   ''' build NN: x nodes and weights '''
   x_vals = [[[i for i in temp]] for temp in training_set] # x_vals starts with first input values
   # print ("x_vals", x_vals) # [[[1.0, -1.0]], [[-1.0, 1.0]], [[1.0, 1.0]], [[-1.0, -1.0]], [[0.0, 0.0]]]
   # make the x value structure of the NN by putting bias and initial value 0s.
   # for i in range(len(training_set)):
   #    for j in range(len(layer_counts)):
   #       if j == 0: 
   #          '''THIS MIGHT NOT WORK, uncomment if it doesn't!!'''
   #          x_vals[i][j].append(training_set[i][-1])
            # x_vals[i][j].append(1.0)
         # else: x_vals[i].append([0 for temp in range(layer_counts[j])])
   # print ("with bias x_vals", x_vals) # [[[1.0, -1.0, 1.0], [0, 0], [0], [0]], [[-1.0, 1.0, 1.0], [0, 0], [0], [0]], ...
   x_valsBiasRef = [[[j for j in i] for i in x] for x in x_vals]
   # by using the layer counts, set initial weights [3, 2, 1, 1] => 3*2 + 2*1 + 1*1: Total 6, 2, and 1 weights are needed
   weights = [[round(random.uniform(-2.0, 2.0), 2) for j in range(layer_counts[i]*layer_counts[i+1])]  for i in range(len(layer_counts)-1)]
   # weights = [[0.3, -2, -1.5, 2, 0, 2], [0.3, -0.5], [-1]]
   #weights = [[1.35, -1.34, -1.66, -0.55, -0.9, -0.58, -1.0, 1.78], [-1.08, -0.7], [-0.6]]   #Example 2
   # print ("weights", weights)    #[[2.0274715389784507e-05, -3.9375970265443985, 2.4827119599531016, 0.00014994269071843774, -3.6634876683142332, -1.9655046461270405]
                        #[-3.7349985848630634, 3.5846029322774617]
                        #[2.98900741942973]]

   # build the structure of BP NN: E nodes and negative_gradients 
   # E_vals = [[*i] for i in x_vals]  #copy elements from x_vals, E_vals has the same structures with x_vals
   negative_grad = [[*i] for i in weights]  #copy elements from weights, negative gradients has the same structures with weights
   errors = [10]*len(training_set)  # Whenever FF is done once, error will be updated. Start with 10 (a big num)
   count = 1  # count how many times you trained the network, this can be used for index calc or for decision making of 'restart'
   alpha = 0.3 #try 0.19
   # print('ionitialized', negative_grad)
   # calculate the initail error sum. After each forward feeding (# of training sets), calculate the error and store at error list
   
   
   
   for k in range(len(training_set)):
      # print(k)
      x_vals[k], errors[k] = ff(training_set[k], x_vals[k], weights, t_funct, expected[k])
 
   err = sum(errors)
   ''' 
   while err is too big, reset all weights as random values and re-calculate the error sum.
   
   '''
   while err >= 0.01:
      while count < 2500:
         if count == 1000:
            alpha = alpha *.9
         # x_vals = [[x[0]] for x in x_valsBiasRef]
         # print("inloop", x_vals)
         for k in range(len(training_set)):
            
            
            # print(training_set[k])

            # x_vals[k], errors[k] = ff(training_set[k], x_vals[k], weights, t_funct)
            negative_grad = [[*i] for i in weights]

            negative_grad = bp(training_set[k], x_vals[k], weights, negative_grad, expected[k])
            # print(negative_grad)
            # errors[k] = 0
            # for j in negative_grad:
            #    errors[k] += sum(j)
            weights = update_weights(weights, x_vals[k], negative_grad, alpha)
            # print(weights)
            x_vals[k] = [i for i in x_valsBiasRef[k]]
            x_vals[k], errors[k] = ff(training_set[k], x_vals[k], weights, t_funct, expected[k])
            # print(weights)
            # print('okay')
         # print(errors)
         
         err = sum(errors)

         # print("err", err)
         count += 1
         # print(err)
         if err < 0.01:
            # print(errors)
            x_vals = [[[j for j in i] for i in x] for x in x_valsBiasRef]
         # print("inloop", x_vals)
            for k in range(len(training_set)):
               # print(k)
               # if k == 4:
               #    print('hi')
               x_vals[k], errors[k] = ff(training_set[k], x_vals[k], weights, t_funct, expected[k])

            # print(errors)
            err = sum(errors)
            # print(err)
            if err < 0.01: break
            else: 
               continue
            # break

      if err >= 0.01:
         weights = [[round(random.uniform(-2.0, 2.0), 2) for j in range(layer_counts[i]*layer_counts[i+1])]  for i in range(len(layer_counts)-1)]
         count = 0
   ''' 
   while err does not reach to the goal and count is not too big,
      update x_vals and errors by calling ff()
      whenever all training sets are forward fed, 
         check error sum and change alpha or reset weights if it's needed
      update E_vals and negative_grad by calling bp()
      update weights
      count++
   '''
   # raise ValueError(errors, weights, training_set)
   # print final weights of the working NN
   # print("hi")
   # print("Count:", count)
   # print("Errors:", ' '.join([str(x) for x in errors]))
   print ('Layercts:', ' '.join([str(x) for x in layer_counts]))
   print("Errors:", ' '.join([str(x) for x in errors]))
   # print("error total", err )
   print ('Weights:')
   for w in weights: print (' '.join([str(x) for x in w]))
if __name__ == '__main__': main()


#C:\Users\jessica\AppData\Local\Microsoft\WindowsApps\python.exe '.\nn_2_shell.py' x_gate.txt

#g:\My Drive\2021-22\Artificial Intelligence\Unit 6\nn_2_shell copy.py x_gate.txt

#python '.\Ye_J_nn2.py' 'x_gate.txt'
# Jessica Ye, 5, 2023