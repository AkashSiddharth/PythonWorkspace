'''
Problem: Given an array, A, of N integers, print each element in reverse order as a single line of space-separated integers.

    Input Format:   The first line contains an integer, N (the number of integers in A). 
                    The second line contains space-separated integers describing A.

    Constraints:    1 <= N <= 1000
                    1 <= A[i] <= 10000
    Output Format:  Print all N integers in A in reverse order as a single line of space-separated integers.
'''
def reverse(data):
    for i in range(len(data)-1, -1, -1):
        yield data[i]

_s, arr = int(input()), list(map(int, input().rstrip().split()))

for index in reverse(arr):
    print(index, end=' ')