'''
Developer: Alper Kaan
Date: 07.02.2021
Purpose of Software: Reinforcement of learned Python Code and Self-improvement
'''
'''
what is wanted to be done?

Write a program that takes in two words as input and returns a list containing three elements, in the following order:

Shared letters between two words. Letters unique to word 1. Letters unique to word 2. 
Each element of the output should have unique letters, and should be alphabetically sorted. 
Useset operations. The strings will always be in lowercase and will not contain any punctuation.

Example:

Input1>>> "sharp"

Input2>>> "soap"

Output>>> ['aps', 'hr', 'o']
'''

word1 = set(input("Enter 1. Letter: "))
word2 = set(input("Enter 2. Letter: "))

intersection = list(word1 & word2) # intersection of two words
intersection.sort()
a = ''.join(intersection)

difference1 = list(word1 - word2) # letter difference of the first from the second
difference1.sort()
b = ''.join(difference1)

difference2 = list(word2 - word1) # letter difference of the second from the firs
difference2.sort()
c = ''.join(difference2)

my_list =[a,b,c]

print(my_list)


