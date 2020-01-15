'''
@Description: In User Settings Edit
@Author: your name
@Date: 2019-10-15 09:26:22
@LastEditTime: 2019-10-15 14:51:05
@LastEditors: Please set LastEditors
'''
class ListNode:
    def __init__(self, data):
        
        self.data = data
        self.next = None

def removingNode(item, head, tail):
    preNode = None
    curNode = head
    
    while curNode is not None and curNode.value != item:
        preNode = curNode
        curNode = curNode.next
    
    if curNode is not None:
        if curNode is head:
            head = curNode
        else:
            preNode.next = curNode.next
        
        if curNode is tail:
            tail = preNode

def traversal(head):
    curNode = head
    while curNode is not None:
        print(curNode.data)
        curNode = curNode.next 

a = ListNode(11)
b = ListNode(54)
tail = ListNode(90)
a.next = b
b.next = tail

head = appendingNode(62, a, tail)
result = traversal(head)
print(result)