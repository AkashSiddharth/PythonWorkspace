'''
Problem: Harold is a kidnapper who wrote a ransom note, but now he is worried it will be traced back to him through his handwriting. He 
        found a magazine and wants to know if he can cut out whole words from it and use them to create an untraceable replica of his 
        ransom note. The words in his note are case-sensitive and he must use only whole words available in the magazine. He cannot use 
        substrings or concatenation to create the words he needs.
        Given the words in the magazine and the words in the ransom note, print Yes if he can replicate his ransom note exactly using whole
        words from the magazine; otherwise, print No.
        For example, the note is "Attack at dawn". The magazine contains only "attack at dawn". The magazine has all the right words, but 
        there's a case mismatch. The answer is No.

    Function Description: Complete the checkMagazine function in the editor below. It must print Yes if the note can be formed using the 
        magazine, or No.
        checkMagazine has the following parameters:
            --> magazine: an array of strings, each a word in the magazine
            --> note: an array of strings, each a word in the ransom note

    Input Format: The first line contains two space-separated integers, m and n, the numbers of words in the magazine and the note..
        The second line contains m space-separated strings, each magazine[i] .
        The third line contains n space-separated strings, each note[i].

    Constraints:    1 <= m, n <= 30000
                    1 <= |magazine[i]|, |note[i]| <= 5
                    Each word consists of English alphabetic letters (i.e., a to z and A to Z).

    Output Format: Print Yes if he can use the magazine to create an untraceable replica of his ransom note. Otherwise, print No.
'''
# High time complecity
'''def checkMagazine(magazine, note):
    for word in set(note):
        if note.count(word) <= magazine.count(word):
            continue
        else:
            print("No")
            return
    print("Yes")
'''

# Still high execution time
'''def checkMagazine(magazine, note):
    # Convert both in hash maps in word occurances
    note_map = {word: note.count(word) for word in set(note)}
    magazine_map = {word: magazine.count(word) for word in set(magazine)}

    for word in note_map.keys():
        if word in magazine_map and magazine_map[word] >= note_map[word]:
            continue
        else:
            print("No")
            return
    print("Yes")
'''
# using counter from collections
'''from collections import Counter

def checkMagazine(magazine, note):
    if (Counter(note) - Counter(magazine)) == Counter():
        print("Yes")
    else:
        print("No")'''

# using defaultdict from collections
from collections import defaultdict

def checkMagazine(magazine, note):
    mag_dict = defaultdict(int)
    for word in magazine:
        mag_dict[word] += 1
    
    for word in note:
        if word in mag_dict:
            mag_dict[word] -= 1
        else:
            print("No")
            return
    
    if all(cnt >= 0 for cnt in mag_dict.values()):
        print("Yes")
    else:
        print("No")

if __name__ == "__main__":
    # Accept the input
    m, n = [*map(int, input().rstrip().split())]

    magazine, note = input().rstrip().split(), input().rstrip().split()

    checkMagazine(magazine, note)