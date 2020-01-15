'''
@Description: In User Settings Edit
@Author: your name
@Date: 2019-10-15 09:26:22
@LastEditTime: 2019-10-15 11:04:16
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


def removingItem(target, head):
    predNode = None
    curNode = head
    
    while curNode is not None and curNode.data != target:
        predNode = curNode
        curNode = curNode.next
        
    if curNode is not None:
        if curNode is head:
            head = curNode.next
        else:
            predNode.next = curNode.next
            
    result = traversal(head)
    return result


a = ListNode(96)
b = ListNode(2)
c = ListNode(52)
d = ListNode(18)
e = ListNode(36)
f = ListNode(13)
a.next = b
b.next = c
c.next = d
d.next = e
e.next = f

original_linked_list = traversal(a)
print('original_linked_list:{}'.format(original_linked_list))
after_deletion = removingItem(18, a)
print('after_deletion: {}'.format(after_deletion))