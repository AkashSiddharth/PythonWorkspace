'''
Problem: You will be given a list of integers, arr, and a single integer k. You must create an 
         array of length k from elements of arr such that its unfairness is minimized. Call that 
         array subarr. Unfairness of an array is calculated as max(subarr) - min(subarr).
         Note: Integers in arr may not be unique.

    Function Description: Complete the maxMin function in the editor below. It must return an 
        integer that denotes the minimum possible value of unfairness.
        maxMin has the following parameter(s):
            k: an integer, the number of elements in the array to create
            arr: an array of integers .

    Input Format:   The first line contains an integer n, the number of elements in array arr.
                    The second line contains an integer k.
                    Each of the next n lines contains an integer arr[i] where 0 < i < n.

    Constraints:    2 <= n <= 10^5
                    2 <= k <= n
                    0 <= arr[i] <= 10^9

    Output Format: An integer that denotes the minimum possible value of unfairness.
'''
def maxMin(k, arr):
    # sort the arr
    arr.sort()
    unfair = arr[k-1] - arr[0]

    for index in range(1, len(arr) - (k-1)):
        t_unfair = arr[index + (k-1)] - arr[index]

        unfair = t_unfair if t_unfair < unfair else unfair 

    return unfair

if __name__ == "__main__":
    with open('.\\input.txt') as in_file:
        arr_len = int(in_file.readline())
        sub_arr_len = int(in_file.readline())
        arr = [int(x.strip()) for x in in_file ]
    
    print(maxMin(sub_arr_len, arr))