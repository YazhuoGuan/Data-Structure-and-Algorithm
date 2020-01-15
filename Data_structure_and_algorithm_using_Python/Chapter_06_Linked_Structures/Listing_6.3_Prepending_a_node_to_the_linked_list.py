'''
@Description: In User Settings Edit
@Author: your name
@Date: 2019-10-15 09:26:22
@LastEditTime: 2019-10-15 10:19:22
@LastEditors: Please set LastEditors
'''
class ListNode:
    def __init__(self, data):
        
        self.data = data
        self.next = None

def prependingItem(item, head):
    newNode = ListNode(item)
    newNode.next = head
    head = newNode
    return head

def traversal(head):
    curNode = head
    while curNode is not None:
        print(curNode.data)
        curNode = curNode.next 

a = ListNode(11)
b = ListNode(54)
c = ListNode(90)
a.next = b
b.next = c

head = prependingItem(62, a)
result = traversal(head)
print(result)