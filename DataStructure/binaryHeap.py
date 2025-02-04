''' 
This is a min heap. Array representation of a heap formed from [5,9,11,14,18,19,21,33,17,27]
    ----------------------------------------------------------------------
    | 0 | 5 | 9 | 11 | 14 | 18 | 19 | 21 | 33 | 17 | 27 |
    ----------------------------------------------------------------------
      0   1   2   3    4    5    6    7    8    9    10
'''

class BinaryHeap:
    def __init__(self):
        self.heapList = [0]
        self.currentSize = 0
    
    def __precUp(self, i):
        # for any item at index i , its root will always be at i // 2,
        # since for any node i , left child is at 2i and right child is at 2i+1
        while i // 2 > 0:
            if self.heapList[i] < self.heapList[i // 2]:
                # swap
                tmp = self.heapList[i]
                self.heapList[i] = self.heapList[i // 2]
                self.heapList[i // 2] = tmp
            i = i // 2
    
    def insert(self, elem):
        self.heapList.append(elem)
        self.currentSize += 1
        self.__precUp(self.currentSize)
    
    def __precDown(self, i):
        while i * 2 <= self.currentSize:
            mc = self.__minChild(i)
            # swap the root with min child
            if self.heapList[i] >  self.heapList[mc]:
                tmp = self.heapList[i]
                self.heapList[i] = self.heapList[mc]
                self.heapList[mc] = tmp
            i = mc
    
    def __minChild(self, i):
        if 2 * i + 1 > self.currentSize:
            return i * 2
        else:
            return (i * 2) if (self.heapList[2*i] < self.heapList[2 * i + 1]) else (i * 2 + 1)

    def delMin(self):
        # set return value
        ret_val = self.heapList[1]

        # get the last element to the root value
        self.heapList[1] = self.heapList[self.currentSize - 1]

        # remove the last element
        self.heapList.pop()

        # maintain the heap property
        self.__precDown(1)

        return ret_val

    def buildHeap(self, alist):
        self.currentSize = self.currentSize + len(alist)
        self.heapList = self.heapList + alist
        i = self.currentSize // 2
        while i > 0:
            self.__precDown(i)
            i -= 1

if __name__ == "__main__":
    bh = BinaryHeap()
    