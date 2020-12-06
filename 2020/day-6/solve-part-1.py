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
	combined_answers = []

	for group in forms:
		answers = []
		for person in group:
			for answer in person:
				if answer not in answers:
					answers.append(answer)
		print(f'Group {group} has {len(answers)} distinct answers.')
		combined_answers.append(answers)

	combined_sum = 0
	for group_answers in combined_answers:
		combined_sum += len(group_answers)
	print(f'Combined, the sum of all answers is {combined_sum}')

def nice():
	pass

naughty()
