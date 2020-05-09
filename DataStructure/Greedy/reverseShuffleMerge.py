'''
Problem: Given a string, A, we define some operations on the string as follows:
    a. reverse(A) denotes the string obtained by reversing string A.
    b. shuffle(A) denotes any string that's a permutation of string A.
        Example: shuffle("god") E ['god', 'gdo', 'ogd', 'odg', 'dog', 'dgo']
    c. merge(A1, A2) denotes any string that's obtained by interspersing the two strings A1 & A2, 
       maintaining the order of characters in both. For example, A1 = "abc" & A2 = "def" , one 
       possible result of merge(A1, A2) could be 'abcdef', another could be 'abdecf', another could
       be 'adbecf'and so on.

    Given a string s such that s E merge(reverse(A), shuffle(A))for some string A, find the 
    lexicographically smallest A.

    For example, s = abab. We can split it into two strings of ab. The reverse is ba and we need to
    find a string to shuffle in to get abab. The middle two characters match our reverse string,
    leaving the a and b at the ends. Our shuffle string needs to be . Lexicographically ab < ba, so
    our answer is ab.

Function Description: Complete the reverseShuffleMerge function in the editor below. It must return
    the lexicographically smallest string fitting the criteria.
    reverseShuffleMerge has the following parameter(s):
        s: a string

Input Format: A single line containing the string s.

Constraints:    s contains only lower-case English letters, ascii[a-z]
                1 <= |s| <= 10000

Output Format: Find and return the string which is the lexicographically smallest valid A.
'''
from collections import Counter
import copy

def reverseShuffleMerge(s):
    # Total character counts in s
    ctr_s = Counter(s)
    
    # Character counts we need in our final string
    string_chars = { letter: count // 2 for letter, count in ctr_s.items() }
        
    # Character counts in the shuffled string 
    shuffled_chars = copy.deepcopy(string_chars)

    org_s = []

    # For lexicographical order
    for letter in reversed(s):
        print("Current letter:", letter)
        if string_chars[letter] > 0:
            # Maintianing lexicographical order basically
            # means that, if this char is smaller 
            # than the previous char, and the previous char 
            # still occurs in the chars of the shuffled string, 
            # we can the safely replace the previous char 
            # with this one. That's so because we should be 
            # able to still create a valid string which contains
            # both characters although the order will differs.
            while org_s and org_s[-1] > letter and shuffled_chars[org_s[-1]] > 0:
                print("Here with:", letter,"and",org_s)
                removed = org_s.pop()
                string_chars[removed] += 1
                shuffled_chars[removed] -= 1
                print("Inside while, org",string_chars)
                print("Inside while, shuffle",shuffled_chars)
            print("or Here with:", letter,"and",org_s)
            org_s.append(letter)
            string_chars[letter] -= 1
            print("outside while, org",string_chars)
            print("outside while, shuffle",shuffled_chars)
        else:
            shuffled_chars[letter] -= 1
            print("else part, shuffle",shuffled_chars)

    return ''.join(org_s)

'''
def reverseShuffleMerge(s):
    # If S = A + A, then S should have double of everything in A
    c_s = Counter(s)
    a = ''.join([letter*(num//2) for letter, num in c_s.items()])
    return a
'''

if __name__ == "__main__":
    with open('input.txt') as in_f:
        s = in_f.readline()
    
    print(reverseShuffleMerge(s))