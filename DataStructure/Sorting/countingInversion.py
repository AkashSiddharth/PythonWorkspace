'''
Problem: In an array, arr, the elements at indices i and j (where i < j) form an inversion if arr[i] > arr[j]. In other words, inverted
         elements arr[i] and arr[j] are considered to be "out of order". To correct an inversion, we can swap adjacent elements.
         For example, consider the dataset arr = [2,4,1]. It has two inversions: (4,1) and (2,1).
         Given d datasets, print the number of inversions that must be swapped to sort each dataset on a new line.

    Function Description: Complete the function countInversions in the editor below. It must return an integer representing the number of
         inversions required to sort the array.
         countInversions has the following parameter(s):
            arr: an array of integers to sort .

    Input Format:   The first line contains an integer, d, the number of datasets.
                    Each of the next d pairs of lines is as follows:
                    --> The first line contains an integer, n, the number of elements in arr.
                    --> The second line contains n space-separated integers, arr[i].

    Constraints:    1 <= d <= 15
                    1 <= n <= 10^5
                    1 <= arr[i] <= 10^7

    Output Format: For each of the d datasets, return the number of inversions that must be swapped to sort the dataset.
'''
def mergeArrays(arr, leftside, rightside):
    inversion = 0
    i, j, k = [0] * 3

    left_size, right_size = len(leftside), len(rightside)

    while i < left_size and j < right_size:
        if leftside[i] <= rightside[j]:
            arr[k] = leftside[i]
            i += 1
        else:
            arr[k] = rightside[j]
            j += 1
            inversion += (left_size - i)
        k += 1

    while i < left_size:
        arr[k] = leftside[i]
        i += 1
        k += 1
    
    while j < right_size:
        arr[k] = rightside[j]
        j += 1
        k += 1
    
    return arr, inversion

def mergeSort(arr):
    if len(arr) <= 1 :
        return arr, 0

    mid = len(arr) // 2  

    leftside, left_result = mergeSort(arr[:mid])
    rightside, right_result = mergeSort(arr[mid:])

    merged_arr, merge_result = mergeArrays(arr, leftside, rightside)

    return merged_arr, (left_result + right_result + merge_result)

def countInversions(arr):
    _sorted, inversion = mergeSort(arr)
    return inversion

if __name__ == "__main__":
    for _ in range(int(input())):
        _arr_size = int(input())
        arr = list(map(int, input().strip().split()))

        print(countInversions(arr))