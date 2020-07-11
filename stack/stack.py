#!/usr/bin/env python3.6

from node import Node

class Stack(Node):

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
            position = 1
            current = self.head
            if current.data == key:
                return position
            while current.next is not None:
                position += 1
                if (current.next.data == key):
                    return position
                current = current.next
        return None
