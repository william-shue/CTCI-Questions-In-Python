'''Assume you have a method isSubstring which check if one word is a substring of another.
Given two string, s1 and s2, write code to check if s2 is a rotation of s1 using only one
call to isSubstring (eg. "waterbottle" is a rotation of "erbottlewat")'''

'''the programatinc solution to this problem may not be clear without an example.

Essentially, by the fact that the rotated string is just the string itself shifted in one
direction or the other, by contactenating it to itself, the rotation offset will naturally
align it to complete the entire word: 

"erbottlewat" + "erbottlewat" = "erbottlewaterbottlewat"

and as you can see "erbottle[waterbottle]wat" is naturally containted in the word by the nature described.'''

def isRotation(str1, str2):
  if (len(str1) == len(str2) and len(str1) != 0 and len(str2) != 0):
    newStr1 = str1 + str1
    return isSubstring(newStr1, str2)
  else:
    return False #there's no way they can be identical

def isSubstring(strA, strB):
  if strB in strA:
    return True
  else:
    return False

print(str(isRotation("erbottlewat", "waterbottle")))
