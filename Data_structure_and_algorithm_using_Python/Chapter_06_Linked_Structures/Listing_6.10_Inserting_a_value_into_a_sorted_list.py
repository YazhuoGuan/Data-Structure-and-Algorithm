'''
@Description: In User Settings Edit
@Author: your name
@Date: 2019-10-15 09:26:22
@LastEditTime: 2019-10-23 08:48:24
@LastEditors: Please set LastEditors
'''
class ListNode:
    def __init__(self, data):
        
        self.data = data
        self.next = None
        
        
def traversal(head):
    curNode = head
    while curNode is not None:
        print(curNode.data)
        curNode = curNode.next 
        
        
def inserting_node(head, target):
    curNode = head
    predNode = None
    while curNode is not None and curNode.data < target:
        predNode = curNode
        curNode = curNode.next
    newNode = ListNode(target)
    newNode.next = curNode
    if curNode is head:
        head = newNode
    else:
        predNode.next = newNode
    return head

head = ListNode(2)
a = ListNode(13)
b = ListNode(18)
c = ListNode(36)
d = ListNode(52)
head.next = a
a.next = b
b.next = c
c.next = d

result = inserting_node(head, 16)
print(traversal(result))