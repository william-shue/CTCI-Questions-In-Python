'''
The Prompt:
Is Unique: Implement an algorithm to determine if a string has all unique characters.
What if you cannot use additional data strctures?
'''
#runs in O(n) time and C = 128 (our number of chars) O(C) space.
def isUniqueChars(str):
  if len(str) > 128: #under the expectation we're using 128 chracter ascii
    return False

  char_set = [False for value in range(128)]
  for i in range(len(str)):
    print(i)
    val = ord(str[i])
    if char_set[val]:
      return False
    char_set[val] = True
  return True

#some test examples:
examples = ["abcdefg", "abcdefg123", "ABCDEFG", "ABCDEFG123", "!@#", "aabcdefg", "abcdefg1233"
"ABCDDEFFG",
for s in examples:
    pritn(isUniqueChars(s))
