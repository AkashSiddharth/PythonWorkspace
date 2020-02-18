'''
Problem: John works at a clothing store. He has a large pile of socks that he must pair by color for sale. Given an array of integers
         representing the color of each sock, determine how many pairs of socks with matching colors there are.

    Function Description: Complete the sockMerchant function in the editor below. It must return an integer representing the number 
        of matching pairs of socks that are available.
        sockMerchant has the following parameter(s):
            -- n: the number of socks in the pile
            -- ar: the colors of each sock

    Input Format: The first line contains an integer n, the number of socks represented in ar.
        The second line contains n space-separated integers describing the colors ar[i] of the socks in the pile.

    Constraints: 
        1 <= n <= 100
        1 <= ar[i] <= 100 where 0 <= i <= n

    Output Format: Return the total number of matching pairs of socks that John can sell.
'''
def sockMerchant(n, ar):
    # first sort the list, to group the similar colors:
    ar.sort()
    
    pairs, counter = 0, 0

    # count the similar colors
    for i in range(n):
        if counter == ar[i]:
            pairs += 1
            counter = 0
        else:
            counter = ar[i]
    
    print(pairs)

ar_size = int(input())
arr = list(map(int, input().rstrip().split()))

sockMerchant(ar_size, arr)
