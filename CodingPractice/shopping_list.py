def shopping_list(*small_talk: tuple, **grocery_list: dict) -> int:
	''' The function takes all the values of the shopping list
passed as a dictionary and returns the total bill.
'''
	if input('Is the shop open? ') in {'Yes', 'yes', 'Y', 'y'}:
		bill: int = 0
		for words in small_talk:
			print(words)
		for item, quantity in grocery_list.items():
			print ("Give me ", item, ": ", quantity, " Kg")
			bill += 5 * int(quantity)
		return bill

# print function doc
print(shopping_list.__doc__)

# print function annotation
print(shopping_list.__annotations__)

# Call the function
bill = shopping_list('Great!','I was hoping for it', 'Here is my Grocery list: ', Maida=5, Sugar=2, Atta='10')

print ("Shopping Bill : ", bill)