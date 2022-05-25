class Queue:
  def __init__(self):
    self.items = []
  
  def isEmpty(self):
    return self.items == []
  
  def enqueue(self, item):
    self.items.append(item)
  
  def dequeue(self):
    return self.items.pop(0)
  
  def size(self):
    return len(self.items)
  
  def __str__(self):
    return "Queue({})".format(' '.join((map(str, self.items))))

if __name__ == "__main__":
  q = Queue()
  q.enqueue(4)
  q.enqueue('Dog')
  q.enqueue(8.099)
  print(q)
  print(q.size())
  print(q.dequeue())
