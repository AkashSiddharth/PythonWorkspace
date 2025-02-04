''' # List Implementation
def binaryTree(node):
    return [node, [], []]

def getRoot(tree):
    return tree[0]

def setRoot(tree, newVal):
    tree[0] = newVal

def insertLeftChild(root, node):
    lc = root.pop(1)
    if len(lc) > 1:
        root.insert(1, [node, lc, []])
    else:
        root.insert(1, [node, [], []])
    
    return root
        
def getLeftChild(tree):
    return tree[1]

def insertRightChild(root, node):
    rc = root.pop(2)

    if len(rc) > 1:
        root.insert(2, [node, rc, []])
    else:
        root.insert(2, [node, [], []])
    
    return root

def getRightChild(tree):
    return tree[2]

def buildTree():
    root = binaryTree('a')
    insertLeftChild(root, 'b')
    insertRightChild(root, 'c')
    insertRightChild(getLeftChild(root),'d')
    insertLeftChild(getRightChild(root),'e')
    insertRightChild(getRightChild(root),'f')

    return root

x = binaryTree('a')
insertLeftChild(x,'b')
insertRightChild(x,'c')
insertRightChild(getRightChild(x),'d')
insertLeftChild(getRightChild(getRightChild(x)),'e')

ttree = buildTree()
print(ttree)
'''

class BinaryTree:
    def __init__(self, rootVal):
        self.key = rootVal
        self.leftChild = None
        self.rightChild = None
    
    def getRoot(self):
        return self.key
    
    def getLeftChild(self):
        return self.leftChild
    
    def getRightChild(self):
        return self.rightChild
    
    def setRoot(self, newVal):
        self.key = newVal
    
    def insertLeft(self, node):
        if self.leftChild == None:
            self.leftChild = BinaryTree(node)
        else:
            temp = BinaryTree(node)
            temp.leftChild = self.leftChild
            self.leftChild = temp

    def insertRight(self, node):
        if self.rightChild == None:
            self.rightChild = BinaryTree(node)
        else:
            temp = BinaryTree(node)
            temp.rightChild = self.leftChild
            self.rightChild = temp


def buildTree():
    r = BinaryTree('a')
    r.insertLeft('b')
    r.getLeftChild().insertRight('d')
    r.insertRight('c')
    r.getRightChild().insertLeft('e')
    r.getRightChild().insertRight('f')
    return r

if __name__ == "__main__":
    '''r = BinaryTree('a')
    print(r.getRoot())
    print(r.getLeftChild())
    r.insertLeft('b')
    print(r.getLeftChild())
    print(r.getLeftChild().getRoot())
    r.insertRight('c')
    print(r.getRightChild())
    print(r.getRightChild().getRoot())
    r.getRightChild().setRoot('hello')
    print(r.getRightChild().getRoot())'''
    ttree = buildTree()
