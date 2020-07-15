''' 
Problem: Create a program that asks the user to enter their name and their age. Print out a message addressed
         to them that tells them the year that they will turn 100 years old.
            Extras:
                -> Add on to the previous program by asking the user for another number and printing out that
                   many copies of the previous message.
                -> Print out that many copies of the previous message on separate lines.
'''

def age():
    ''' The functions requests input for name and age and returns year when the user turns 100.'''
    import datetime
    name = input("Specify your name: ")
    age = int(input("Specify your age in years: "))
    repeat = int(input ("Specify the number of times you need this repeated: "))
    cur_year = datetime.datetime.now()
    print("Hello %s. You will turn a 100 yrs old in %d\n" %(name, (cur_year.year + (100 - age))) * repeat)
 
# Call the function
age()