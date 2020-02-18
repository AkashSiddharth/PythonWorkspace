'''
Problem: You are given an unordered array consisting of consecutive integers E [1, 2, 3, ..., n] without any duplicates. You are allowed to
        swap any two elements. You need to find the minimum number of swaps required to sort the array in ascending order.
        For example, given the array arr = [7, 1, 3, 2, 4, 5, 6] we perform the following steps:
                i   arr                         swap (indices)
                0   [7, 1, 3, 2, 4, 5, 6]   swap (0,3)
                1   [2, 1, 3, 7, 4, 5, 6]   swap (0,1)
                2   [1, 2, 3, 7, 4, 5, 6]   swap (3,4)
                3   [1, 2, 3, 4, 7, 5, 6]   swap (4,5)
                4   [1, 2, 3, 4, 5, 7, 6]   swap (5,6)
                5   [1, 2, 3, 4, 5, 6, 7]

        It took 5 swaps to sort the array.

    Function Description: Complete the function minimumSwaps in the editor below. It must return an integer representing the minimum number
        of swaps to sort the array.
        minimumSwaps has the following parameter(s):
            -> arr: an unordered array of integers

    Input Format: The first line contains an integer, n, the size of arr. The second line contains n space-separated integers arr[i].

    Constraints:    1 <= n <= 10^5
                    1 <= arr[i] <= n

    Output Format: Return the minimum number of swaps to sort the given array.
'''
# Approach: Visualize a graph and find cycles in it. To sort any cycle with n nodes it takes (n-1) swaps.
def minimumSwaps(arr):
    # inititalize variables
    swaps = 0

    # create a new array with node numbers and values.
    # subtracting 1 from each element to make it easier to compare with the index values.
    arr_graph = [*enumerate([x-1 for x in arr])]

    # initialize a boolean array to record node visit
    visited = [False] * len(arr)

    # traverse the nodes, until all are: visited = True 
    for node, value in arr_graph:
        # If the enumerated index & value are equal, it means that the node is at the right place
        # Set visited to true and continue to the next node
        if node == value or visited[value] == True:
            continue

        # If the enumerated index & value are unequal, it means that the node is at the wrong place
        # set the node as visited
        cycle_size = 0
        value = node

        while not visited[value]:
            # set visited to true
            visited[value] = True

            # set the value of the node as the index and check the next node, until a visited node is found.
            value = arr_graph[value][1]

            # Increase the cycle size with each node redirection
            cycle_size += 1
        swaps += (cycle_size - 1)

    print(swaps)

if __name__ == "__main__":
    # Accept input
    size, arr = int(input().rstrip()), [*map(int, input().rstrip().split())]

    # Call minimumSwaps
    minimumSwaps(arr)
