'''
Problem: Starting with a 1-indexed array of zeros and a list of operations, for each operation add a value to each of the array element
         between two given indices, inclusive. Once all operations have been performed, return the maximum value in your array.
         For example, the length of your array of zeros n = 10. Your list of queries is as follows:
                    a b k
                    1 5 3
                    4 8 7
                    6 9 1
        Add the values of k between the indices a and b inclusive:
            index->	 1 2 3  4  5 6 7 8 9 10
                    [0,0,0, 0, 0,0,0,0,0, 0]
                    [3,3,3, 3, 3,0,0,0,0, 0]
                    [3,3,3,10,10,7,7,7,0, 0]
                    [3,3,3,10,10,8,8,8,1, 0]
        The largest value is 10 after all operations are performed.

    Function Description: Complete the function arrayManipulation in the editor below. It must return an integer, the maximum value in the
        resulting array.
        arrayManipulation has the following parameters:
            -> n - the number of elements in your array
            -> queries - a two dimensional array of queries where each queries[i] contains three integers, a, b, and k.

    Input Format: The first line contains two space-separated integers n and m, the size of the array and the number of operations.
        Each of the next m lines contains three space-separated integers a, b and k, the left index, right index and summand.

    Constraints:
        3 <= n <= 10^7
        1 <= m <= 2 * 10^5
        1 <= a <= b <= n
        0 <= k <= 10^9

    Output Format: Return the integer maximum value in the finished array.
5 3
1 2 100
2 5 100
3 4 100
'''

# Code has high computational and space complexity.
'''def arrayManipulation(arr_size, queries):
    # returns an integer, the maximum value in the array.
    # Create array with all elements initialized to zero 
    arr = [0] * arr_size
    max_elem = 0

    for query in queries:
        #print("Before:",arr)
        #print("query:", query)
        for index in range(query[0] - 1, query[1]):
            arr[index] += query[2]
            if max_elem < arr[index]:
                max_elem =  arr[index]    
    print(max_elem)

if __name__ == "__main__":
    # arr, operations = 5, 3
    # op_params = [[1, 2, 100], [2, 5, 100], [3, 4, 100]]
    # accept the zero-array size and number of operations
    arr, operations = map(int, input().split())

    # accept the operation parameters
    op_params = []
    for _ in range(operations):
        op_params.append(list(map(int, input().rstrip().split())))

    arrayManipulation(arr, op_params) '''


# Code with better space time complexity
if __name__ == "__main__":
    # accept the zero-array size and number of operations
    arr_size, operations = map(int, input().split())

    arr = [0] * (arr_size + 1)

    for _ in range(operations):
        print("Before:",arr)
        a, b, k = [int(n) for n in input().rstrip().split()]
        arr[a - 1] += k

        print("length:", arr_size, len(arr))
        if b <= len(arr): 
            arr[b] -= k
        print("After:",arr)

    max_elem = counter = 0
    for elem in arr:
        counter += elem

        if max_elem < counter: 
            max_elem = counter
    print(max_elem)
