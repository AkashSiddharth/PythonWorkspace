'''
Problem: The Fibonacci sequence begins with fibonacci(0) = 0 and fibonacci(1) = 1 as its 
  first and second terms. After these first two elements, each subsequent element 
  is equal to the sum of the previous two elements.

  Programmatically: fibonacci(0) = 0
                    fibonacci(1) = 1
                    fibonacci(n) = fibonacci(n - 1) + fibonacci(n - 2)

Function Description: Complete the recursive function fibonacci.
    fibonacci has the following parameter(s):
        int n: the index of the sequence to return

Returns: int: the nth element in the Fibonacci sequence

Input Format: The integer n

Constraints: 0 < n <= 30
'''
def fibonacci(n : int) -> int:
  if n <= 1:
    return n

  return fibonacci(n - 1) + fibonacci(n - 2)

if __name__ == "__main__":
  n = int(input())
  print(fibonacci(n))