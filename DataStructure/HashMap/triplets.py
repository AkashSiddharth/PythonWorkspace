'''
Problem: You are given an array and you need to find number of tripets of indices (i, j, k) such that the elements at those indices are in
         geometric progression for a given common ratio r and i < j < k.
         For example, arr = [1, 4, 16, 64]. If r = 4, we have [1, 4, 16] and [4, 16, 64] at indices (0, 1, 2) and (1, 2, 3).

    Function Description: Complete the countTriplets function in the editor below. It should return the number of triplets forming a
        geometric progression for a given r as an integer.
        countTriplets has the following parameter(s):
            --> arr: an array of integers
            --> r: an integer, the common ratio

    Input Format: The first line contains two space-separated integers n and r, the size of arr and the common ratio.
        The next line contains n space-seperated integers arr[i].

    Constraints:    1 <= n <= 10^5
                    1 <= r <= 10^9
                    1 <= arr[i] <= 10^9

    Output Format: Return the count of triplets that form a geometric progression.
'''

'''
# Getting Runtime error for large values
from itertools import combinations
def countTriplets(arr: list, r: int) -> int:
    # first make tuples of 3
    # Method 1: using combinations
    # triples = list(combinations(arr, 3))
    #print(triples)

    # Method 2 : using list comprehension
    arr_t = [(arr[i], arr[i+j+1], arr[i+j+k+1]) for i in range(len(arr)-2) for j in range(len(arr)-i-2) for k in range(1,(len(arr)-i-j-1 ))]
    #print(arr_t)

    # Filter the triples
    t_count = list(filter(lambda t: ((t[1] // t[0]) == (t[2] // t[1]) == r) and (t[0] <= t[1] <= t[2]), arr_t))
    return len(t_count)'''

'''
# using Counters
from collections import Counter

def countTriplets(arr, r):
    r2 = Counter()
    r3 = Counter()
    count = 0

    for v in arr:
        print(v)
        if v in r3:
            count += r3[v]
            print('Count increased', count)
        
        if v in r2:
            r3[v*r] += r2[v]
        
        r2[v*r] += 1
        print("r2:",r2)
        print("r3:",r3)

    return count
'''

# Using default dict
from collections import defaultdict

def countTriplets(arr, r):
    count = 0
    level2 = defaultdict(int) 
    level3 = defaultdict(int)

    for elem in arr:
        count += level3[elem]
        level3[elem * r] += level2[elem]
        #print("Level3:", level3)
        level2[elem * r] += 1
        #print("Level2:", level2)

    return count 

if __name__ == "__main__":
    # Accept the input from command line
    #size, r = [*map(int, input().strip().split())]
    #arr = [*map(int, input().strip().split())]

    # Accept the input from file
    with open('input.txt') as in_file:
        size, r = [*map(int, in_file.readline().strip().split())]
        arr = [*map(int, in_file.readline().strip().split())]

    # print("size:",size, "common ratio:", r)
    print("Some part of the array:", arr[0:100])

    print(countTriplets(arr, r))
