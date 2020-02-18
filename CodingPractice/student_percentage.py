'''
Problem: You have a record of N students. Each record contains the student's name, and their percent marks in Maths, Physics and Chemistry.
        The marks can be floating values. The user enters some integer N followed by the names and marks for students. You are required to
        save the record in a dictionary data type. The user then enters a student's name. Output the average percentage marks obtained by
        that student, correct to two decimal places.

    Input Format: The first line contains the integer N, the number of students. The next N lines contains the name and marks obtained by 
        that student separated by a space. The final line contains the name of a particular student previously listed.

    Constraints: 2 <= N <= 10
                0 <= Marks <= 100

    Output Format: Print one line: The average of the marks obtained by the particular student correct to 2 decimal places.
'''

# Accept the input
records = { temp[0]: list(temp[1:]) for _ in range(int(input())) if (temp := input().split())[0] != 'NaN' }

# If the student exists, then print the percentage
if (student := input().strip()) in records.keys():
    avg = sum([float(score) for score in records[student]]) / len(records[student])
    print(f'{avg:.2f}')
else:
    raise KeyError