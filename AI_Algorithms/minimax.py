# A simple Python3 program to find
# maximum score that
# maximizing player can get

import math

def minimax (cur_depth, nodeIndex, maxTurn, scores, targetDepth):
    # Max depth reached
    if cur_depth == targetDepth:
        return scores[nodeIndex]
    
    if maxTurn:
        return max(
                    minimax(cur_depth + 1, nodeIndex * 2, False, scores, targetDepth),
                    minimax(cur_depth + 1, nodeIndex * 2 + 1, False, scores, targetDepth) 
                )
    else: # If minTurn
        return min(
                    minimax(cur_depth + 1, nodeIndex * 2, True, scores, targetDepth),
                    minimax(cur_depth + 1, nodeIndex * 2 + 1, True, scores, targetDepth)
                )
def runner():
    scores = [3, 5, 2, 9, 12, 5, 23, 23]
    treeDepth = math.log(len(scores), 2)

    print("Optimal score:", end= "")
    print(minimax(0, 0, True, scores, treeDepth))

if __name__ == "__main__":
    runner()