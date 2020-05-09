'''
Problem: A string is said to be a child of a another string if it can be formed
         by deleting 0 or more characters from the other string. Given two 
         strings of equal length, what's the longest string that can be 
         constructed such that it is a child of both?
         For example, ABCD and ABDC have two children with maximum length 3, 
         ABC and ABD. They can be formed by eliminating either the D or C from 
         both strings. Note that we will not consider ABCD as a common child 
         because we can't rearrange characters and ABCD != ABDC.

    Function Description: Complete the commonChild function in the editor 
         below. It should return the longest string which is a common child of 
         the input strings.
         commonChild has the following parameter(s):
            s1, s2: two equal length strings

    Input Format: There is one line with two space-separated strings, s1 and s2.

    Constraints:    1 <= |s1|, |s2| <= 5000
                    All characters are upper case in the range ascii[A-Z].

    Output Format: Print the length of the longest string s, such that s is a 
         child of both s1 and s2. 
'''

'''def array_print(arr):
    for i in range(len(arr)):
        for j in range(len(arr[i])):
            print(arr[i][j], end = " ")
        print("")
'''

## LONGEST COMMON SUBSEQUENCE
## Space optimized dynamic programming implementation
## At any point in time we are only accessing 2 rows
def commonChild(s1, s2):
    # get the string lengths
    s1_len, s2_len = len(s1), len(s2)

    # Initialize a 2-D array of size s1_len X s2-len
    lcs = [ [None]*(s2_len+1) for _ in range(2)]
    bi = bool

    for i in range(s1_len + 1):
        # Calulate the binary index
        bi = i & 1
        v1 = s1[i-1]
        for j in range(s2_len + 1):
            v2 = s2[j-1]
            if i == 0 or j == 0:
                lcs[bi][j] = 0
            elif v1 == v2:
                lcs[bi][j] = lcs[1-bi][j-1] + 1
            else:
                # lcs[bi][j] = max(lcs[1-bi][j], lcs[bi][j-1])
                lcs[bi][j] = lcs[1-bi][j] if lcs[1-bi][j] > lcs[bi][j-1] else lcs[bi][j-1]

    return lcs[bi][s2_len]

## Dynamic Programming implementation
'''
def commonChild(s1, s2):
    # get the string lengths
    s1_len, s2_len = len(s1), len(s2)

    # Initialize a 2-D array of size s1_len X s2-len
    lcs = [ [None]*(s2_len+1) for _ in range(s1_len+1)]

    for i in range(s1_len + 1):
        for j in range(s2_len + 1):
            if i == 0 or j == 0:
                lcs[i][j] = 0
            elif s1[i-1] == s2[j-1]:
                lcs[i][j] = lcs[i-1][j-1] + 1
            else:
                lcs[i][j] = max(lcs[i-1][j], lcs[i][j-1])
        #array_print(lcs)
    
    return lcs[s1_len][s2_len]
'''

##  Naive recursive implementation (exponentional time complexity)
'''
def commonChild (s1, s2):
    if len(s1) == 0 or len(s2) == 0:
        return 0
    elif s1[-1] == s2[-1]:
        return 1 + commonChild(s1[:-1], s2[:-1])
    else:
        return max(commonChild(s1[:-1], s2), commonChild(s1, s2[:-1]))
'''

if __name__ == "__main__":
    with open("S:\\GitHub\\PythonWorkspace\\DataStructure\\Strings\\input.txt") as in_file:
        s1, s2 = in_file.readline().split()

    print(commonChild(s1, s2))