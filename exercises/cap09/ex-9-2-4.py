'''Code for 9.2.4

Write a function named uses_only that takes a word and a string of letters,
and that returns True if the word contains only letters in the list. 
Can you make a sentence using only the letters acefhlo? Other than “Hoe alfalfa”?'''

def uses_only(word, letters):
	'''checks if all letters from word are in given list'''
	for letter in word:
		if not letter in letters:
			return False

	return True
 			
 			
def check_input(u_input):
	'''Checks if all input is alpha'''
	while not u_input.isalpha():
		u_input = input('Enter only alphabetic characters: ')

	return u_input


word = check_input(input('Enter a word: '))
letters = check_input(input('Enter a sequence of letters: '))

if uses_only(word, letters):
	print('Word uses only letters in the list')
else:
	print('Word uses letters not in the list')