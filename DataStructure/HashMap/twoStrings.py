'''
Problem: Given two strings, determine if they share a common substring. A substring may be as small as one character.
        For example, the words "a", "and", "art" share the common substring a. The words "be" and "cat" do not share a substring.

    Function Description: Complete the function twoStrings in the editor below. It should return a string, either YES or NO based on 
        whether the strings share a common substring.
        twoStrings has the following parameter(s):
            --> s1, s2: two strings to analyze .

    Input Format: The first line contains a single integer p, the number of test cases.
        The following p pairs of lines are as follows:
            --> The first line contains string s1. 
            --> The second line contains string s2.

    Constraints:
        s1 and s2 consist of characters in the range ascii[a-z].
        1 <= p <= 10
        1 <= |s1|, |s2| <= 10^5

    Output Format: For each pair of strings, return YES or NO.
'''
from collections import Counter

if __name__ == "__main__":
    for _ in range(int(input())):
        s1, s2 = Counter(input().rstrip()), Counter(input().rstrip())
        diff = s2 - s1

        if sum(s2.values()) != sum(diff.values()):
            print("YES")
        else:
            print("NO")


