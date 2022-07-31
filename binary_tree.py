#Binary Tree implementation
class BinaryTree:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right
    def insert(self, value):
        if self.value:
            if value < self.value:
                if self.left is None:
                    self.left = BinaryTree(value)
                else:
                    self.left.insert(value)
            elif value > self.value:
                if self.right is None:
                    self.right = BinaryTree(value)
                else:
                    self.right.insert(value)
        else:
            self.value = value
    def delete(self, value):
        if self is None:
            return
        if value < self.value:
            self.left = self.left.delete(value)
        elif(value > self.value):
            self.right = self.right.delete(value)
        elif(value==self.value):
                self=None
    def isEmpty(self): 
        if self is None:   
            return False
        if self.left is None and self.right is None:
            return False
        if self.left is not None and self.right is not None:
            return (self.left.isEmpty() and self.right.isEmpty())
        
        return True
    def traversePreOrder(self):
        print(self.value, end=' ')
        if self.left:
            self.left.traversePreOrder()
        if self.right:
            self.right.traversePreOrder()
    def find(self, value):
        if value < self.value:
            if self.left is None:
                return False
            return self.left.find(value)
        elif value > self.value:
            if self.right is None:
                return False
            return self.right.find(value)
        else:
            return True
