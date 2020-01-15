'''
@Description: In User Settings Edit
@Author: your name
@Date: 2019-10-15 09:26:22
@LastEditTime: 2019-10-15 09:29:23
@LastEditors: Please set LastEditors
'''
class ListNode:
    def __init__(self, data):
        
        self.data = data
        self.next = None
        
a = ListNode(11)
b = ListNode(54)
c = ListNode(90)

a.next = b
b.next = c

print(a.data)
print(a.next.data)
print(a.next.next.data)        