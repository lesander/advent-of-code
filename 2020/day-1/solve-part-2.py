#!/bin/python

def parse_input():
	nums = []
	with open("input.txt", "r") as f:
		for line in f:
			num = line.strip()
			if len(num) > 0:
				nums.append(int(num))
	return nums

nums = parse_input()

def naughty(goal_sum):

	for num_1 in nums:
		for num_2 in nums:
			for num_3 in nums:
				if len(list(set([num_1, num_2, num_3]))) != 3:
					continue
				sum = num_1 + num_2 + num_3
				if sum == goal_sum:
					prod = num_1 * num_2 * num_3
					print(f"Found solution: {num_1} + {num_2} + {num_3} = {sum}")
					print(f"{num_1} * {num_2} * {num_3} = {prod}")

def nice(goal_sum):
	# too lazy to implement own version of itertools,
	# too cheaty to use itertools directly..
	pass

# naughty or nice?
naughty(goal_sum=2020)
