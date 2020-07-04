#!/usr/bin/env python3.6

from node import Node

class Queue(Node):
    def __init__(self):
        self.head = None
        self.tail = None

    # Function to check if queue is empty
    def isEmpty(self):
        return self.head == None

    # Function to enqueue
    def enqueue(self, data):
        if self.isEmpty() == True:
            self.head = Node(data)
            self.tail = self.head
        else:
            self.tail.next = Node(data)
            self.tail = self.tail.next

    # Function to dequeue
    def dequeue(self):
        if self.isEmpty() == True:
            return None
        else:
            item = self.head.data
            self.head = self.head.next
            return item

    # Function to get size of queue
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
            print("Queue is empty.")
        else:
            print('Queue:')
            temp = self.head
            while temp is not None:
                print(temp.data, end ="->")
                temp = temp.next
            print('')

    # Function to get front
    def getFront(self):
        if self.isEmpty() == True:
            return None
        else:
            return self.head.data

    # Function to get tail
    def getTail(self):
        if self.isEmpty() == True:
            return None
        else:
            return self.tail.data
