'''
@Description: In User Settings Edit
@Author: your name
@Date: 2019-10-15 09:26:22
@LastEditTime: 2019-10-15 13:14:51
@LastEditors: Please set LastEditors
'''

class Bag:
    # Construct a bag
    def __init__(self, head):
        self._head = head
        self._size = 0

    # Returns the number of items in the bag.
    def __len__(self):
        return self._size
    
    # Determines if an item is contained in the bag.
    def __contains__(self, target):
        curNode = self._head
        while curNode is not None and curNode.item != target:
            curNode = curNode.next
        return curNode is not None
    
    # Adds a new item to the bag.
    def add(self, item):
        newNode = _BagListNode(item)
        newNode.next = self._head
        self._head = newNode
        self._size += 1
        
    # Removes an instance of item from the bag
    def remove(self, item):
        predNode = None
        curNode = self._head

        while curNode is not None and curNode.item != item:
            predNode = curNode
            curNode = curNode.next

        # The item has to be in the bag to remove it.
        assert curNode is not None, "The item must be in the bag!"
        self._size -= 1

        # Unlink the node and return the item.
        if curNode is self._head:
            self._head = curNode.next
        else:
            predNode.next = curNode.next
        
        return curNode.item
    
    # Returns a iterator for traversing the list of items.
    def __iter__(self):
        return _BagIterator(self._head)


# Defines a private storage class for creating list nodes.
class _BagListNode(object):
    def __init__(self, item):
        self.item = item
        self.next = None
        
class _BagIterator:
    def __init__(self, listHead):
        self._curNode = listHead
        
    def __iter__(self):
        return self
    
    def next(self):
        if self._curNode is None:
            raise StopIteration
        else:
            item = self._curNode.item
            self._curNode = self._curNode.next
            return item

