'''
Problem: A group of friends want to buy a bouquet of flowers. The florist wants to maximize his
         number of new customers and the money he makes. To do this, he decides he'll multiply the 
         price of each flower by the number of that customer's previously purchased flowers plus 1.
         The first flower will be original price, (0 + 1) X Original Price, the next will be 
         (1 + 1) X Original Price and so on.

         Given the size of the group of friends, determine the minimum cost to purchase atleast one
         of each type of the flowers.

    Function Description: Complete the getMinimumCost function in the editor below. It should return
         the minimum cost to purchase all of the flowers.
         getMinimumCost has the following parameter(s):
            --> c: an array of integers representing the original price of each flower
            --> k: an integer, the number of friends

    Input Format:   --> The first line contains two space-separated integers n and k, the number of 
                        flowers and the number of friends.
                    --> The second line contains n space-separated positive integers c[i], the 
                        original price of each flower.

    Constraints:    --> 1 <= n, k <= 100
                    --> 1 <= c[i] <= 10^6
                    --> answer < 2^31
                    --> 0 <= i < n

    Output Format: Print the minimum cost to buy all n flowers.
'''
def getMinimumCost(k, c):
    # sort the costs
    c.sort(reverse=True)

    return sum([((i // k) + 1)*cost for i, cost in enumerate(c)])

# accept input
if __name__ == "__main__":
    with open("S:\\GitHub\\PythonWorkspace\\DataStructure\\Greedy\\input.txt") as in_file:
        num_flower, group_size = list(map(int, in_file.readline().split()))
        prices = list(map(int, in_file.readline().split()))
    
    print(getMinimumCost(group_size, prices))
