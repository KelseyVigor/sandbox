"""Kelsey"""

name = input("Please enter name: ")
if len(name) < 1:
	print("Invalid name.")
for char in range (0, len(name) + 1, 2):
	print(char, end = ' ')
print()