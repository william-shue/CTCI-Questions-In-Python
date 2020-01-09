'''Zero Matrix: Write an algorithm such that if an element in a MxN matrix is 0, its entire row and column are set to 0.

ex.)    a = [[1,1,1],         [[0,1,1],
             [1,1,1],   ->     [0,1,1]
             [1,1,1],          [0,1,1],
             [0,1,1]]          [0,0,0]]           '''


a = [[1,1,1],
     [1,1,1],
     [1,1,1],
     [1,0,1]]

b = [[1,1,1,1],
     [1,1,1,1],
     [1,1,1,0]]

'''find any of the zeros in the matrix'''
def findZeros(inArr):
  #note this is not a n^2 for loop despite the double nesting
  #as it is only assessing each value in the matrix once
  zeroCoord = []
  for x in range(len(inArr)):
    tempRow = inArr[x]
    for y, count in enumerate(tempRow):
      if count == 0:
        zeroCoord.append([x, y])

  for i in zeroCoord:
    #print(i[0])
    setZeros(inArr, i[0], i[1])
  #print(inArr[0][0])


'''zeros out the row and column the zero is found'''
def setZeros(Arr, row, column):
  #the hard one is setting the columns to zero
  for i, val in enumerate(Arr):
    Arr[i][column] = 0
  #now make all values in the row zero and we're done!
  #print(len(Arr[row]))
  for i in range(0, len(Arr[row])):
    Arr[row][i] = 0



findZeros(a)
print(a)

findZeros(b)
print(b)
