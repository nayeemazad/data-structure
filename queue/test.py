#!/usr/bin/env python3.6

from queue import Queue

class Test(Queue):

    queue = Queue()
    queue.enqueue(10)
    print('enqueued 10')
    queue.enqueue(20)
    print('enqueued 20')
    queue.enqueue(30)
    print('enqueued 30')
    queue.display()

    print('Queue Size: {0}'.format(queue.getSize()))
    print('Front: {0}'.format(queue.getFront()))
    print('Tail: {0}'.format(queue.getTail()))

    item = queue.dequeue()
    print('Dequeued : {0}'.format(item))
    print('Queue Size: {0}'.format(queue.getSize()))
    print('Front: {0}'.format(queue.getFront()))
    print('Tail: {0}'.format(queue.getTail()))

    item = queue.dequeue()
    print('Dequeued : {0}'.format(item))
    print('Queue Size: {0}'.format(queue.getSize()))
    print('Front: {0}'.format(queue.getFront()))
    print('Tail: {0}'.format(queue.getTail()))

    item = queue.dequeue()
    print('Dequeued : {0}'.format(item))
    print('Queue Size: {0}'.format(queue.getSize()))

    print('isEmpty: {0}'.format(queue.isEmpty()))
