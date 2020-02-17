'''3.4 Queue via Stacks: Implement a MyQueue
   class which implementes a queue using two stacks'''

'''I'll be using a python list as I can treat it as a stack.
   The essence of this solution is that we use a stacks LIFO nature
   to fill a second stack which in turn reverses the order ultimately accessing elements'''

class MyQueue:
  #constructor for the the MyQueue class
   def __init__(self, stackNewest, stackOldest):
        self.stackNewest = stackNewest;
        self.stackOldest = stackOldest;

   def size(self):
    return len(self.stackNewest) + len(self.stackOldest)

   #push new values onto our 'queue'
   #push to 'stackNewest' as it will contain newest items on top
   #becuase this is python our 'push' is 'append'
   def add(self, newValue):
     self.stackNewest.append(newValue)

   def shiftStacks(self):
     if not self.stackOldest: #if stackOldest is empty
       while(self.stackNewest): #while stack newest is not empty
        #keep popping values off stackNewest and pushing to stackOldest
        self.stackOldest.append(self.stackNewest.pop())

   def peek(self):
   #call the shiftStacks method to make sure the 'correct element' is peeked at
     self.shiftStacks() #don't forget your '()' next time!
     return self.stackOldest[-1]

   def remove(self):
     self.shiftStacks()
     return self.stackOldest.pop()

#use examples

elems = ['a', 'b', 'c', 'd', 'e']
#stackA = []

# for i in elems:
#   stackA.append(i)

# for i in range(len(stackA)):
#   print(stackA.pop()) #observe the output is in LIFO stack order

#now using our new queue made of stacks . . .

stackB = elems
stackC = []

myQueueObject = MyQueue(stackB, stackC)
print("peek: ", myQueueObject.peek())
print("size: ", myQueueObject.size())

for i in range(myQueueObject.size()):
  print("remove: ", myQueueObject.remove())

myQueueObject.add(1)
myQueueObject.add(2)
myQueueObject.add(3)
print()

for i in range(myQueueObject.size()):
  print("remove: ", myQueueObject.remove())
