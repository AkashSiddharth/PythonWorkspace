"""
start() & end()
These expressions return the indices of the start and end of the substring matched by the group.

Code
>>> import re
>>> m = re.search(r'\d+','1234')
>>> m.end()
4
>>> m.start()
0

Task
You are given a string .
Your task is to find the indices of the start and end of string  in .

Input Format:
The first line contains the string S.
The second line contains the string k.

Constraints:
    0 < len(S) < 100
    0 < len(k) < len(S)

Output Format:
Print the tuple in this format: (start _index, end _index).
If no match is found, print (-1, -1).

Sample Input:
aaadaa
aa

Sample Output:
(0, 1)  
(1, 2)
(4, 5)
"""
import re

def re_index_search(b_str: str, sbstr: str) -> None:
    matches = list(re.finditer(f'(?={sbstr})', b_str))
    if not matches:
        print("(-1, -1)")
    else:
        for item in matches:
            print("({0}, {1})".format(item.start(),item.start() + len(sbstr) - 1))

if __name__ == "__main__":
    base_str = input()
    search_substr = input()
    
    re_index_search(base_str, search_substr)
