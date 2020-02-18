'''
Problem : Given a 6 X 6 2D Array, arr:

            1 1 1 0 0 0
            0 1 0 0 0 0
            1 1 1 0 0 0
            0 0 0 0 0 0
            0 0 0 0 0 0
            0 0 0 0 0 0

        We define an hourglass in arr to be a subset of values with indices falling in this pattern in arr's graphical representation:

            a b c
            d
            e f g

        There are 16 hourglasses in arr, and an hourglass sum is the sum of an hourglass' values. Calculate the hourglass sum for every
        hourglass in arr, then print the maximum hourglass sum.

        Input Format: Each of the 6 lines of inputs contains space-separated integers arr[i][j].

        Output Format: Print the largest (maximum) hourglass sum found in arr.
'''
from functools import reduce

arr = [list(map(int, input().split())) for i in range(6)]
print(arr)

max_hglass_sum = -99999999

# get 3 X 3 sub arrays
for v_iter in range(4):
    for h_iter in range(4):
        sub_arr = []
        for i in range (3):
            sub_arr.append(arr[v_iter+i][h_iter:h_iter+3])
        # Get the sum of the sub array
        hourglass_sum = sum(reduce(lambda x,y: x+y, i) for i in sub_arr) - sub_arr[1][0] - sub_arr[1][2]
        print(sub_arr,'   ',hourglass_sum)
        if hourglass_sum > max_hglass_sum:
            max_hglass_sum = hourglass_sum

print("max hourglass sum:", max_hglass_sum)
