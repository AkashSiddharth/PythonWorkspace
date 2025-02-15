"""
An English text needs to be encrypted using the following encryption scheme.
First, the spaces are removed from the text. Let L be the length of this text.
Then, characters are written into a grid, whose rows and columns have the 
following constraints:
floor(√L) <= row <= column <= ceiling(√L)

Example
s = if man was meant to stay on the ground god would have given us roots.
After removing spaces, the string is 54 characters long. √54 is between 7
and 8,
so it is written in the form of a grid with 7 rows and 8 columns.

ifmanwas  
meanttos          
tayonthe  
groundgo  
dwouldha  
vegivenu  
sroots

Ensure that rows X columns >= L

If multiple grids satisfy the above conditions, choose the one with the 
minimum area, i.e. rows X columns.The encoded message is obtained by 
displaying the characters of each column, with a space between column texts.
The encoded message for the grid above is:
imtgdvs fearwer mayoogo anouuio ntnnlvt wttddes aohghn sseoau

Create a function to encode a message.

Function Description:
encryption has the following parameter(s):
 - string s: a string to encrypt

Returns:
 - string s: the encrypted string
Input Format:
 - One line of text, the string s

Constraints:
 - 1 <= Length ofs <= 81
 - s contains characters in the range ascii[a-z] and space, ascii(32).

Sample Input: haveaniceday
Sample Output 0: hae and via ecy
Explanation 0: 
 L = 12, √12 is between 3 and 4.
 Rewritten with 3 rows and 4 columns:
have
anic
eday

Sample Input 1: feedthedog    
Sample Output 1: fto ehg ee dd
Explanation 1:
 L = 10, √10 is between 3 and 4.
 Rewritten with 3 rows and 4 columns:
feed
thed
og

Sample Input 2: chillout
Sample Output 2: clu hlt io
Explanation 2:
 L = 8, √8 is between 2 and 3.
 Rewritten with 3 columns and 3 rows (2 * 3 = 6 < 8 so we have to use 3X3.)
chi
llo
ut
"""

import math
import os
import random
import re
import sys
import itertools

def get_dimensions(l: int) -> tuple:
    # Constraint: floor(√L) <= row <= column <= ceiling(√L)
    row_size = math.floor(l ** 0.5)
    col_size = math.ceil(l ** 0.5)

    while row_size * col_size < l and row_size <= col_size:
        row_size += 1
    
    return (row_size, col_size)

def strip_spaces(text: str) -> str:
    temp = re.findall("[\S]*", text)
    return ('').join(temp)

def encryption(s: str) -> str:
    text = strip_spaces(s)
    row, col = get_dimensions(len(text))
    text_field = list()

    print(row, col)

    # define a 2-D array of the dimension
    text_field = [[text[(i*col) + j] for j in range(col) if (i* col + j) < len(text)] for i in range(row)]
    print(text_field)

    # transpose
    t_text_field = list(itertools.zip_longest(*text_field, fillvalue = ''))
    print(t_text_field)

    enc_text = (' ').join(list(map(lambda x: ('').join(x), t_text_field)))

    return enc_text

if __name__ == "__main__":
    s = input()
    result = encryption(s)
    print(result)