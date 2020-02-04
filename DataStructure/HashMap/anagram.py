'''
Problem: Two strings are anagrams of each other if the letters of one string can be rearranged to form the other string. Given a string, 
        find the number of pairs of substrings of the string that are anagrams of each other.
        For example s = mom, the list of all anagrammatic pairs is [m, m], [mo, om] at positions [[0], [2]], [[0, 1], [1, 2]] respectively.

    Function Description: Complete the function sherlockAndAnagrams in the editor below. It must return an integer that represents the 
        number of anagrammatic pairs of substrings in s.
        sherlockAndAnagrams has the following parameter(s):
            s: a string.

    Input Format: The first line contains an integer q, the number of queries.
        Each of the next q lines contains a string s to analyze.

    Constraints:    1 <= q <= 10
                    2 <= |s| <= 100
                    String s contains only lowercase letters E ascii[a-z].

    Output Format: For each query, return the number of unordered anagrammatic pairs. 
'''
# Apprach using Binomaial theorm, 'N choose 2' i.e. n!/ (2!*(n-2)!) = (n*(n-1)) / 2
# Here n is the windodw size

from collections import Counter

def sherlockAndAnagrams(s: str) -> int:
    anagrams = 0

    for i in range(1, len(s) + 1):
        a = [''.join(sorted(s[j:j+i])) for j in range(len(s)-i+1)]
        b = Counter(a)
        for ss in b:
            anagrams += b[ss] * (b[ss]-1) / 2
    return int(anagrams)

if __name__ == "__main__":
    # Accept the input
    for _ in range(int(input())):
        # get the string to search
        s = input().rstrip()

        print(sherlockAndAnagrams(s))