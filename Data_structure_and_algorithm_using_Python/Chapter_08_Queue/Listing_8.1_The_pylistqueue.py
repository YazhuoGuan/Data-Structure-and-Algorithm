'''
@Author: your name
@Date: 2020-01-14 17:19:44
@LastEditTime : 2020-01-15 14:12:04
@LastEditors  : Please set LastEditors
@Description: In User Settings Edit
'''
# Implementation of the Queue ADT using a Python list.
class Queue:
    # Creates an empty queue.
    def __init__(self):
        super().__init__()
        self._qList = list()
    
    def isEmpty(self):
        return len(self) == 0
    
    def __len__(self):
        return len(self._qList)
    
    def enqueue(self, item):
        self._qList.append(item)
        
    def dequeue(self):
        assert not self.isEmpty(), 'Cannot dequeue from an empty queue.'
        return self._qList.pop(0)
    

a_queue = Queue()

a_queue.enqueue(1)
a_queue.enqueue(4)
a_queue.enqueue(6)
a_queue.enqueue(29)

print(a_queue.dequeue())