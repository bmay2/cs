import random
A = [[random.choice([0,0,0,0,0,1,1]) for col in range(25)] for row in range(25)]
for row in A:
	print(row)

def dfs(maze, row=0, col=0):
	if row not in range(0, len(maze)) or col not in range(0, len(maze)) or maze[row][col] != 0:
		return False
	if row == len(maze)-1 and col == len(maze)-1:
		return True
	old = maze[row][col]
	maze[row][col] = 1
	if dfs(maze, row, col+1) or dfs(maze, row+1, col) or dfs(maze, row, col-1) or dfs(maze, row-1, col):
		return True
	return False

print(dfs(A))