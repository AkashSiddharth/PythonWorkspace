''' Problem: Ask the user for a string and print out whether this string is a palindrome or not.
             (A palindrome is a string that reads the same forwards and backwards.)
'''

if __name__ == "__main__":
    p_str = input("Enter a string: ")
    print(p_str + " is a palindrome") if (p_str == p_str[::-1]) else print(p_str + " not a palindrome")