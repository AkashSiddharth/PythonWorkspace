from custom_queue import Queue

class Dequeue(Queue):
  def __init__(self):
    self.items = []
  
  def addFront(self, item):
    return self.items.insert(0, item)

  def addRear(self, item):
    return self.enqueue(item)
  
  def removeFront(self):
    return self.dequeue()
  
  def removeRear(self):
    return self.items.pop()

  def peek(self):
    for i, item in enumerate(self.items):
      if i == (self.size() - 1):
        print(item)
      else:
        print(item, end=", ")

if __name__ == "__main__":
  dqu = Dequeue()

  dqu.addFront(4)
  dqu.peek()
  print(dqu.size())
  dqu.addRear('Dog')
  dqu.peek()
  print(dqu.size())
  dqu.addFront(8.99)
  dqu.peek()
  dqu.addRear(False)
  dqu.peek()
  print(dqu.isEmpty())
  print(dqu.size())
  print(dqu)