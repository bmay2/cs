import random

def last(nums, target):
	lo = 0
	hi = len(nums)-1
	last = -1
	while lo <= hi:
		mid = int(lo+(hi-lo)/2)
		if nums[mid] < target:
			lo = mid+1
		elif nums[mid] == target:
			last = mid
			lo = mid+1
		else:
			hi = mid-1
	if nums[last] != target:
		return -1
	return last

A = [random.randrange(6) for x in range(10)]
A.sort()
t = random.randint(0,5)

print(A)
print(t)
print(last(A, t))