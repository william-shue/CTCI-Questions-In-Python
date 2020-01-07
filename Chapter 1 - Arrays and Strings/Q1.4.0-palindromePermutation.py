'''
1.4
Palindrome Permutation: Given a string, write a function to check if it is a
permutation of a palindrome. A palindrome is a word or phrase that is the same
forwards and backwards. A permutation is a rearrangment of letters. The palindrome
does not need to me limited to just dictionary words.

EXAMPLE:
Input: Tact Coa
Output: True (premutations: "taco cat", "atco cta", etc.)
'''

def palindromePermutation(string):  
  hTable = {}
  for i in string:
    if i == ' ':
      continue
    if i in hTable:
      hTable[i] += 1
    else:
      hTable[i] = 1

  numOfOdd = 0
  for val in hTable:
    if hTable[val] % 2 != 0:
      numOfOdd += 1
    else:
      continue
    if numOfOdd > 1:
      return False
  return True

#some test cases
examples = ["taco cat", "atco cta", "a t c o c t a", "racecar",
"carrace", "abba", "abcba", "atco ctaz", "abcdefg"]
for s in examples:
    print(palindromePermutation(s))
