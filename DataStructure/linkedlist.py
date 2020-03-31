from node import Node

class UnorderedList:
    def __init__(self):
        self.head = self.tail = None
    
    def isEmpty(self):
        return self.head == None
    
    def add(self, item):
        temp = Node(item)
        temp.setNext(self.head)
        if self.tail == None:
            self.head = self.tail = temp
        else:
            self.head = temp

    def size(self):
        current = self.head
        length = 0
        while current != None:
            length += 1
            current = current.getNext()
        
        return length
    
    def search(self, item):
        current = self.head
        while current != None:
            if current.getData() == item:
                return True
            current = current.getNext()
        return False

    def remove(self, item):
        current = self.head
        previous = None
        found = False

        while not found:
            if current.getData == item:
                found = True
            else:
                previous = current
                current = current.getNext()
            
        if previous == None:
            self.head = current.getNext()
        else:
            previous.setNext(current.getNext())

    def insert(self, pos, item):
        try:
            if pos > self.size():
                raise IndexError

            temp = Node(item)
            current = self.head
            previous = None

            for i in range(pos):
                previous = current
                current = current.getNext()

            # insert the node
            previous.setNext(temp)
            temp.setNext(current)
        except IndexError as e:
            print(e)
    
    def append(self, item):
        if self.head == None:
            # List is empty
            self.add(item)
        else:
            current = self.tail
            temp = Node(item)
            current.setNext(temp)
            self.tail = temp

    def index(self, item):
        current = self.head
        found = False
        counter = 0

        while not found:
            if current.getData() == item:
                found = True

            counter += 1

        return counter

    def print_list(self):
        current = self.head

        while current.getNext() != None:
            print(current.getData(), end=' --> ')
            current = current.getNext()
        
        print(current.getData())

if __name__ == "__main__":
    mylist = UnorderedList()

    mylist.add(31)
    mylist.add(77)
    mylist.add(17)
    mylist.add(93)
    mylist.add(26)
    mylist.add(54)

    print(mylist.size())
    mylist.print_list()

    mylist.append(22)
    print(mylist.size())
    mylist.print_list()

    mylist.insert(4, 87)
    print(mylist.size())
    mylist.print_list()