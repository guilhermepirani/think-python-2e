'''Code for 9.2.1
Write a program that reads words.txt and prints only 
the words with more than 20 characters (not counting whitespace). '''

words = open('words.txt')

for word in words:
	if len(word) > 20:
		print(word)

words.close()