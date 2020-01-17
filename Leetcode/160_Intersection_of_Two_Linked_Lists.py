'''
@Author: your name
@Date: 2020-01-17 15:57:22
@LastEditTime : 2020-01-17 16:05:58
@LastEditors  : Please set LastEditors
@Description: In User Settings Edit
'''
# 编写一个程序，找到两个单链表相交的起始节点。

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

# 拼接链表以弥补长度差
class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
        ha,hb = headA, headB
        
        while ha != hb:
            ha = ha.next if ha else headB
            hb = hb.next if hb else headA

        return ha