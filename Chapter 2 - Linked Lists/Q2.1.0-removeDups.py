'''2.1 Remove Dups: Write code to remove duplicates from an unsorted linked list. FOLLOW UP
How would you solve this problem if a temporary buffer is not allowed'''

#will use the following def. of singly linked list
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

#recursive print just for fun!
#pass the head of a linked singly linked list to print
def printList(self):
  if self == None or self.val == None:
    print("None/Null")
    return None
  else:
    print(str(self.val) + " ->", end=" ")
    printList(self.next)

#is passed the previous node to the one being removed
def removeNode(self):
  if self.next == None:
    self.val = None
  elif self.next.next == None:
    self.next = None
  else:
    self.next = self.next.next

'''essentially each value is added to the hash
 table and if a value is already in the hash table,
  then it's a duplicate so it's removed'''
def removeDups(self):
  dups = {}

  dups[self.val] = True

  prev = self
  self = self.next #can skip the first one, cannot have duplicate
  while self != None:
    if self.val in dups:
      removeNode(prev)

    dups[self.val] = True
    self = self.next
    prev = prev.next #prev is always on behind


#quick example

A = ListNode(7)
B = ListNode(9)
C = ListNode(10)
D = ListNode(7)
E = ListNode(9)

A.next = B
B.next = C
C.next = D
D.next = E
E.next = None

printList(A)
removeDups(A)
printList(A)
