'''
@Author: your name
@Date: 2020-01-16 10:41:03
@LastEditTime : 2020-01-16 11:13:44
@LastEditors  : Please set LastEditors
@Description: In User Settings Edit
'''
# 将两个有序链表合并为一个新的有序链表并返回。新链表是通过拼接给定的两个链表的所有节点组成的。
# 输入：1->2->4, 1->3->4
# 输出：1->1->2->3->4->4

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def mergeTwoLists(self, l1:ListNode, l2:ListNode) -> ListNode:
        h = ListNode(-1)
        cur = h
        
        cur1 = l1
        cur2 = l2
        
        while cur1 != None and cur2 != None:
            if cur1.val <= cur2.val:
                cur.next = cur1
                cur1 = cur1.next
            
            else:
                cur.next = cur2
                cur2 = cur2.next
            
            cur = cur.next
        # 上述循环结束后，可能有一个不为空 
        if cur1 != None:
            cur.next = cur1
        
        if cur2 != None:
            cur.next = cur2
        
        return h.next
