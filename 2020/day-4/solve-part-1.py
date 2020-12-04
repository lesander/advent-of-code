#!/bin/python

def parse_input(path):
	passports = []
	with open(path, "r") as f:
		lines = f.read()

	for passport in lines.split("\n\n"):
		passports.append(passport)
	return passports

def naughty():
	valid = 0
	required = ['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid']
	passports = parse_input("input.txt")

	for p in passports:
		if has_required_fields(p):
			valid += 1

	print(f"Got {str(valid)} valid passports.")
	return valid

def has_required_fields(p):
	valid_parts = 0
	for r in required:
		if r in p:
			valid_parts += 1
	if valid_parts == len(required):
		print(f"valid: {p}")
		return True
	else:
		print(f"not valid: {p}")
		return False

def nice():
	pass

naughty()
