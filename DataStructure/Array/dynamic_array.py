'''
Problem: Create a list, seqList, of N empty sequences, where each sequence is indexed from 0 to N-1. The elements within each of the
        N sequences also use 0-indexing. Create an integer, lastAnswer, and initialize it to 0. The types of queries that can be performed 
        on your list of sequences (seqList) are described below:
            Query: 1 x y
                1. Find the sequence, seq, at index ((x XOR lastAnswer) % N) in seqList.
                2. Append integer y to sequence seq.
            Query: 2 x y
                1. Find the sequence, seq, at index ((x XOR lastAnswer) % N) in seqList.
                2. Find the value of element y % size in seq (where is the size of seq) and assign it to lastAnswer.
                3. Print the new value of lastAnswer on a new line.

    Input Format: The first line contains two space-separated integers, N (the number of sequences) and Q (the number of queries),
                respectively. Each of the Q subsequent lines contains a query in the format defined above.

    Constraints:    1 <= N, Q < = 100000
                    0 <= x <= 1000000000
                    0 <= y <= 1000000000
                    It is guaranteed that query type 2 will never query an empty sequence or index.

    Output Format: For each type 2 query, print the updated value of on a new line.
'''

# Get the size of seqList and number of queries
seqListlen, _queries = list(map(int, input().split()))
seqList = [[] for _ in range(seqListlen)]
lastAnswer, queryList  = 0, []

# Get the queries
for _ in range(_queries):
    queryList.append(list(map(int, input().split())))

# Process the queries
for query in queryList:
    # Query Type 1
    indexVal = int((query[1] ^ lastAnswer) % seqListlen)
    if query[0] == 1:
        seqList[indexVal].append(query[2])
    # Query Type 2
    else:
        lastAnswer = seqList[indexVal][query[2] % len(seqList[indexVal])]
        print(lastAnswer)