'''
Problem: You are given queries. Each query is of the form two integers described below:
        -1 x : Insert x in your data structure.
        -2 y : Delete one occurence of y from your data structure, if present.
        -3 z : Check if any integer is present whose frequency is exactly z. If yes, print 1 else 0.

        The queries are given in the form of a 2-D array queries of size q where queries[i][0] contains the operation, and queries[i][1]
        contains the data element. For example, you are given array queries = [(1,1), (2,2), (3,2), (1,1), (1,1), (2,1), (3,2)]. The results
        of each operation are:
            Operation   Array   Output
            (1,1)       [1]
            (2,2)       [1]
            (3,2)                   0
            (1,1)       [1,1]
            (1,1)       [1,1,1]
            (2,1)       [1,1]
            (3,2)                   1

        Return an array with the output: [0, 1].

    Function Description: Complete the freqQuery function in the editor below. It must return an array of integers where each element is a
        1 if there is at least one element value with the queried number of occurrences in the current array, or 0 if there is not.
        freqQuery has the following parameter(s):
            queries: a 2-d array of integers

    Input Format: The first line contains of an integer q, the number of queries.
        Each of the next lines contains two integers denoting the 2-d array queries.

    Constraints:    1 <= q <= 10^6
                    1 <= x, y, z <= 10^9
                    All queries[i][0] E {1, 2, 3}
                    1 <= queries[i][1] <= 10^9

    Output Format:  Return an integer array consisting of all the outputs of queries of type 3.
'''
from collections import defaultdict
from collections import Counter
import os
import sys

# Best execution time
def freqQuery(arr):
    freq_dict = defaultdict(set)
    keeper = dict()

    for action, value in arr:
        # let's first check if we have the value present and if we have then return the value
        freq = keeper.get(value, 0)
        if action == 1:
            # if the number is not in the dictionary, set the default to zero
            # and if it exists then the set default will return the current value
            # and then add 1 to it
            keeper[value] = freq + 1
            # discard the value in the current set and move it to the new 
            # increased freq set
            freq_dict[freq].discard(value)
            freq_dict[freq + 1].add(value)

            # discard the defaultdict keys with empty set
            if freq_dict[freq] == set():
                freq_dict.pop(freq)

        elif action == 2:
            # if the value exist in the dictionary, decrease the frequency by 1
            keeper[value] = max(0, freq - 1)
            # Discard the value from the current set and move it to
            # the lowered set
            freq_dict[freq].discard(value)
            freq_dict[freq - 1].add(value)

            # discard the defaultdict keys with empty set
            if freq_dict[freq] == set():
                freq_dict.pop(freq)
        else:
            if value in freq_dict.keys():
                #op.append(1)
                print(1)
            else: 
                #op.append(0)
                print(0)
            #print("output:", op)
        #print(freq)

# Better complexity, using counters
'''
def freqQuery(queries):
    freq, cnt = Counter(), Counter()
    arr = list()

    for q in queries:
        print(q)
        if q[0]==1:
            cnt[freq[q[1]]]-=1
            print("cnt:", cnt)
            freq[q[1]]+=1
            cnt[freq[q[1]]]+=1
            print("freq:", freq)
            print("cnt:", cnt)

        elif q[0]==2:
            if freq[q[1]]>0:
                cnt[freq[q[1]]]-=1
                freq[q[1]]-=1
                cnt[freq[q[1]]]+=1
                print("cnt:", cnt)
                print("freq:", freq)

        else:
            if cnt[q[1]]>0:
                arr.append(1)
            else:
                arr.append(0)
    return arr
'''

# High time complexity
'''
def freqQuery(arr):
    freq = defaultdict(int)
    #op = []

    for action, value in arr:
        #print("Current action:", action, "value:", value)
        if action == 1:
            freq[value] += 1
        elif action == 2:
            if value in freq.keys(): freq[value] -= 1
        else:
            if value in freq.values():
                #op.append(1)
                print(1)
            else: 
                #op.append(0)
                print(0)
            #print("output:", op)
        #print(freq)
'''

if __name__ == "__main__":
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')
    # fptr = sys.stdout()

    queries = []

    with open('input.txt') as in_file:
        q_no = int(in_file.readline())
        for line in in_file:
            temp = list(map(int, line.split()))
            queries.append(temp)

    # for _ in range(int(input())):
    #    queries.append(list(map(int, input().rstrip().split())))

    # ans = freqQuery(queries)

    # fptr.write('\n'.join(map(str, ans)))
    # fptr.write('\n')

    # fptr.close()
    freqQuery(queries)