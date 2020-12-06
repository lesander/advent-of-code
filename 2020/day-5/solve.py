#!/bin/python

def parse_input(path):
	boarding_passes = []
	with open(path, "r") as f:
		lines = f.read()

	for boarding_pass in lines.split("\n"):
		if len(boarding_pass) > 0:
			boarding_passes.append(boarding_pass)
	return boarding_passes

def chop(range, char):
	# binary chop time!
	divided = int(len(range) / 2)
	char_type = None

	if char == 'B' or char == 'R':
		# higher, so return upper part unless too small
		if len(range) > 2:
			return range[divided:]
		else:
			return range[1]

	elif char == 'F' or char == 'L':
		# lower, so return that part, unless too small
		if len(range) > 2:
			return range[:divided]
		else:
			return range[0]

	raise Exception(f'could not chop {range} {char}')

def find_seat(seat_ids):
	for i in range(len(seat_ids)):
		if seat_ids[i] + 1 != seat_ids[i+1]:
			return seat_ids[i] + 1

def naughty():
	boarding_passes = parse_input('input.txt')
	print(boarding_passes)
	seat_ids = []

	for boarding_pass in boarding_passes:
		cols = range(8)
		rows = range(128)

		boarding_pass_rows = list(boarding_pass)[:7]
		boarding_pass_cols = list(boarding_pass)[7:]

		for char in boarding_pass_rows:
			rows = chop(rows, char)

		for char in boarding_pass_cols:
			cols = chop(cols, char)

		seat_id = rows * 8 + cols
		print(f'{boarding_pass}: row {rows}, col {cols}, seat ID {seat_id}')
		seat_ids.append(seat_id)

	print(f"Highest found seat ID is {str(max(seat_ids))}")
	our_seat = find_seat(sorted(seat_ids))
	print(f"Our seat ID is {our_seat}")

def nice():
	pass

naughty()
