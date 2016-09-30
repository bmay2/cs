A = [6,5,4,3,2,1]
B = []
C = []

def move(n, current, target, aux):
	if n == 1:
		target.append(current.pop())
		return
	move(n-1, current, aux, target)
	move(1, current, target, aux)
	move(n-1, aux, target, current)

move(len(A), A, C, B)
print(A)
print(B)
print(C)