''' Problem: I give you a list saved in a variable: a = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]. 
             Write one line of Python that takes this list a and makes a new list that has only
             the even elements of this list in it.
'''
if __name__ == "__main__":
    import random
    rand_lst = random.choices(range(1,1000), k=random.randint(1,100))
    evn_lst = [x for x in rand_lst if x % 2 == 0]
    print(sorted(evn_lst))