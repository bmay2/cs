import random
A = [[random.choice([0,0,0,0,0,1,1]) for col in range(25)] for row in range(25)]
for row in A:
	print(row)

def bfs(maze):
	to_visit = []
	if len(maze) > 0 and len(maze[0]) > 0 and maze[0][0] == 0:
		to_visit.append([0,0])
	while to_visit:
		node = to_visit.pop(0)
		row, col = node[0], node[1]
		if row < 0 or row >= len(maze) or col < 0 or col >= len(maze[0]) or maze[row][col] != 0:
			continue
		if row == len(maze)-1 and col == len(maze[0])-1:
			return True
		to_visit.append([row-1,col])
		to_visit.append([row,col+1])
		to_visit.append([row+1,col])
		to_visit.append([row,col-1])
		maze[row][col] = 1
	return False
	
print(bfs(A))