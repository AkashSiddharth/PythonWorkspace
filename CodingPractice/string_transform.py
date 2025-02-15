"""
###
Tranform a sentence based on the following rules
For each word in the sentence:
- first character remains unchanged
- for any character X in the word:
    - if the preceeding character Y comes after X in the alphabets then transform Y to Upper
    - if the preceeding character Y comes before X in the alphabets then transform Y to lower
    - if the preceeding character Y is the same as X then do nothing
###
"""

#!/bin/python3
import math
import os
import random
import re
import sys

#
# Complete the 'transformSentence' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING sentence as parameter.
#
def apply_rules(s: str) -> str:
    transformed = ''
    
    # Iterate over the characters:
    for index,character in enumerate(s):
        if index == 0:
            transformed += character
        else:
            # Get the ascii value of the current character
            x = ord(s[index].upper())
            
            # Get the ascii value of the preceeding character
            y = ord(s[index-1].upper())
            
            # If x (s [i]) comes after y (s[i-1])
            if x > y:
                transformed += character.upper()
            # If x (s [i]) comes before y (s[i-1])
            elif x < y:
                transformed += character.lower()
            # If x (s [i]) is the same as y (s[i-1])
            elif x == y:
                transformed += character

    return transformed

def transformSentence(sentence: str) -> str:
    return (' ').join(map(apply_rules,sentence.split(' ')))

if __name__ == '__main__':
    sentence = input()
    result = transformSentence(sentence)
    print(result)
