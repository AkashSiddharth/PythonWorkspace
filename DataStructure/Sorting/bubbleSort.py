'''
Problem: Consider the following version of Bubble Sort:
                for (int i = 0; i < n; i++) {
                    for (int j = 0; j < n - 1; j++) {
                        // Swap adjacent elements if they are in decreasing order
                        if (a[j] > a[j + 1]) {
                            swap(a[j], a[j + 1]);
                        }
                    }  
                }
        Given an array of integers, sort the array in ascending order using the Bubble Sort algorithm above. Once sorted, print the
        following three lines:
            1. Array is sorted in numSwaps swaps., where numSwaps is the number of swaps that took place.
            2. First Element: firstElement, where firstElement is the first element in the sorted array.
            3. Last Element: lastElement, where lastElement is the last element in the sorted array.

        Hint: To complete this challenge, you must add a variable that keeps a running tally of all swaps that occur during execution.
        For example, given a worst-case but small array to sort: a = [6, 4, 1] we go through the following steps:
            swap    a       
            0       [6,4,1]
            1       [4,6,1]
            2       [4,1,6]
            3       [1,4,6]
        It took 3 swaps to sort the array. Output would be
            Array is sorted in 3 swaps.  
            First Element: 1  
            Last Element: 6 

    Function Description: Complete the function countSwaps in the editor below. It should print the three lines required, then return.
        countSwaps has the following parameter(s):
            --> a: an array of integers .

    Input Format:   The first line contains an integer, n, the size of the array a.
                    The second line contains n space-separated integers a[i].

    Constraints:    2 <= n <= 600
                    1 <= a[i] <= 2 x 10^6

    Output Format: You must print the following three lines of output:
        1. Array is sorted in numSwaps swaps., where numSwaps is the number of swaps that took place.
        2. First Element: firstElement, where firstElement is the first element in the sorted array.
        3. Last Element: lastElement, where lastElement is the last element in the sorted array.
'''
def countSwaps(arr):
    swap = 0

    for i in range(len(arr)):
        for j in range(len(arr) - 1):
            if arr[j] > arr[j + 1]:
                swap += 1
                temp = arr[j]
                arr[j] = arr[j+1]
                arr[j+1] = temp
    
    print("Array is sorted in", swap,"swaps.")
    print("First Element:", arr[0])
    print("Last Element:", arr[len(arr) - 1])

if __name__ == "__main__":
    size = int(input())
    arr = list(map(int, input().split()))

    countSwaps(arr)    