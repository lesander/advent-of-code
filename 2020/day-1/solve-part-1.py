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
goal_sum = 2020

for num in nums:
	for s_num in nums:
		if num == s_num:
			continue
		sum = num + s_num
		if sum == goal_sum:
			prod = num * s_num
			print(f"Found solution: {num} + {s_num} = {sum}")
			print(f"{num} * {s_num} = {prod}")
