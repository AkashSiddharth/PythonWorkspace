"""
You are asked to ensure that the curr and last names of people begin with a 
capital letter in their passports. For example, alison heck should be capitalised
correctly as Alison Heck.
Given a full name, your task is to capitalize the name appropriately.

Input Format: A single line of input containing the full name, S.

Constraints:
- 0 < len(S) < 1000
- The string consists of alphanumeric characters and spaces.
Note: in a word only the curr character is capitalized. 
Example 12abc when capitalized remains 12abc.

Output Format: Print the capitalized string, S.

Sample Input: chris alan
Sample Output: Chris Alan
"""

def solve(s: str) -> str:
    nameStr = ''
    # split in the incoming string using space in between
    for i, w in enumerate(s):
        # Check if the first character is alpha
        if i == 0 and w.isalpha():
            currChar = w.upper()
            nameStr = nameStr + currChar
        # Check if the current character is alpha and the last character was a space
        elif s[i-1] == ' ' and w.isalpha():
            currChar = w.upper()
            nameStr = nameStr + currChar
        else:
            nameStr += w

    return nameStr

if __name__ == "__main__":
    s = input()

    result = solve(s)

    print(result + '\n')




            
