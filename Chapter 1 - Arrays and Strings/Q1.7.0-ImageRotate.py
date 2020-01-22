"""Given an image  represented by an NxN matrix where
each pixel in the image is 4 bytes. Write a method to rotate the image
in 90 degrees. Can you do this in place"""
"""
    [0, 1]    ->     [1, 0]
    [1, 0]    ->     [0, 1]
"""
def transposeMatrix(image):
    counter = 0
    for i in range(0, len(image)):
        for j in range(counter,len(image)):
            image[i][j], image[j][i] = image[j][i], image[i][j]
        counter += 1
    return image

def reverseRows(image):
    startIterator = 0
    EndIterator = len(image) - 1
    while(startIterator != EndIterator and startIterator < EndIterator):
        image[startIterator], image[EndIterator] = image[EndI
        terator], image[startIterator]
        startIterator += 1
        EndIterator -= 1
    return image

imageEven = [[1, 2, 3, 4],
            [5, 6, 7, 8],
            [9, 10, 11, 12],
            [13, 14, 15, 16]]

imageOdd = [[0, 1, 1],
            [1, 0, 0],
            [0, 1, 0]]

#Examples of inputs for the function
print ("Even Matrix")
for i in imageEven:
    print (i)
print ("Matrix rotated 90 degrees clock-wise")
transposeMatrix(imageEven)
for i in imageEven:
    reverseRows(i)
    print (i)

print ("Odd Matrix")
for i in imageOdd:
    print (i)
print ("Matrix rotated 90 degrees clock-wise")
transposeMatrix(imageOdd)
for i in imageOdd:
    reverseRows(i)
    print (i)
