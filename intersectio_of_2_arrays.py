from collections import Counter
class Solution:
    def intersect(self, nums1, nums2):
		# Counter(nums1) & Counter(nums2) gives the intersection of elemets and the number of times it occurs
		# .elements() returns an itertools.chain object which when wrapped by a list() method converts to a list
        return list((Counter(nums1)&Counter(nums2)).elements())

obj = Solution()
print(obj.intersect([4,9,5], [9,4,9,8,4]))