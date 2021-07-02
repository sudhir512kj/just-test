def sort(nums):
    temp = 0
    for i in range(len(nums)):
        minIndex = i
        for j in range(i, len(nums)):
           if (abs(nums[j]) < abs(nums[minIndex])):
              minIndex = j
           elif (abs(nums[j]) == abs(nums[minIndex])):
                 minIndex = j
        if (minIndex != i):
            temp = nums[minIndex]
            nums[minIndex] = nums[i]
            nums[i] = temp
    return nums

arr = [2,-7,-2,-2,0]
print(sort(arr))
