
class Node:

    def __init__(self, data):
        self.left = None
        self.right = None
        self.data = data

    # function to insert new data
    def insert(self, data):

        if self.data:
            if data < self.data:
                if self.left is None:
                    self.left = Node(data)
                else:
                    self.left.insert(data)
            elif data > self.data:
                if self.right is None:
                    self.right = Node(data)
                else:
                    self.right.insert(data)
        else:
            self.data = data

    # function to search item
    def contains(self, data):
        if self.data == None:
            return False
        if data == self.data:
            return True
        if data < self.data:
            if self.left is None:
                return False
            return self.left.contains(data)
        elif data > self.data:
            if self.right is None:
                return False
            return self.right.contains(data)

    # function to inorder traversal
    def inorder(self):
        if self.left:
            self.left.inorder()
        print(self.data)
        if self.right:
            self.right.inorder()

    # function to preorder traversal
    def preorder(self):
        print(self.data),
        if self.left:
            self.left.preorder()
        if self.right:
            self.right.preorder()

    # function to postorder traversal
    def postorder(self):
        if self.left:
            self.left.preorder()
        if self.right:
            self.right.preorder()
        print(self.data),
