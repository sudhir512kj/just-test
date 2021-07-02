class Solution:
    def containsNearbyDuplicate(self, nums, k):
        Map = {}
        for i in range(len(nums)):
            if nums[i] in Map and i - Map[nums[i]] <= k:
                return True
            else:
                Map[nums[i]] = i
        return False
        # d = {}
        # for k,v in enumerate(nums):
        #     if v in d and k - d[v] <= k:
        #         return True
        #     d[v] = k
        
        # return False

obj = Solution()
print(obj.containsNearbyDuplicate([0,1,2,3,4,0,0,7,8,9,10,11,12,0], 1))