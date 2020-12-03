#!/bin/python

def parse_input():
	grid = []
	with open("input.txt", "r") as f:
		for line in f:
			line = line.strip()
			if len(line) > 0:
				grid.append(line)
	return grid

def move(grid, movement, cur_pos):
	line_len = len(grid[0])

	# move to the right
	movement_x = movement[0]
	new_pos_x = cur_pos[0] + movement_x
	if new_pos_x >= line_len:
		# x would be out of bounds, so move to y+1 below.
		new_pos_y =+ 1
		# reset x to correct pos
		new_pos_x = new_pos_x - line_len #-1

	# move down
	movement_y = movement[1]
	new_pos_y = cur_pos[1] + movement_y

	if new_pos_y >= len(grid):
		# reached end
		return False
	if new_pos_x < 0 or new_pos_y < 0:
		raise Exception(f"Illegal position {str([new_pos_x, new_pos_y])}")
	return [new_pos_x, new_pos_y]

def see(grid, pos):
	x = pos[0]
	y = pos[1]
	visual = grid[y][x]
	if visual == "#":
		return 'tree'
	else:
		return 'empty'

def iter_loop(grid, movement):
	iters = 0
	trees = 0
	pos = [0,0]

	print(f"Starting iteration for movement {str(movement)}")

	while True:
		iters =+ 1
		print(f"Currently at {str(pos)}")
		pos = move(grid, movement, pos)
		print(f"Moving to {str(pos)}")
		if pos == False:
			print("Reached end of forrest!")
			break
		if see(grid, pos) == 'tree':
			print(f"There's a tree at {str(pos)}!")
			trees += 1
		if iters >= round(len(grid[0])/3)*len(grid):
			print(f"Should've reached the end by now (iters={iters})...")
			break

	print(f"We have seen {str(trees)} for movement type {str(movement)}")
	return trees

def naughty():
	grid = parse_input()

	movement_types = [
		[1,1],
		[3,1],
		[5,1],
		[7,1],
		[1,2]
	]

	tree_results = []

	for movement in movement_types:
		trees = iter_loop(grid, movement)
		tree_results.append(trees)

	tree_res = 1
	for t in tree_results:
		tree_res *= t

	print(f"Finished all movement types, results:")
	print(f"{str(tree_results)}")
	print(f"Multiplied together that makes {str(tree_res)}")

def nice():
	pass

naughty()
