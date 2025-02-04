""" 
Case 1: Write a function that takes a string as a parameter and returns a new string 
that is the reverse of the old string.
"""

from concurrent.futures import process


def revStr(in_str: str) -> str:
  if len(in_str) <= 1:
    return in_str
  else:
    return in_str[-1] + revStr(in_str[:-1])

"""
Case 2: Write a function that takes a string as a parameter and returns True if 
the string is a palindrome, False otherwise. Remember that a string is a 
palindrome if it is spelled the same both forward and backward. For example: 
radar is a palindrome. for bonus points palindromes can also be phrases, but you
need to remove the spaces and punctuation before checking. 
for example: madam i’m adam is a palindrome. Other fun palindromes include:
    kayak
    aibohphobia
    Live not on evil
    Reviled did I live, said I, as evil I did deliver
    Go hang a salami; I’m a lasagna hog.
    Able was I ere I saw Elba
    Kanakanak – a town in Alaska
    Wassamassaw – a town in South Dakota
"""
def cleanStr(in_s : str) -> str:
  # import re
  # space_cleaned = in_s.replace(' ','')
  # cleaned_str = re.sub(r"[^a-zA-Z0-9]", "", in_s)

  cleaned_str = ''.join(filter(str.isalnum, in_s)) 
  return cleaned_str.lower()

def palidrome(in_str: str) -> bool:
  if len(in_str) <= 1:
    return True
  elif in_str[0] == in_str[-1]:
    return True & palidrome(in_str[1:-1])
  else:
    return False

if __name__ == "__main__":
  test = 'R'
  #print(test)
  #print(revStr(test))
  print(test)
  print(palidrome(cleanStr(test)))