'''
@Author: your name
@Date: 2020-01-17 15:08:42
@LastEditTime : 2020-01-17 15:14:57
@LastEditors  : Please set LastEditors
@Description: In User Settings Edit
'''

# 给定一个链表，判断链表中是否有环。

# 为了表示给定链表中的环，我们使用整数 pos 来表示链表尾连接到链表中的位置（索引从 0 开始）。 如果 pos 是 -1，则在该链表中没有环。

#  

# 示例 1：

# 输入：head = [3,2,0,-4], pos = 1
# 输出：true

# 示意图： https://leetcode-cn.com/problems/linked-list-cycle/solution/dong-hua-yan-shi-141-huan-xing-lian-biao-by-user74/
class Solution(object):
    def hasCycle(self, head: ListNode) -> bool:
        if not (head and head.next):
            return False
        
        i, j = head, head.next
        
        while j and j.next:
            if i == j:
                return True
            i, j = i.next, j.next.next
        return False