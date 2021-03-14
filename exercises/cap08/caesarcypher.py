'''Asks user to input a word and a key and then return the word encripted by 
given key in caesar cypher'''

from string import ascii_lowercase

def ceasar_cypher(letter, key):
    '''rotates the alphabet by given key'''
    if letter.isupper():
        first = ord('A')
    elif letter.islower():
        first = ord('a')
    else:
        return letter

    pos = ord(letter) - first
    new_pos = (pos + key) % 26 + first
    return chr(new_pos)

def rotate_word(word, key):
    """Cyphers word by given key"""
    cypher = ""
    for letter in word:
        cypher += ceasar_cypher(letter, key)
    return cypher


# Prompts user for word and key
word = ''
key = 0

while len(word) <= 0:
	word = input('Enter a word: ')

while key <= 0:
	key = input('Enter a number key: ')
	if key in ascii_lowercase:
		key = 0
	else:
		key = int(key)


# Cypher
print(rotate_word(word, key))
