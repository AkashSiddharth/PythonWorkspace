'''
Problem: You can perform the following operations on the string, a:
         1. Capitalize zero or more of a's lowercase letters.
         2. Delete all of the remaining lowercase letters in q.

         Given two strings, a and b, determine if it's possible to make a equal to b as described.
         If so, print YES on a new line. Otherwise, print NO. 
         For example, given a = AbcDE and b = ABDE, in a we can convert b and delete c to match b.
         If a = AbcDE and b = AFDE, matching is not possible because letters may only be capital-
         ized or discarded, not changed.

    Function Description: Complete the function abbreviation in the editor below. It must return
         either YES or NO.
         abbreviation has the following parameter(s):
            a: the string to modify
            b: the string to match

    Input Format:   The first line contains a single integer q, the number of queries.
                    Each of the next q pairs of lines is as follows:
                        - The first line of each query contains a single string, a.
                        - The second line of each query contains a single string, b.

    Constraints:    --> 1 <= q <= 10
                    --> 1 <= |a|, |b| <= 1000
                    --> String a consists only of uppercase and lowercase English letters, 
                        ascii[A-Za-z].
                    --> String b consists only of uppercase English letters, ascii[A-Z].

    Output Format: For each query, print YES on a new line if it's possible to make string equal to
                    string . Otherwise, print NO.
'''
def print_array(arr):
    for i in range(len(arr)):
        print(arr[i])

# Dynamic Programming solution
def abbreviation(s1, s2):
    # calculates length 
    n = len(s1) 
    m = len(s2) 
    dp=([[False for i in range(m+1)] for i in range(n+1)]) 
      
    # mark 1st position as true  
    dp[0][0] = True
      
    # traverese for all DP i, j 
    for i in range(n): 
        for j in range(m+1): 
            # if possible for to convert i  
            # characters of s1 to j characters  
            # of s2 
            if (dp[i][j]):
                # if upper_case(s1[i])==s2[j]  
                # is same 
                if ((j < m and (s1[i].upper()== s2[j]))): 
                    dp[i + 1][j + 1] = True
                      
                # if not upper then deletion is  
                # possible 
                if not s1[i].isupper(): 
                    dp[i + 1][j] = True
    return 'YES' if (dp[n][m]) else 'NO' 

'''
# Naive recursive solution
def abbreviation(a, b):
    if len(b) == 0:
        return 'YES'
    elif (a[-1].isupper() and a[-1] != b[-1]) or len(a) == 0:
        return 'NO'
    else:
        if a[-1].upper() == b[-1]:
            return abbreviation(a[:-1], b[:-1])  
        else:
            return abbreviation(a[:-1], b)
'''

if __name__ == "__main__":
    with open('S:\\GitHub\\PythonWorkspace\\DataStructure\\DynamicProgramming\\input.txt') as in_f:
        queries = int(in_f.readline())
        for query in range(queries):
            str_a = in_f.readline().strip()
            str_b = in_f.readline().strip()

            print(abbreviation(str_a, str_b))