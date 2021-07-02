# Given an array of size n, containing random integers. It also contains some zeros. Move all the zeros in the end of the array.
array = [1,0,9,-1,3,4,4,0]
Ouyput = [1,9,-1,3,4,4,0,0]

def makeZerosend(array):
    index = 0
    n = len(array)
    for i in range(n):
        if array[i] != 0:
            array[index] = array[i]
            index += 1
    while index < n:
        array[index] = 0
        index += 1
    return array

res = makeZerosend(array)
print(res)
