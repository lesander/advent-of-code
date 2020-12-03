#!/bin/python
# why be nice when you can be naughty?

def parse_input():
	passwords = []
	with open("input.txt", "r") as f:
		for line in f:
			line = line.strip()
			if len(line) == 0:
				continue
			parts = line.split(" ")
			min_occurrence = parts[0].split("-")[0]
			max_occurrence = parts[0].split("-")[1]
			character = parts[1].replace(":", "")
			password = parts[2]
			passwords.append({
				"requirements": {"min": int(min_occurrence), "max": int(max_occurrence)},
				"character": character,
				"password": password
			})
	return passwords

def naughty():
	passwords = parse_input()
	valid_passwords = 0
	for p in passwords:
		print(p)
		password = p["password"]
		min = p["requirements"]["min"]
		max = p["requirements"]["max"]
		char = p["character"]
		occurrences = password.count(char)
		if occurrences >= min and occurrences <= max:
			valid_passwords += 1
	return valid_passwords

def nice():
	pass

print(f"{naughty()} valid passwords")
