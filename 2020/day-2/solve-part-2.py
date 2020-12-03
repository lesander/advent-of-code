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
			pos_1 = parts[0].split("-")[0]
			pos_2 = parts[0].split("-")[1]
			character = parts[1].replace(":", "")
			password = parts[2]
			passwords.append({
				"positions": [int(pos_1), int(pos_2)],
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
		pos_1 = p["positions"][0]
		pos_2 = p["positions"][1]
		char = p["character"]
		pass_pos_1 = password[pos_1-1]
		pass_pos_2 = password[pos_2-1]
		if (pass_pos_1 == char or pass_pos_2 == char) and not (pass_pos_1 == pass_pos_2):
			valid_passwords += 1
	return valid_passwords

def nice():
	pass

print(f"{naughty()} valid passwords")
