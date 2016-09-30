import random

def first(nums, target):
	lo = 0
	hi = len(nums)-1
	first = -1
	while lo <= hi:
		mid = int(lo+(hi-lo)/2)
		if nums[mid] < target:
			lo = mid+1
		elif nums[mid] == target:
			first = mid
			hi = mid-1
		else:
			hi = mid-1
	if nums[first] != target:
		return -1
	return first

A = [random.randrange(6) for x in range(10)]
A.sort()
t = random.randint(0,5)

print(A)
print(t)
print(first(A, t))