'''
@Author: your name
@Date: 2020-01-14 17:19:44
@LastEditTime : 2020-01-15 16:12:04
@LastEditors  : Please set LastEditors
@Description: In User Settings Edit
'''
# Implementation of the Queue ADT using a circular array.

from array import Array

class Queue:
    # Creates an empty queue.
    def __init__(self, maxSize):
        super().__init__()
        self._count = 0
        self._front = 0
        self._back = maxSize -1
        self._qArray = Array(maxSize)
    
    def isEmpty(self):
        return self._count == 0
    
    def isFull(self):
        return self._count == len(self._qArray)
    
    def __len__(self):
        return self._count
    
    def enqueue(self, item):
        assert not self.isFull(), 'Cannot insert an item to a full queue!'
        
        self._qArray
        
    def dequeue(self):
        assert not self.isEmpty(), 'Cannot dequeue from an empty queue.'
        return self._qList.pop(0)
    

a_queue = Queue()

a_queue.enqueue(1)
a_queue.enqueue(4)
a_queue.enqueue(6)
a_queue.enqueue(29)

print(a_queue.dequeue())