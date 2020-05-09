'''
Problem: Lena is preparing for an important coding competition that is preceded by a number of 
         sequential preliminary contests. Initially, her luck balance is 0. She believes in "saving
         luck", and wants to check her theory. Each contest is described by two integers, L[i] and 
         T[i]:
            --> L[i] is the amount of luck associated with a contest. If Lena wins the contest, her
                luck balance will decrease by L[i]; if she loses it, her luck balance will increase
                by L[i].
            --> T[i] denotes the contest's importance rating. It's equal to 1 if the contest is 
                important, and it's equal to 0 if it's unimportant.
         If Lena loses no more than k important contests, what is the maximum amount of luck she 
         can have after competing in all the preliminary contests? This value may be negative.
         For example, k = 2 and:
            Contest		L[i]	T[i]
                1		5       1
                2		1	    1
                3		4	    0
         If Lena loses all of the contests, her will be 5 + 1 + 4 = 10. Since she is allowed to 
         lose 2 important contests, and there are only 2 important contests. She can lose all three
         contests to maximize her luck at 10. If k = 1, she has to win at least 1 of the 2 
         important contests. She would choose to win the lowest value important contest worth 1.
         Her final luck will be 5 + 4 - 1 = 8.

    Function Description: Complete the luckBalance function in the editor below. It should return 
        an integer that represents the maximum luck balance achievable.
        luckBalance has the following parameter(s):
            --> k: the number of important contests Lena can lose
            --> contests: a 2D array of integers where each contests[i] contains two integers that 
                represent the luck balance and importance of the i-th contest.

    Input Format:   --> The first line contains two space-separated integers n and k, the number of
                        preliminary contests and the maximum number of important contests Lena can
                        lose.
                    --> Each of the next n lines contains two space-separated integers, L[i] and 
                        T[i], the contest's luck balance and its importance rating.

    Constraints:    1 <= n <= 100
                    0 <= k <= N
                    1 <= L[i] <= 10^4
                    T[i] E {0, 1}

    Output Format: Print a single integer denoting the maximum amount of luck Lena can have after 
        all the contests.
'''
# Simple solution
def luckBalance(k, contest):
    # sort the luck in increasing order
    sorted_contest = sorted(contest, key=lambda k: k[0], reverse=True)

    # initialize luck factor
    lf = 0

    for i in range(len(contest)):
        if sorted_contest[i][1] == 1:
            if k > 0:
                lf += sorted_contest[i][0]
                k -= 1
            else:
                lf -= sorted_contest[i][0]
        else:
            lf = lf + sorted_contest[i][0] if sorted_contest[i][0] > 0 else lf - sorted_contest[i][0]
    
    return lf

# Naive recursive solution
'''
def luckBalance(k, contests):
    # If whole array has been examined
    if len(contests) == 0:
        return 0

    # If the loss threhold is exhausted and the nth item in important
    if k == 0 and contests[-1][1] == 1:
        return -contests[-1][0] + luckBalance(k, contests[:-1])
    else:
        # Either we can win the contest or we can lose it
        # we will consider the branch which returns the maximum luck
        return max(contests[-1][0] + luckBalance(k - contests[-1][1], contests[:-1]), -contests[-1][0] + luckBalance(k, contests[:-1]))
'''

if __name__ == "__main__":
    with open("s:\\GitHub\\PythonWorkspace\\DataStructure\\Greedy\\input.txt") as in_f:
        n, k = list(map(int, in_f.readline().split()))
        contest = [list(map(int, line.split())) for line in in_f]

    print(luckBalance(k, contest))

