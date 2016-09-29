import random

# smallest index of number >= target
def ceiling(nums, target):
	lo = 0
	hi = len(nums)-1
	ceiling = -1
	while lo <= hi:
		mid = int(lo+(hi-lo)/2)
		if target <= nums[mid]:
			ceiling = mid
			hi = mid-1
		else:
			lo = mid+1
	if nums[ceiling] != target:
		return -1
	return ceiling

A = [random.randrange(10) for x in range(50)]
A.sort()
t = random.randint(0,10)

print(ceiling(A, t))