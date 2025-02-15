# # Create 2 new lists height and weight
# height = [1.87,  1.87, 1.82, 1.91, 1.90, 1.85]
# weight = [81.65, 97.52, 95.25, 92.98, 86.18, 88.45]

# # Import the numpy package as np
# import numpy as np

# # Create 2 numpy arrays from height and weight
# np_height = np.array(height)
# np_weight = np.array(weight)

# print(type(np_height))

# # Calculate bmi
# bmi = np_weight / np_height ** 2

# # Print the result
# print(bmi)

# print(bmi[bmi > 25])

## Pandas test
# dict = {"country": ["Brazil", "Russia", "India", "China", "South Africa"],
#        "capital": ["Brasilia", "Moscow", "New Dehli", "Beijing", "Pretoria"],
#        "area": [8.516, 17.10, 3.286, 9.597, 1.221],
#        "population": [200.4, 143.5, 1252, 1357, 52.98] }

# import pandas as pd
# brics = pd.DataFrame(dict)
# print(brics)

###################################################################################
## Generator Example
## Bingo Number Generator
# import random

# def lottery():
#     # returns 6 numbers between 1 and 40
#     for i in range(6):
#         yield random.randint(1, 40)

#     # returns a 7th number between 1 and 15
#     yield random.randint(1, 15)

# for random_number in lottery():
#        print("And the next number is... %d!" %(random_number))

####################################################################################

## Fibonnaci Generator
# def fib():
#     a, b = 0, 1
#     while True:
#         yield a
#         a, b = b, a + b

# # testing code
# import types
# if type(fib()) == types.GeneratorType:
#     print("Good, The fib function is a generator.")

#     counter = 0
#     for n in fib():
#         print(n)
#         counter += 1
#         if counter == 10:
#             break

####################################################################################
# Decorartor Example
# def type_check(correct_type):
#     def check(old_function):
#         def new_function(arg):
#             if (isinstance(arg, correct_type)):
#                 return old_function(arg)
#             else:
#                 print("Bad Type")
#         return new_function
#     return check

# @type_check(int)
# def times2(num):
#     return num*2

# print(times2(2))
# times2('Not A Number')

# @type_check(str)
# def first_letter(word):
#     return word[0]


####################################################################################
# def my_add_fn():
#    print("SUM:%s"%sum(map(int,raw_input("Enter 2 numbers seperated by a space").split())))

# def my_quit_fn():
#    raise SystemExit

# def invalid():
#    print("INVALID CHOICE!")

# menu = {"1":("Sum",my_add_fn),
#         "2":("Quit",my_quit_fn)
#        }
# for key in sorted(menu.keys()):
#      print(key+":" + menu[key][0])

# ans = int(input("Make A Choice"))
# menu.get(ans,[None,invalid])[1]()
####################################################################################
# Color Example
# class Font:
#    def set_style(f_style, fcolor, bcolor = "black"):
#       style = {
#          "NORMAL": "\033[0m",
#          "BOLD": "\033[1m",
#          "FAINT": "\033[2m",
#          "ITALIC": "\033[3m",
#          "UNDERLINE": "\033[4m",
#          "BLINK": "\033[5m",
#          "NEGATIVE": "\033[7m",
#          "STRIKE": "\033[9m"
#       }

#       fgcolor = {
#          "BLACK": "\033[0;30m",
#          "RED": "\033[0;31m",
#          "GREEN": "\033[0;32m",
#          "BROWN": "\033[0;33m",
#          "BLUE": "\033[0;34m",
#          "PURPLE": "\033[0;35m",
#          "CYAN": "\033[0;36m",
#          "LIGHT_GRAY": "\033[0;37m",
#          "DARK_GRAY": "\033[1;30m",
#          "LIGHT_RED": "\033[1;31m",
#          "LIGHT_GREEN": "\033[1;32m",
#          "YELLOW": "\033[1;33m",
#          "LIGHT_BLUE": "\033[1;34m",
#          "LIGHT_PURPLE": "\033[1;35m",
#          "LIGHT_CYAN": "\033[1;36m",
#          "LIGHT_WHITE": "\033[1;37m"
#       }

#       bgcolor = {
#          "BLACK": "\033[40m",
#          "RED": "\033[41m",
#          "GREEN": "\033[42m",
#          "BROWN": "\033[43m",
#          "BLUE": "\033[44m",
#          "MAGENTA": "\033[45m",
#          "CYAN": "\033[46m",
#          "GRAY": "\033[47m"
#       }

#       code = "{0}{1}{2}".format(style[f_style.upper()], 
#                                  fgcolor[fcolor.upper()], 
#                                  bgcolor[bcolor.upper()])

#       return code
    
#    def end_style():
#       END_FONT_STYLE = "\033[0m"
#       return END_FONT_STYLE

# print(Font.set_style("blink",'red') + "TESTING" + Font.end_style())
######################################################################
# row = 7
# col = 8
# text = 'ifmanwasmeanttostayonthegroundgodwouldhavegivenusroots'
import itertools
row = 3
col = 3
text = 'chillout'
textf = [[text[(i*col) + j] for j in range(col) if (i* col + j) < len(text)] for i in range(row)]
print(*textf)

t_textf = list(itertools.zip_longest(*textf, fillvalue= ''))
print(t_textf)
# print(zip(['c', 'h', 'i'], ['l', 'l', 'o'], ['u', 't']))
# print(*zip(['c', 'h', 'i'], ['l', 'l', 'o'], ['u', 't']))
