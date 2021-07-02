a = b = c = 0
count = 0
result = 0
for i in range(len(nums) + 1):
	if i == len(nums) or nums[i] == 0:
		if count == 0:
			result = max(result, i - a)
		else:
			result = max(c - a, i - b, result)
			count = 0
		a = b = c = i + 1
	elif nums[i] < 0:
		count ^= 1
		if a == b:
			b = i + 1
		c = i
return result