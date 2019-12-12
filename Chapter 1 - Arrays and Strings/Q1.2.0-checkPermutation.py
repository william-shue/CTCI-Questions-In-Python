'''
Check Permutation: Given two strings, write a method to decide if one is a permutation of the other
'''

def checkPermutation(string1, string2):
  hTable = {}
  for i in string1:
    hTable[i] = True
  for j in string2:
    if j in hTable: 
      continue
    else: 
      return False
  return True

stringA = "abcdef"
stringB = "abcfed"

stringC = "abcdef"
stringD = "abcjed"

print(checkPermutation(stringA, stringB))
print(checkPermutation(stringC, stringD))

#note this is not one of the solutions from the book, however . . .
#this does run in O(n) runtime and O(n) space
