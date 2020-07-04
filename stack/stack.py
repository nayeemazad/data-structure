#!/usr/bin/env python3.6

class Node:

    def __init__(self, data):
       self.data = data
       self.next = None

class Stack:

    def __init__(self):
        self.head = None

    # Function to check if stack is empty
    def isEmpty(self):
        return self.head == None

    # Function to push element to stack
    def push(self, data):
        if self.isEmpty() == True:
            self.head = Node(data)
        else:
            newNode = Node(data)
            newNode.next = self.head
            self.head = newNode

    # Function to pop element from stack
    def pop(self):
        if self.isEmpty() == True:
            return None
        else:
            popped = self.head.data
            self.head = self.head.next
            return popped

    # Function to return top element of stack
    def peek(self):
        if self.isEmpty() == True:
            return None
        else:
            return self.head.data

    # Function to get size of the stack
    def getSize(self):
        count = 0
        if self.isEmpty() == True:
            return count
        else:
            temp = self.head
            while temp is not None:
                count += 1
                temp = temp.next
            return count

    # Function to print elements of the stack
    def display(self):
        if self.isEmpty() == True:
            print("Stack is empty.")
        else:
            temp = self.head
            while temp is not None:
                print(temp.data, end ="->")
                temp = temp.next
            print('')

    # Function to find an element in the stack
    def find(self, key):
        if self.isEmpty() == True:
            return None
        else:
            temp = self.head
            position = 0
            while temp is not None:
                position += 1
                if (temp.data == key):
                    return position
                temp = temp.next
        return None

# TEST
stack = Stack()
stack.push(10)
stack.push(20)
stack.push(30)
stack.push(40)
stack.push(50)
stack.push(100)
stack.display()
print("Stack size: {0}".format(stack.getSize()))
popped = stack.pop()
if popped == None:
    print('Stack is empty.')
else:
    print('Just popped: {0}'.format(popped))

stack.display()
print("Stack size: {0}".format(stack.getSize()))

peek = stack.peek()
if peek == None:
    print('Stack is empty.')
else:
    print('Peek: {0}'.format(peek))

item = 10
position = stack.find(item)
if position == None:
    print('Oh,snap! {0} does not exist in the stack.'.format(item))
else:
    print('{0} is at position {1}'.format(item, position))

item = 150
position = stack.find(item)
if position == None:
    print('Oh,snap! {0} does not exist in the stack.'.format(item))
else:
    print('{0} is at position {1}'.format(item, position))



