'''Code for 6.11.3
A palindrome is a word that is spelled the same backward and forward, like 
“noon” and “redivider”. Recursively, a word is a palindrome if the first and 
last letters are the same and the middle is a palindrome.

The following are functions that take a string argument and return the first, 
last, and middle letters:

def first(word):
    return word[0]

def last(word):
    return word[-1]

def middle(word):
    return word[1:-1]
We’ll see how they work in Chapter 8.

Type these functions into a file named palindrome.py and test them out. 
What happens if you call middle with a string with two letters? One letter? 
What about the empty string, which is written '' and contains no letters?

Write a function called is_palindrome that takes a string argument and returns 
True if it is a palindrome and False otherwise. 
Remember that you can use the built-in function len to check the length of a 
string.

Solution: http://thinkpython2.com/code/palindrome_soln.py.'''

def first(word):
    return word[0]

def last(word):
    return word[-1]

def middle(word):
    return word[1:-1]


def is_palindrome(s):
    '''Evaluate a word'''
    if len(s) <= 1:
        return True
    elif first(s) != last(s):
        return False
    return is_palindrome(middle(s))