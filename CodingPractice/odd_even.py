'''
Problem: Ask the user for a number. Depending on whether the number is even or odd, print out an appropriate message to the user.
            Extras:
                --> If the number is a multiple of 4, print out a different message.
                --> Ask the user for two numbers: one number to check (call it num) and one number to divide by (check). 
                If check divides evenly into num, tell that to the user. If not, print a different appropriate message.

'''

num = int(input("Odd or Even: "))
check = int(input("Check: "))

if num % 2 == 0:
    if num % 4 == 0:
        print("Even & Divisible by 4")
    else:
        print("Even")
else:
    print("Not Even")

if num % check == 0:
    print(check,"divides",num,"cleanly.")
else:
    print(check,"does not divide",num,"cleanly.")