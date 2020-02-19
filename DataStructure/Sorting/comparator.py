'''
Problem: Comparators are used to compare two objects. In this challenge, you'll create a comparator and use it to sort an array. The Player
         class is provided in the editor below. It has two fields:
             name: a string.
             score: an integer.
         Given an array of n Player objects, write a comparator that sorts them in order of decreasing score. If 2 or more players have the
         same score, sort those players alphabetically ascending by name. To do this, you must create a Checker class that implements the 
         Comparator interface, then write an int compare(Player a, Player b) method implementing the Comparator.compare(T o1, T o2) method.
         In short, when sorting in ascending order, a comparator function returns -1 if a < b, 0 if a = b, and 1 if a > b.
         For example, given n = 3 Player objects with Player.name, Player.score values of , 
            data = [[Smith, 20], [Jones, 15], [Jones, 20]], we want to sort the list as
            data_sorted = [[Jones, 20], [Smith, 20], [Jones, 15]].

    Function Description: Declare a Checker class that implements the comparator method as described. It should sort first descending by 
         score, then ascending by name. The code stub reads the input, creates a list of Player objects, uses your method to sort the data,
         and prints it out properly.

    Input Format: Locked stub code in the Solution class handles the following input from stdin:
        The first line contains an integer, n, the number of players.
        Each of the next lines contains a player's respective name and score, a string and an integer.

    Constraints:    0 <= score <= 1000
                    Two or more players can have the same name.
                    Player names consist of lowercase English alphabetic letters.

    Output Format:  You are not responsible for printing any output to stdout. Locked stub code in Solution will create a Checker object,
                    use it to sort the Player array, and print each sorted element.
'''

class Player:
    def __init__(self, name, score):
        self.name = name
        self.score = score

    def __repr__(self):
        return repr((self.name, self.score))

    def comparator(a, b):
        # if the scores are equal then check the names
        if a.score != b.score:
            return b.score - a.score
        return (a.name > b.name) - (a.name < b.name)

n = int(input())
data = []
for i in range(n):
    name, score = input().split()
    score = int(score)
    player = Player(name, score)
    data.append(player)
    
data = sorted(data, key=cmp_to_key(Player.comparator))
for i in data:
    print(i.name, i.score)