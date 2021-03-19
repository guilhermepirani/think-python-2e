'''Code for 9.7.7

This question is based on a Puzzler that was broadcast on the radio program Car Talk 
(http://www.cartalk.com/content/puzzlers):

Give me a word with three consecutive double letters. I’ll give you a couple of words
that almost qualify, but don’t. For example, the word committee, c-o-m-m-i-t-t-e-e. It
would be great except for the ‘i’ that sneaks in there. Or Mississippi: M-i-s-s-i-s-s-ip-p-i. 
If you could take out those i’s it would work. But there is a word that has three
consecutive pairs of letters and to the best of my knowledge this may be the only word.
Of course there are probably 500 more but I can only think of one. What is the word?
Write a program to find it. 

Solution: http://thinkpython2.com/code/cartalk1.py '''

def has_triple_double(word):
	'''Search word for three consecutive double letters'''
	i = 0
	count = 0

	while i < len(word) - 1:
		if word[i] == word[i + 1]:
			count += 1
			if count == 3:
				return True
			i += 2
		else: # Code by author
			i += 1 - 2 * count 
			count = 0

	return False

words = open('words.txt')

for line in words:
	word = line.strip()
	if has_triple_double(word):
		print(word)