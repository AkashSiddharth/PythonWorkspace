def age():
    ''' The functions requests input for name and age and returns year when the user turns 100.'''
    import datetime
    name = input("Specify your name: ")
    age = int(input("Specify your age in years: "))
    repeat = int(input ("Specify the number of times you need this repeated: "))
    cur_year = datetime.datetime.now()
    print ("Hello %s. You will turn a 100 yrs old in %d" %(name, (cur_year.year + (100 - age))) * repeat, end = '\n')
 
# Call the function
age()