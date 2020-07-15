''' Problem: Take two lists, say for example these two:
                a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
                b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
             and write a program that returns a list that contains only the elements that
             are common between the lists (without duplicates). Make sure your program works
             on two lists of different sizes.

             Extras:
                --Randomly generate two lists to test this
                --Write this in one line of Python (don’t worry if you can’t figure this out at this point - we’ll get to it soon)
'''

if __name__ == "__main__":
    import random as r
    a = r.choices(list(range(1,100)),k = r.randint(1,20))
    b = r.choices(list(range(1,100)),k = r.randint(1,20))

    c = [num for num in a if num in b]

    print("First list: {0}\nSecond List: {1}\nCommon List: {2}".format(a, b, c))

