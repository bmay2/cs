import random

# greatest index of number <= target
def floor(nums, target):
	lo = 0
	hi = len(nums)-1
	floor = -1
	while lo <= hi:
		mid = int(lo+(hi-lo)/2)
		if nums[mid] <= target:
			floor = mid
			lo = mid+1
		else:
			hi = mid-1
	if nums[floor] != target:
		return -1
	return floor

A = [random.randrange(10) for x in range(50)]
A.sort()
t = random.randint(0,10)

print(floor(A, t))