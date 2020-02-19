'''
Problem: Mark and Jane are very happy after having their first child. Their son loves toys, so Mark wants to buy some. There are a number of
         different toys lying in front of him, tagged with their prices. Mark has only a certain amount to spend, and he wants to maximize
         the number of toys he buys with this money.
         Given a list of prices and an amount to spend, what is the maximum number of toys Mark can buy? 
         For example, if prices = [1,2,3,4] and Mark has k = 7 to spend, he can buy items for [1,2,3] for 6, or [3, 4] for 7 units of
         currency. He would choose the first group of 3 items.

    Function Description: Complete the function maximumToys in the editor below. It should return an integer representing the maximum number
        of toys Mark can purchase.
        maximumToys has the following parameter(s):
            --> prices: an array of integers representing toy prices
            --> k: an integer, Mark's budget

    Input Format:   The first line contains two integers, n and k, the number of priced toys and the amount Mark has to spend.
                    The next line contains n space-separated integers prices[i]

    Constraints:    1 <= n <= 10^5
                    1 <= k <= 10^9
                    1 <= prices[i] <= 10^9
                    A toy can't be bought multiple times.

    Output Format: An integer that denotes the maximum number of toys Mark can buy for his son.
'''

def maximumToys(arr, k):
    max_toys, temp = 0, 0

    # Filter out the values which are greater than k
    n_arr = sorted(filter(lambda x: x < k, arr))
    print(n_arr)

    while temp < k and max_toys < len(n_arr):
        temp += n_arr[max_toys]

        if temp < k:
            max_toys += 1
        else: break
 
    print(max_toys)

if __name__ == "__main__":
    inventory_size, budget = map(int, input().strip().split())
    inventory_prices = list(map(int, input().strip().split()))

    maximumToys(inventory_prices, budget)
