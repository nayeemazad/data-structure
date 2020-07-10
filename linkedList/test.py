#!/usr/bin/env python3.6

from linkedList import LinkedList

class Test(LinkedList):

    linkedList = LinkedList()
    linkedList.append(10)
    linkedList.append(20)
    linkedList.append(30)
    linkedList.append(40)
    linkedList.append(50)
    linkedList.append(100)
    linkedList.display()
    linkedList.prepend(200)
    linkedList.display()

    item = 200
    position = linkedList.find(item)
    if position == None:
        print('Oh,snap! {0} does not exist in the linkedList.'.format(item))
    else:
        print('{0} is at position {1}'.format(item, position))

    print('deleting 200 from list')
    linkedList.deleteItem(200)
    linkedList.display()

    print('deleting 50 from list')
    linkedList.deleteItem(50)
    linkedList.display()

    item = 150
    position = linkedList.find(item)
    if position == None:
        print('Oh,snap! {0} does not exist in the linkedList.'.format(item))
    else:
        print('{0} is at position {1}'.format(item, position))
