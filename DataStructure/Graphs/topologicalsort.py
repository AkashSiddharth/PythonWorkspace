import sys
  
#Class to represent a graph
class Course: 
    def __init__(self): 
        self.graph = dict()
 
    def add(self,u,v):
        self.graph[u] = v
 
    def courseSortUtil(self,v,visited, stack): 
        # Mark the current node as visited. 
        visited[v] = True

        # get the value at v
        for i, key in enumerate(self.graph.keys()):
            if i == v:
                current_key = key
                next_key = self.graph[key]

        # Recur for all the vertices adjacent to this vertex 
        for i, value in enumerate(self.graph.values()):
            if value == next_key and visited[i] == False: 
                self.courseSortUtil(i,visited, stack)
  
        # Push current vertex to stack which stores result 
        stack.insert(0,next_key)
 
    def courseSort(self):
        stack = []

        vertices = len(self.graph.keys())
        # Mark all the vertices as not visited 
        visited = [False]*vertices

        for i in range(vertices): 
            if visited[i] == False:
                self.courseSortUtil(i, visited, stack) 
  
        # Print contents of the stack 
        length = len(stack)
        tp = (length //2) - 1 if length % 2 == 0 else (length // 2)
        return (stack[tp])

# accept input
if __name__ == "__main__":
    course = Course()
    for line in sys.stdin:
        classes = line.strip().split()
        course.add(classes[0], classes[1])
    
    print(course.courseSort())

'''
#Python
import sys

def courseSortUtil(v,visited, stack, pairs): 
  # Mark the current node as visited. 
  visited[v] = True

  # Recur for all the vertices adjacent to this vertex 
  for i in pairs:
    if visited[i] == False: 
       courseSortUtil(i,visited, stack, pairs)

  # Push current vertex to stack which stores result 
  stack.insert(0, pairs[v][0])
  
def findMidpointCourse(pairs):
  stack = []
  # Mark all the vertices as not visited 
  visited = [False]*len(pairs)

  for i in range(len(pairs)): 
     if visited[i] == False:
        courseSortUtil(i, visited, stack, pairs) 

  # Print contents of the stack 
  length = len(stack)
  tp = (length //2) - 1 if length % 2 == 0 else (length // 2)
  stack.reverse()
  print(stack)
  return stack[tp]

# DO NOT MODIFY BELOW THIS LINE
def main():
  pairs = []

  for line in sys.stdin:
    if len(line.strip()) == 0:
      continue

    line = line.rstrip()

    pairs.append(line.split(" "))

  print(findMidpointCourse(pairs))

main()
'''