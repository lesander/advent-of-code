#!/bin/python

def parse_input(path):
	forms = []
	with open(path, "r") as f:
		lines = f.read()

	for group_raw in lines.split("\n\n"):
		group = []
		if len(group_raw.strip()) > 0:
			for person in group_raw.split("\n"):
				if len(person.strip()) > 0:
					group.append(person)
			forms.append(group)
	return forms

def naughty():
	forms = parse_input('input.txt')
	alphabet = 'abcdefghijklmnopqrstuvwxyz'
	answers_same = 0

	for group in forms:
		for letter in alphabet:
			everyone_with_letter = 0
			for person in group:
				if person.count(letter) > 0:
					everyone_with_letter += 1

			if everyone_with_letter == len(group):
				answers_same += 1

	print(f'Numer of questions everyone answered yes to sum: {answers_same}')

def nice():
	pass

naughty()
