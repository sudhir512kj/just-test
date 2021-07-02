class Solution:
    def largestOddNumber(self, num: str) -> str:
        Max = 0
        n = len(num)
        for i in range(n - 1, -1, -1):
            if int(num[i]) % 2 != 0:
                Max = num[:i+1]
                break
        return Max if Max else ""

obj = Solution()
print(obj.largestOddNumber("35427"))