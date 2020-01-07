'''String Compression: Implement a method to perform
a basic string compression using the counts of repeated
characters. For example, the string aabcccccaaa would
become a2b1c5a3. If the "compressed" string could not
become smaller than the original string, your method
should return the original string. You can assume the
string has only uppercase and lowercase letters"'''

def stringCompression(strA):
  compString = strA[0]
  repeatCount = 1
  for i in range(1, len(strA)):
    if strA[i] != strA[i-1]:
      compString += str(repeatCount)
      compString += strA[i]
      repeatCount = 1
    else:
      repeatCount += 1

  return compString + str(repeatCount)


print(stringCompression("aabcccccaaa"))
