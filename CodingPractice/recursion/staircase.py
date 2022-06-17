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

## Recursion solution
def r_stepPerms(n: int) -> int:
  if n < 0: return 0
  elif n == 1:  return 1
  elif n in [1,2,3]:
    return 1 + sum(r_stepPerms(n - s) for s in [1,2,3] if s < n)
  else:
    return sum(r_stepPerms(n - s) for s in [1,2,3] if s < n)

## Dynamic Solution 
def stepPerms(n: int) -> int:
  cache = [0] * (n+1)
  cache[0] = 1

  for i in range(n+1):
    cache[i] = sum(cache[i - s] for s in [1,2,3] if (i - s) > 0)
    cache[i] += 1 if i in [1,2,3] else 0
  
  return cache[-1]

if __name__ == "__main__":
  # number of staircases
  s = int(input().strip())

  for i in range(n):
    # height of the staircase
    n = int(input().strip())

    # get the number of ways the stair can be  traversed
    print(stepPerms(n))
