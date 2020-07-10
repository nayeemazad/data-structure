#!/usr/bin/env python3.6

from node import Node

class LinkedList(Node):

    def __init__(self):
        self.head = None

    # Function to check if list is empty
    def isEmpty(self):
        return self.head == None

    # Function to append value to list
    def append(self, data):
        if self.isEmpty() == True:
            self.head = Node(data)
        else:
            current = self.head
            while current.next is not None:
                current = current.next
            current.next = Node(data)

    # Function to prepend value to list
    def prepend(self, data):
        if self.isEmpty() == True:
            self.head = Node(data)
        else:
            newNode = Node(data)
            newNode.next = self.head
            self.head = newNode

    # Function to print list
    def display(self):
        if self.isEmpty() == True:
            print("List is empty.")
        else:
            current = self.head
            while current is not None:
                print(current.data, end ="->")
                current = current.next
            print('')

    # Function to find an element in list
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

    # Function to delete an element in list
    def deleteItem(self, key):
        if self.isEmpty() == True:
            return None
        else:
            current = self.head
            if current.data == key:
                self.head = self.head.next
                return
            while current.next is not None:
                if (current.next.data == key):
                    current.next = current.next.next
                    return
                current = current.next
            return None
