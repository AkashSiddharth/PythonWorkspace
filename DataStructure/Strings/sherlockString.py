'''
Problem: Sherlock considers a string to be valid if all characters of the string appear the same number of times. It is also valid if he can
         remove just 1 character at 1 index in the string, and the remaining characters will occur the same number of times. Given a string
         s, determine if it is valid. If so, return YES, otherwise return NO.
         For example, if s = abc, it is a valid string because frequencies are {a: 1, b: 1, c: 1}. So is s = abcc because we can remove one
         c and have 1 of each character in the remaining string. If s = abccc however, the string is not valid as we can only remove 1 
         occurrence of c. That would leave character frequencies of {a: 1, b: 1, c: 2}.

    Function Description: Complete the isValid function in the editor below. It should return either the string YES or the string NO.
        isValid has the following parameter(s):
            s: a string

    Input Format: A single string s.

    Constraints:    1 <= |s| <= 10^5
                    Each character s[i] E ascii[a - z]

    Output Format: Print YES if string s is valid, otherwise, print NO.
'''
from collections import Counter

def isValid(s):
    # print (Counter(s))
    ctr_occurances = Counter(Counter(s).values())
    # print(ctr_occurances)
    ctr_size = len(ctr_occurances)

    # Invalid Case: If keys are more than 2, means that there are more frequencies to handle
    if ctr_size > 2:  
        return 'NO'
    # Default Valid case: If there is one frequency, then the string is already valid
    elif ctr_size == 1:
        return 'YES'
    # General Case: If there are 2 keys, then either are difference between frequencies must be 1
    # and one frequecy must be 1
    else: 
        return 'YES' if ((sum(ctr_occurances.keys()) % 2 == 1) or (ctr_occurances[1] == 1)) and (1 in ctr_occurances.values()) else 'NO'

if __name__ == "__main__":
    print(isValid(input().strip()))