'''
Infinite Monkey Theorem ::: 
The theorem states that a monkey hitting keys at random on a typewriter keyboard for an 
infinite amount of time will almost surely type a given text, such as the complete works
of William Shakespeare. Well, suppose we replace a monkey with a Python function. How 
long do you think it would take for a Python function to generate just one sentence of 
Shakespeare? The sentence we'll shoot for is: “methinks it is like a weasel”

Self Check Challenge
See if you can improve upon the program in the self check by keeping letters that are correct
and only modifying one character in the best string so far. This is a type of algorithm in the
class of "hill climbing" algorithms, that is we only keep the result if it is better than the 
previous one.
'''

import random
import string

def gen_line(length):
  source = string.ascii_lowercase + ' '
  generated = ''.join([x for i in range(length) for x in source[random.randrange(27)]])
  return generated

def score(goal):
  source_line = gen_line(len(goal))

  sameness = 0

  for i in range(len(goal)):
    if goal[i] == source_line[i]:
      sameness += 1
      # print("Goal[{0}]: {1}".format(i, goal[i]))
      # print("Generated[{0}]: {1}".format(i, source_line[i]))

  sameness_percent = sameness / len(goal) * 100
  # print("Goal: {0}\nGenerated: {1}\nSameness: {2}".format(goal, source_line, sameness_percent))

  return sameness_percent, source_line

def simulate(runs, target_line):
  best_score=0
  best_string=''
  
  for attempt in range(runs):
    attempt_score, attempt_string = score(target_line)

    if attempt_score > best_score:
      best_score = attempt_score
      best_string = attempt_string
  
  return best_score, best_string

if __name__ == "__main__":
  target_line = "methinks it is like a weasel"

  final_score, final_string = simulate(100000, target_line)

  print(final_score)
  print(final_string)
