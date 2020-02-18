'''
Problem: Lilah has a string, s, of lowercase English letters that she repeated infinitely many times. Given an integer, n, find and print
        the number of letter a's in the first n letters of Lilah's infinite string.
        For example, if the string s = 'abcac' and n = 10, the substring we consider is abcacabcac, the first characters of her infinite
        string. There are 4 occurrences of a in the substring.
    
    Function Description: Complete the repeatedString function in the editor below. It should return an integer representing the number of
        occurrences of a in the prefix of length n in the infinitely repeating string.
        repeatedString has the following parameter(s):
            - s: a string to repeat
            - n: the number of characters to consider
    
    Input Format: The first line contains a single string, s. The second line contains an integer, n.

    Constraints:
        --> 1 <= |s| <= 100
        --> 1 <= n  <= 10^12
        --> For 25% of the test cases, n <= 10^6.

    Output Format: Print a single integer denoting the number of letter a's in the first n letters of the infinite string created by 
        repeating s infinitely many times.
'''
def repeatedString(s: str, n: int ) -> int:
    # number of repitions of s in length n
    repitions: int = n // len(s)
    print("rep:",repitions)

    # partial characters of s, if any
    partial_rep: int = n % len(s)

    # Count the appearance of 'a' in s
    # Without function:
    '''for letter in s:
        if letter == 'a':
            count += 1'''
    # With function
    count: int = s.count('a')
    print("count:", count)

    # total number of appearance of 'a'
    appearance = (repitions * count) + s.count('a',0,partial_rep)
    print(appearance)

if __name__ == "__main__":
    # Get the input
    s, n = input().rstrip(), int(input().rstrip())

    repeatedString(s, n)