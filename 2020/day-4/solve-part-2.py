#!/bin/python
import re

def parse_input(path):
	passports = []
	with open(path, "r") as f:
		lines = f.read()

	for passport in lines.split("\n\n"):
		passport_dict = parse_passport(passport)
		passports.append(passport_dict)
	return passports

def parse_passport(p):
	p_dict = {}

	# replace newlines with a space
	p = p.replace("\n", " ").strip()

	# key value pairs are delimited by a space
	properties = p.split(" ")

	# a key precedes a value with a semicolon
	for property in properties:
		key = property.split(":")[0].strip()
		value = property.split(":")[1].strip()
		p_dict[key] = value

	return p_dict

def naughty():
	valid = 0
	passports = parse_input("input.txt")
	for p in passports:
		if has_required_fields(p) and fields_are_valid(p):
			valid += 1

	print(f"Got {str(valid)} valid passports.")
	return valid

def has_required_fields(p):
	valid_parts = 0
	required = ['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid']
	for r in required:
		if r in p:
			valid_parts += 1
	return valid_parts == len(required)

def fields_are_valid(p):
	valid_fields = 0
	for k in p:
		v = p[k]
		if k == 'byr' and len(v) == 4 and int(v) >= 1920 and int(v) <= 2002:
			valid_fields += 1
		elif k == 'iyr' and len(v) == 4 and int(v) >= 2010 and int(v) <= 2020:
			valid_fields += 1
		elif k == 'eyr' and len(v) == 4 and int(v) >= 2020 and int(v) <= 2030:
			valid_fields += 1
		elif k == 'hgt':
			length = int(v.replace('cm', '').replace('in', ''))
			if 'cm' in v and length >= 150 and length <= 193:
				valid_fields += 1
			elif 'in' in v and length >= 59 and length <= 76:
				valid_fields += 1
		elif k == 'hcl':
			if v[0] == '#' and re.match("^#[0-9a-f]{6}$", v):
				valid_fields += 1
		elif k == 'ecl':
			colors = ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']
			if v in colors:
				valid_fields += 1
		elif k == 'pid':
			if re.match("^[0-9]{9}$", v):
				valid_fields += 1

	return valid_fields == 7

def nice():
	pass

naughty()
