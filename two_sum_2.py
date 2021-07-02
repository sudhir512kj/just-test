class Solution:
    def twoSum(self, numbers, target):
        i1 = 0
        for i in range(1,len(numbers)):
            if numbers[i]+numbers[i1] == target:
                return (i1+1, i+1)
            elif numbers[i]+numbers[i1] < target:
                i1 = i
obj = Solution()
print(obj.twoSum([2,3,4], 6))