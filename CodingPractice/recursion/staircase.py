'''
Problem: Davis has a number of staircases in his house and he likes to climb 
    each staircase 1, 2, or 3 steps at a time. Being a very precocious child, 
    he wonders how many ways there are to reach the top of the staircase.

    Given the respective heights for each of the s staircases in his house, 
    find and print the number of ways he can climb each staircase.

Returns: int: the number of ways Davis can climb the staircase.

Input Format: The first line contains a single integer, s, the number of 
    staircases in his house.
    Each of the following s lines contains a single integer, n, the height of 
    staircase i.

Constraints:  1 <= s <= 5
              1 <= n <= 36
'''
def stepPerms(n: int) -> int:
  

if __name__ == "__main__":
  # number of staircases
  s = int(input().strip())

  for i in range(n):
    # height of the staircase
    n = int(input().strip())

    # get the number of ways the stair can be  traversed
    print(stepPerms(n))