'''
Problem: A 10 X 10 Crossword grid is provided to you, along with a set of words
  (or names of places) which need to be filled into the grid. Cells are marked 
  either + or -. Cells marked with a - are to be filled with the word list.

  Example:  The following shows an example crossword from the input crossword grid
    and the list of words to fit, words = [POLAND, LHASA, SPAIN, INDIA]:

      Input 	   		Output
    ++++++++++ 		++++++++++
    +------+++ 		+POLAND+++
    +++-++++++ 		+++H++++++
    +++-++++++ 		+++A++++++
    +++-----++ 		+++SPAIN++
    +++-++-+++ 		+++A++N+++
    ++++++-+++ 		++++++D+++
    ++++++-+++ 		++++++I+++
    ++++++-+++ 		++++++A+++
    ++++++++++ 		++++++++++
    POLAND;LHASA;SPAIN;INDIA
  
  Input Format: Each of the first 10 lines represents crossword[i], each of which
    has 10 characters, crossword[i][j]. The last line contains a string consisting
    of semicolon delimited words[i] to fit. 
  
  Constraints:  1 <= |words| <= 10
                crossword[i][j] E {+,-}
                words[i][j] E ascii[A-Z]

  Output Format:  Position the words appropriately in the 10 X 10 grid, then return
    your array of strings for printing. 
'''
'''
Pseudo:
  1. iterate row and fill words
    1.1 if a row has - count it
    1.2 test if word of same length is there
    1.3 if more than 1 words of same length, continue (do not fill)
  2. tranpose and call the function again with partially filled crossword and word list with used words removed 
  3. return when the words array is empty
'''

def crosswordPuzzle(crossword, words):
    # Write your code here
    arr_words = words.split(';')
    dict_word_length= {len(x): x for x in arr_words}

    for row in crossword:
      if '-' in row:

if __name__ == '__main__':
    crossword = []

    for _ in range(10):
        crossword_item = input()
        crossword.append(crossword_item)

    words = input()

    result = crosswordPuzzle(crossword, words)

    print(','.join(result))
