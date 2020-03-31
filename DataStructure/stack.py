class Stack:
    # initialize the stack
    def __init__(self):
        self.items = []

    # Stack functions
    def push(self, item):
        ''' Add item to the top of the stack
            Item: Provide any value to put on the top of the stack '''
        # Complexity O(1)
        self.items.append(item)

        # Complexity O(n)
        # self.items.insert(0, item)
        return self.items

    def pop(self):
        ''' Return and remove the top item of the stack '''
        # Complexity O(1)
        return self.items.pop()
        # Complexity O(n)
        # return self.items.pop(0)

    def isEmpty(self):
        ''' Check and return Boolean, if the stack is empty '''
        return self.items == []

    def peek(self):
        ''' Show the top element of the stack.
            Does not pops the element from the stack. '''
        return self.items[0]

    def size(self):
        ''' Return the size of the stack '''
        return len(self.items)

if __name__ == "__main__":
    s = Stack()
    print(s.isEmpty())
    print(s.push(4))
    print(s.push('start'))
    print(s.peek())
    print(s.size())
    print(s.pop())
    print(s.isEmpty())
    print(s.size())  
