"""Kelsey"""

name = input("Please enter name: ")
if len(name) < 1:
	print("Invalid name.")
print(name[::2])
