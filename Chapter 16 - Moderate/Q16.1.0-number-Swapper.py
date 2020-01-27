'''16.1 Number Swapper: Write a function to swap a number in place
(that is, without temporary variables).'''

#here's a simple way to do it arithmetically
def numberSwapper(a,  b):
  a = a - b #'store' 'b' in 'a' via subtraction
  b = b + a #assign 'b' the correct value by adding 'a' to it
  a = b - a #assign 'a' by getting the difference from 'b - a'
  return a, b

valueA = 123
valueB = 3215
print("valueA : %2d, valueB : %2d" %(valueA, valueB))
valueA, valueB = numberSwapper(valueA,  valueB)
print("valueA : %2d, valueB : %2d \n" %(valueA, valueB))


arr = [123, 0, 3215]
print(arr)
#python also supports operations like this one liner swap
arr[0], arr[2] = arr[2], arr[0]
print(arr, "\n")
'''but unless they're performing the above swap method 'under the hood'
it doesn't gaurentee no temp. variables, so the above can be applied
arithmetic to an array like so'''

def numberSwapperArray(array, i, j):
    array[i] = array[i] - array[j]
    array[j] = array[j] + array[i]
    array[i] = array[j] - array[i]

#working example
arr2 = [765, 0, 432]
print(arr2)
numberSwapperArray(arr2, 0, 2)
print(arr2)
