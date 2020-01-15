'''
@Description: In User Settings Edit
@Author: your name
@Date: 2019-10-15 09:26:22
@LastEditTime: 2019-10-15 13:28:23
@LastEditors: Please set LastEditors
'''
class ListNode:
    def __init__(self, data):
        
        self.data = data
        self.next = None

def appendingNode(item, head, tail):
    newNode = ListNode(item)
    if head is None:
        head = newNode
    else:
        tail.next = newNode
    tail = newNode
    print(traversal(head))

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