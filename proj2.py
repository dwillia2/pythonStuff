import random
import math


def every_other_character(input_str):
	output = ''
	for i in range(0, len(input_str)):
		if(i % 2 == 0):
			output += input_str[i]
	return output


def reverse_string(input_str):
	output = ''
	for i in range(len(input_str) - 1, -1, -1):
		output += str(input_str[i])
	return output


def is_palindrome(input_str):
	"""
	Empty string is vacuously true
	"""
	temp = len(input_str) - 1
	for i in range(int(len(input_str) / 2)):
		if input_str[i] != input_str[temp]:
			return False
		temp -= 1
	return True


def print_menu():
	print('1: every_other_character\n2:reverse_string\n3:is_palindrome\n4:Exit program')


while True:
	print_menu()
	choice = int(input('Make a selection:'))
	if choice == 1:
		input_str = input('Enter a string: ')
		print(every_other_character(input_str) + '\n')
	elif choice == 2:
		input_str = input('Enter a string: ')
		print(reverse_string(input_str) + '\n')
	elif choice == 3:
		input_str = input('Enter a string: ')
		boolean = is_palindrome(input_str)
		if boolean:
			print('That is a palindrome\n')
		else:
			print('That is not a palindrome\n')
	elif choice == 4:
		print('Thanks for using my program')
		break
	else:
		print('Improper input\n')