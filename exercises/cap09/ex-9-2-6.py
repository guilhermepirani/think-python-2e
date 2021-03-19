'''Code for 9.2.6

Write a function called is_abecedarian
that returns True if the letters in a word appear
in alphabetical order (double letters are ok).
How many abecedarian words are there?'''

def is_abc(word):
	'''Check if word is in alphabetical order'''
	return word == ''.join(sorted(word))

f = open('words.txt')
count = 0

for line in f:
	line = line.strip()
	if is_abc(line):
		count += 1
		print(line)
		
print(count, 'abecedarian words')