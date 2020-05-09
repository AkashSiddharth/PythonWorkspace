'''
Problem: Alice is a kindergarten teacher. She wants to give some candies to the children in her 
         class.  All the children sit in a line and each of them has a rating score according to 
         his or her performance in the class.  Alice wants to give at least 1 candy to each child. 
         If two children sit next to each other, then the one with the higher rating must get more 
         candies. Alice wants to minimize the total number of candies she must buy.
         For example, assume her students' ratings are [4, 6, 4, 5, 6, 2]. She gives the students 
         candy in the following minimal amounts: [1, 2, 1, 2, 3, 1]. She must buy a minimum of 10 
         candies.

    Function Description: Complete the candies function in the editor below. It must return the 
        minimum number of candies Alice must buy.
        candies has the following parameter(s):
            n: an integer, the number of children in the class
            arr: an array of integers representing the ratings of each student

    Input Format:   --> The first line contains an integer, n, the size of arr.
                    --> Each of the next n lines contains an integer arr[i] indicating the rating 
                        of the student at position.

    Constraints: 1 <= n <= 10^5
                 1 <= arr[i] <= 10^5

    Output Format: Output a single line containing the minimum number of candies Alice must buy.
'''
def candies(n, arr):
    candy = [1] * n

    # Going Left -> Right
    for i in range(1,n):
        # If current rating is greater than previous rating
        # then increase the candy at index i  
        if arr[i] > arr[i-1]:
            candy[i] = candy[i-1] + 1
    
    print(candy)
    # Going Right -> Left
    for i in range(n-1, 0, -1):
        # if the current rating is greater than previous rating
        # If the number of candies are equal, add 1 
        if arr[i-1] > arr[i] and candy[i] >= candy[i-1]:
            candy[i-1] = candy[i] + 1
    
    return sum(candy)

if __name__ == "__main__":
    with open('S:\\GitHub\\PythonWorkspace\\DataStructure\\DynamicProgramming\\input.txt') as in_f:
        size = int(in_f.readline().strip())
        rating = [int(line) for line in in_f]
    
    print(candies(size, rating))