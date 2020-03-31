import sys, os

def sort_course_util(index, visited, sorted_arr, input_arr):
    # mark the index in visited as 1
    visited[index] = 1

    # Find the next course index by searching the pre-req
    for i, course in enumerate(input_arr):
        # if the current course is equal to the pre-requisite and,
        # visited is false for the index
        if course[0] == input_arr[index][1] and not visited[i]:
          sort_course_util(i, visited, sorted_arr, input_arr)

    # push the course in stack
    if input_arr[index][1] not in sorted_arr:
      #print("Pushin prereq-",input_arr[index][1])
      sorted_arr.append(input_arr[index][1])

    # For the final course
    if sum(visited) == len(input_arr) and input_arr[index][0] not in sorted_arr:
      #print("Not in :",input_arr[index][0])
      sorted_arr.append(input_arr[index][0])

def findMidpointCourse(arr):
    visited = [0] * len(arr)
    courses = []
    
    for i in range(len(arr)):
        if not visited[i]:
          # call the recursion
          sort_course_util(i, visited, courses, arr)
    
    for item in courses:
      print(item,end="-->")
        
# DO NOT MODIFY BELOW THIS LINE
if __name__ == "__main__":
  # Set the script dir as the working directory
  script_dir = os.path.dirname(os.path.realpath(sys.argv[0]))
  os.chdir(script_dir)

  pairs = []
  with open('input.txt') as in_f:
    for line in in_f:
      if len(line.strip()) == 0:
        continue
      pairs.append(line.rstrip().split(" "))

  findMidpointCourse(pairs)