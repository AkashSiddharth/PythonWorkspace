'''
Problem: Given an array of integers, find the subset of non-adjacent elements with the maximum sum.
         Calculate the sum of that subset.

    Function Description: Complete the maxSubsetSum function in the editor below. It should return 
        an integer representing the maximum subset sum for the given array.
        maxSubsetSum has the following parameter(s):
            arr: an array of integers

    Input Format:   The first line contains an integer, n.
                    The second line contains n space-separated integers arr[i].

    Constraints:    1 <= n <= 10^5
                    -10^4 <= arr[i] <= 10^4

    Output Format: Return the maximum sum described in the statement.
'''

# Dynammic Programming Solution
def maxSubsetSum(arr):
    incl = arr[0]
    excl = 0

    for num in arr[1:]:
        cur_incl = excl + num
        excl = max(incl, excl)
        incl = cur_incl
    
    return max(incl, excl)

'''
# Naive Recursive solution
def maxSubsetSum(arr):
    if len(arr) == 0:
        return 0
    else:
        return max(
            arr[-1] + maxSubsetSum(arr[:-2]), 
            maxSubsetSum(arr[:-1])
            )
'''

if __name__ == "__main__":
    with open('input.txt') as in_f:
        next(in_f)
        arr = list(map(int, in_f.readline().split()))

    print(maxSubsetSum(arr))