'''Code for 9.2.5

Write a function named uses_all that takes a word and a string of required letters,
and that returns True if the word uses all the required letters at least once.
 How many words are there that use all the vowels aeiou? How about aeiouy?'''

def uses_all(word, req):
	'''True if word has all required letters'''
	for c in req:
		if c in word:
			pass
		else:
			return False
	return True

# Iterates through word.txt using defined function to check each word for req letters.
u_input = '0'

while not u_input.isalpha():
	u_input = input('Enter a string of required letters: ')

words = open('words.txt')

count = 0
for word in words:
	if uses_all(word, u_input):
		count += 1
		print(word)

print(count)