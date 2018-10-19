#!/usr/bin/env python
from random import choice,shuffle

#Text color Ascii representations.
Asciifg=['\033[3%dm'%i for i in range(1,8)]
Asciifg+=['\033[9%dm'%i for i in range(1,8)]
shuffle(Asciifg)
#print (Asciifg)
#Background color representations.
Asciibg=['\033[4%dm'%j for j in range(1,6)]
shuffle(Asciibg)
#print (Asciibg)
#default normal
Norm='\033[0m\n'

def colorfg(text):
    """Get Text and return a random colored text"""
    text=str(text)
    new_txt=''
    text=text.split('\n')
    for t in text:
        new_txt+=choice(Asciifg)+t+Norm
    return new_txt
def colorbg(text):
    """Get Text and return a random colored background."""
    text=str(text)
    new_text=''
    text=text.split('\n')
    for t in text:
        new_text+=choice(Asciibg)+t+Norm
    return new_txt
