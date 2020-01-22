'''
Problem: Given an integer, n, perform the following conditional actions:
            -> If n is odd, print Weird
            -> If n is even and in the inclusive range of 2 to 5, print Not Weird
            -> If n is even and in the inclusive range of 6 to 20, print Weird
            -> If n is even and greater than 20, print Not Weird
    Input Format: A single line containing a positive integer, n.

    Constraints: 1 <= n <= 100

    Output Format: Print Weird if the number is weird; otherwise, print Not Weird.
'''

n = int(input("Provide a number:"))

if n > 100 :
    exit
else:
    if n % 2 == 0:
        if n in range(2,6):
            print("Not Weird")
        elif n in range(6,21):
            print("Weird")
        else:
            print("Not Weird")
    else:
        print("Weird")
