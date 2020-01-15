'''
@Description: In User Settings Edit
@Author: your name
@Date: 2019-10-15 09:26:22
@LastEditTime: 2019-10-15 10:07:34
@LastEditors: Please set LastEditors
'''
class ListNode:
    def __init__(self, data):
        
        self.data = data
        self.next = None
 
def unorderedSearch(head, target):
    curNode = head
    while curNode is not None and curNode.data != target:
        curNode = curNode.next 
    return curNode is not None

a = ListNode(11)
b = ListNode(54)
c = ListNode(90)

a.next = b
b.next = c
result = unorderedSearch(a, 12)
print(result)