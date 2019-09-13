#!/bin/python3

''' Problem: You are given a spreadsheet that contains a list of N athletes and their details (such as age, height, weight and
 so on). You are required to sort the data based on the K-th attribute and print the final resulting table.

 Note that K is indexed from 0 to M-1, where M is the number of attributes.

Note: If two attributes are the same for different rows, for example, if two atheletes are of the same age, 
print the row that appeared first in the input.

Input Format

The first line contains N and M separated by a space.
The next N lines each contain elements.
The last line contains K.

Constraints
    1 <= N,M <= 1000
    0 <= K < M
    Each element <= 1000

Output Format: Print the N lines of the sorted table. Each line should contain the space separated elements.
Check the sample below for clarity.

Sample Input 0

5 3
10 2 5
7 1 0
9 9 9
1 23 12
6 5 9
1

Sample Output 0

7 1 0
10 2 5
6 5 9
9 9 9
1 23 12

Explanation 0

The details are sorted based on the second attribute, since K is zero-indexed.
'''
import math
import os
import random
import re
import sys

nm = input().split()

n, m = int(nm[0]), int(nm[1])

arr = []

for _ in range(n):
    arr.append(list(map(int, input().rstrip().split())))

k = int(input())

arr.sort(key = lambda elem: elem[k])

for row in arr:
    print(' '.join(map(str, row)))