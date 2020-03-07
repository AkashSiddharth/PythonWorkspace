'''
Problem: You are given a string containing characters A and B only. Your task is to change it into a string such that there are no matching
         adjacent characters. To do this, you are allowed to delete zero or more characters in the string.
         Your task is to find the minimum number of required deletions.
         For example, given the string s = AABAAB, remove an A at positions 0 and 3 to make s = ABAB in 2 deletions.

    Function Description: Complete the alternatingCharacters function in the editor below. It must return an integer representing the
        minimum number of deletions to make the alternating string.
        alternatingCharacters has the following parameter(s):
            s: a string

    Input Format:   The first line contains an integer q, the number of queries.
                    The next q lines each contain a string s.

    Constraints:    1 <= q <= 10
                    1 <= |s| <= 10^5
                    Each string s will consist only of characters A and B

    Output Format: For each query, print the minimum number of deletions required on a new line. 
'''
def alternatingCharacters(s):
    count = 0

    for i in range(len(s)-1):
        if s[i] == s[i+1]:
            count += 1
    return count

if __name__ == "__main__":
    with open('input.txt') as in_file:
        queries = next(in_file)
        for line in in_file:
            print(alternatingCharacters(line.strip()))