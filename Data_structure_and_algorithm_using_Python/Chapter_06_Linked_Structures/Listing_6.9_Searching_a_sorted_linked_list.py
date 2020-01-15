'''
@Description: In User Settings Edit
@Author: your name
@Date: 2019-10-15 09:26:22
@LastEditTime: 2019-10-15 15:06:09
@LastEditors: Please set LastEditors
'''
class ListNode:
    def __init__(self, data):
        
        self.data = data
        self.next = None

def sortedSearch(head, target):
    curNode = head
    while curNode is not None and curNode.data < target:
        if curNode.data == target:
            print('true:', curNode.data)
            return True
        else:
            print('false', curNode.data)
            curNode = curNode.next
    return False

a = ListNode(11)
b = ListNode(54)
tail = ListNode(90)
a.next = b
b.next = tail

result = sortedSearch(a, 11)
print(result)