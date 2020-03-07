'''
Problem: A string is said to be a special string if either of two conditions is met:
            --> All of the characters are the same, e.g. aaa.
            --> All characters except the middle one are the same, e.g. aadaa.
         A special substring is any substring of a string which meets one of those criteria. Given a string, determine how many special
         substrings can be formed from it.
         For example, given the string s = mnonopoo, we have the following special substrings:
            {m, n, o, n, o, p, o, o, non, ono, opo, oo}.

    Function Description: Complete the substrCount function in the editor below. It should return an integer representing the number of
         special substrings that can be formed from the given string.
         substrCount has the following parameter(s):
            n: an integer, the length of string s   
            s: a string

    Input Format:   The first line contains an integer, n, the length of s.
                    The second line contains the string s.

    Constraints:    1 <= n <= 10^6
                    Each character of the string is a lowercase alphabet, ascii[a-z].

    Output Format: Print a single line containing the count of total special substrings.
'''
# O(n) pass over the string
def substrCount(n, s):
    print(s)

    spl_sbstr = n
    prev = ''
    register = 0
    for i, current in enumerate(s):
        if i and (current != prev) :
            # it could be the central character
            # so we check the next characters as per the length of the register
            ## First add the subtrings that could be formed from the array in register
            if register > 1:
                spl_sbstr += (register * (register - 1)) // 2
            
            ## Check the next character moving backwards in the register
            ## assign j to the next character in s
            j = 1
            while (i-j) >= 0 and j <= register and (i+j) < n:
                # each iteration will increase the pattern to x.x to xx.xx and so on
                if s[i-j] == prev == s[i+j]:
                    # increase the count
                    spl_sbstr += 1
                    j += 1
                else:
                    # end of the x.x pattern, break the loop
                    break
            # Elements do not match, reset the register to 1 for the current character
            register = 1
        else:
            # If the characters match, increment counter
            register += 1

        # Reassign temp
        prev = current

    # At the end of the for-loop if the register value is more than 1, then increment spl_sbstr
    if register > 1:
        spl_sbstr += (register * (register - 1)) // 2

    return spl_sbstr

'''
# High time complexity
def substrCount(n, s):
    # Create an array with all possible substrings:
    spl_sbstr = [s[i:j] for i in range(n) for j in range(i+2,n+1) if s[i:j] == s[i:j][-1::-1]]
    print(spl_sbstr)

    return n + len(spl_sbstr)
'''

if __name__ == "__main__":
    with open('input.txt') as in_f:
        length = int(in_f.readline())
        in_string = in_f.readline().strip()

    print(substrCount(length, in_string))
    