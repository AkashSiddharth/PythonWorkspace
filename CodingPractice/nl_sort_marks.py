'''
Problem: Given the names and grades for each student in a Physics class of N students, store them in a nested list and print the name(s)
         of any student(s) having the second lowest grade.
         Note: If there are multiple students with the same grade, order their names alphabetically and print each name on a new line.

    Input Format: The first line contains an integer, N, the number of students. The subsequent 2N lines describe each student over 2
                    lines; the first line contains a student's name, and the second line contains their grade.

    Constraints:    2 <= N <= 5
                    There will always be one or more students having the second lowest grade.

    Output Format:  Print the name(s) of any student(s) having the second lowest grade in Physics; if there are multiple students, 
                    order their names alphabetically and print each one on a new line.

    Sample Input 0: 
                    5
                    Harry
                    37.21
                    Berry
                    37.21
                    Tina
                    37.2
                    Akriti
                    41
                    Harsh
                    39

    Sample Output 0
                    Berry
                    Harry
'''
# student = [[input(), float(input())] for _ in range(int(input()))]

student = [['anthem', 41.23], ['zack', 39.40], ['bandy', 39.40], ['fanta', 45.33], ['yoda', 36.2]]

# sort the class scores
student.sort(key = lambda elem: elem[1])

print(student)

filter_lowest = list(filter(lambda score: score[1] > student[0][1], student))
print(filter_lowest)

names = list(filter(lambda name: name[1] == filter_lowest[0][1], filter_lowest))
names.sort()

for i in range(len(names)):
    print(names[i][0]) 

        
