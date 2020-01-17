'''
@Author: your name
@Date: 2020-01-16 16:25:50
@LastEditTime : 2020-01-17 09:05:00
@LastEditors  : Please set LastEditors
@Description: In User Settings Edit
'''


# 一次遍历法
# 动态图解：https://leetcode-cn.com/problems/remove-duplicates-from-sorted-list/solution/dong-hua-yan-shi-83-shan-chu-pai-xu-lian-biao-zhon/
class Solution:
    def deleteDuplicates(self, head):
        if not (head and head.next):
            return head
        
        i, j = head, head
        while j:
            if i.val != j.val:
                i = i.next
                i.val = j.val
            j = j.next
        
        i.next = None
        return head
            