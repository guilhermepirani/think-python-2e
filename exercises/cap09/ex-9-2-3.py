'''Code for 9.2.3

Write a function named avoids that takes a word and a string of forbidden letters,
and that returns True if the word doesn’t use any of the forbidden letters.

Write a program that prompts the user to enter a string of forbidden letters
and then prints the number of words that don’t contain any of them. 
Can you find a combination of 5 forbidden letters that excludes the smallest number of words?'''

def avoid(word, forb):
	'''Checks if word uses any of the forb letters'''
	for c in forb:
		if c in word:
			return False
	return True

u_input = '0'

while not u_input.isalpha():
	u_input = input('Enter a string of forbidden letters: ')

words = open('words.txt')

for word in words:
	if avoid(word, u_input):
		print(word)
