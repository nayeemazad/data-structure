#!/usr/bin/env python3.6

from node import Node

class Test(Node):
    bst = Node(50)
    bst.insert(10)
    bst.insert(20)
    bst.insert(30)
    bst.insert(40)
    bst.insert(60)
    bst.insert(70)
    bst.insert(80)
    bst.insert(90)
    bst.insert(100)
    print('Pre order traversal:')
    bst.preorder()
    print('In order traversal:')
    bst.inorder()
    print('Post order traversal:')
    bst.postorder()
    print("Search Result for {}:{}".format(70, bst.contains(70)))
