# Name: Jessica Ye 
# Date: 9/26/21

import random

class HeapPriorityQueue():
   # copy your HeapPriorityQueue() from Lab3
    def __init__(self):
        self.queue = ["dummy"]  # we do not use index 0 for easy index calulation
        self.current = 1        # to make this object iterable

    def next(self):            # define what __next__ does
        if self.current >=len(self.queue):
            self.current = 1     # to restart iteration later
            raise StopIteration
        
        out = self.queue[self.current]
        self.current += 1
    
        return out

    def __iter__(self):
        return self

    __next__ = next

    def isEmpty(self):
        return len(self.queue) == 1    # b/c index 0 is dummy

    def swap(self, a, b):
        self.queue[a], self.queue[b] = self.queue[b], self.queue[a]

    # Add a value to the heap_pq
    def push(self, value):
      self.queue.append(value)
      self.heapUp(len(self.queue[1:])-1)

    # helper method for push      
    def heapUp(self, k):
      # while (k > 1 and self.queue[k][0] < self.queue[math.floor(k/2)][0]):
      #    self.swap(k, math.floor(k/2))
      #    k = math.floor(k/2)
      parent = (k//2)
      if (k > 1 and self.queue[k] < self.queue[(parent)]):
         self.swap(k, (parent))
         # k = math.floor(k/2)
         self.heapUp((parent))

      # bottom = k
      # while(bottom > 1):
      #    parent = math.floor(bottom / 2)
      #    if(self.queue[parent] > self.queue[bottom]):
      #       self.swap(parent, bottom)
      #       bottom = parent
         
      #    else:
      #       break
                
    # helper method for reheap and pop
    def heapDown(self, k, size):
      if (k > size or k*2 > size):
         return
      
      maxChild = k*2
      if (maxChild+1<=size and self.queue[maxChild] > self.queue[maxChild+1]):
         maxChild = maxChild+1
      if (self.queue[k] > self.queue[maxChild]):
         self.swap(k, maxChild)
         self.heapDown(maxChild, size)
    
    # remove the min value (root of the heap)
    # return the removed value            
    def pop(self):
      # Your code goes here
      self.swap(1, -1)
      returnedVal = self.queue.pop(-1)
      if len(self.queue)>2:
         self.heapDown(1, len(self.queue[1:]))
      
      return returnedVal

      # make the queue as a min-heap          
      # never used  
    def reheap(self):
        for i in range(1, len(self.queue[1:])+1):
            self.heapDown(i, len(self.queue[1:]))

    # remove a value at the given index (assume index 0 is the root)
    # return the removed value   
    # never used
    def remove(self, index):
        removedVal = self.queue[index+1]
        self.queue.pop(index+1)

        self.reheap()
        return removedVal
   
  

# This method is for testing. Do not change it.
def isHeap(heap, k):
   left, right = 2*k, 2*k+1
   if left == len(heap): return True
   elif len(heap) == right and heap[k] > heap[left]: return False
   elif right < len(heap): 
      if (heap[k] > heap[left] or heap[k] > heap[right]): return False
      else: return isHeap(heap, left) and isHeap(heap, right)
   return True
    
# This method is for testing. Do not change it.
def main():
        
   pq = HeapPriorityQueue()    # create a HeapPriorityQueue object
   
   print ("Check if dummy 0 is still dummy:", pq.queue[0])
   
   # assign random integers into the pq
   for i in range(20):
      t = random.randint(10, 99)
      print (t, end=" ")
      pq.push(t)
   
   print ()
   
   # print the pq which is a min-heap
   for x in pq:
      print (x, end=" ")
   print()
   
   # remove test
   print ("Index 4 is removed:", pq.remove(4))
   
   # check if pq is a min-heap
   for x in pq:
      print (x, end=" ")
   print("\nIs a min-heap?", isHeap(pq.queue, 1))
   
   temp = []
   while not pq.isEmpty():
      temp.append(pq.pop())
      print (temp[-1], end=" ")
   
   #TESTING:
   # print([type(i) for i in temp])
   print ("\nIn ascending order?", temp == sorted(temp))

if __name__ == '__main__':
   main()