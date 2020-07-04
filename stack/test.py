#!/usr/bin/env python3.6

from stack import Stack

class Test(Stack):

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
