#! /usr/bin/env python

import numpy as np

array_1 = np.array([2,3,5])
array_2 = np.array([7,11,13])

array_1 + array_2

print(array_1 @ array_2)
print(array_1 + 2*array_2)


import nltk
from nltk.tokenize import sent_tokenize

sample_lyrics = '''
Call it how it is
Hendrix
I promise, I swear, I swear
You heard
Spit it
Yo

Percocets, molly, Percocets
Percocets, molly, Percocets
Rep the set, gotta rep the set
Chase a check, never chase a bitch
Mask on, fuck it, mask off
Mask on, fuck it, mask off
Percocets, molly, Percocets
Chase a check, never chase a bitch
Don't chase no bitches

Two cups, toast up with the gang
From food stamps to a whole 'nother domain
Out the bottom, I’m the livin' proof (Super)
They compromising, half a million on the Coupe
Drug houses, lookin' like Peru
Graduated, I was overdue
Pink molly, I can barely move
Ask about me, I’m gon' bust a move
Rick James, 33 chains
Ocean Ave., cruisin' Biscayne
Top off, that’s a liability
Hit the gas, boostin' my adrenaline
'''


print(sent_tokenize(sample_lyrics))


