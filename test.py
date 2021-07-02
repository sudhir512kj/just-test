# You are given two sorted arrays. You have to find all pairs such that they sum to target x
# Example: array1: [-2, 0, 1,2,6,8, 9, 11]
# array2 = [-1, 0, 2, 3, 15, 18, 100]
# x= 0

def binarySearch(arr, high, low, num):
    if high >= low:
        mid = (high+low)//2
        if arr[mid] == num:
            return mid
        elif arr[mid] > num:
            return binarySearch(arr, mid-1, low, num)
        else:
            return binarySearch(arr, high, mid+1, num)
    else:
        return -1

array1 = [-2, 0, 1,2,6,8, 9, 11] #m
array2 = [-1, 0, 2, 3, 15, 18, 100] #n
x = int(input())
res = []
for a in array1:
    req = x - a
    if binarySearch(array2, len(array2)-1, 0, req) != -1:
        res.append((a,req))
print(res)
# O(mlogn)