'''
Problem: Consider an array of integers, a = [a[0], a[1], ..., a[n-1]]. We define the absolute difference between two elements, a[i] and
         a[j] (where i != j), to be the absolute value of a[i] - a[j].
         Given an array of integers, find and print the minimum absolute difference between any two elements in the array. For example, 
         given the array arr = [-2, 2, 4] we can create 3 pairs of numbers: [-2,2], [2,4] and [-2, 4]. The absolute differences for these
         pairs are |(-2) - 2| = 4, |(-2) - 4| = 6 and |2 - 4| = 2. The minimum absolute difference is 2.

    Function Description: Complete the minimumAbsoluteDifference function in the editor below. It should return an integer that 
        represents the minimum absolute difference between any pair of elements.
        minimumAbsoluteDifference has the following parameter(s):
            n: an integer that represents the length of arr
            arr: an array of integers

    Input Format:   The first line contains a single integer n, the size of arr.
                    The second line contains n space-separated integers arr[i].

    Constraints:    2 <= n <= 10^5
                    -10^9 <= arr[i] <= 10^9 

    Output Format: Print the minimum absolute difference between any two elements in the array.
''' 
import numpy as np

def minimumAbsoluteDifference(n, arr):
    minabsdiff = 99999999

    arr = np.sort(arr)

    for i in range(0,n-1):
        diff = abs(arr[i] - arr[i+1])
        minabsdiff = diff if diff < minabsdiff else minabsdiff
    
    return minabsdiff

if __name__ == "__main__":
    # get the input
    with open('input.txt') as in_f:
        size = int(in_f.readline())
        arr = list(map(int, in_f.readline().split()))
    
    print(minimumAbsoluteDifference(size, arr))