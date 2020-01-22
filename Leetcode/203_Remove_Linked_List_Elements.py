'''
@Author: your name
@Date: 2020-01-16 16:25:50
@LastEditTime : 2020-01-21 14:18:25
@LastEditors  : Please set LastEditors
@Description: In User Settings Edit
'''

# 删除链表中等于给定值 val 的所有节点。

# 示例:

# 输入: 1->2->6->3->4->5->6, val = 6
# 输出: 1->2->3->4->5

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


# 方法：哨兵节点
# 如果删除的节点是中间的节点，则问题似乎非常简单：

# 选择要删除节点的前一个结点 prev。
# 将 prev 的 next 设置为要删除结点的 next。

# 当要删除的一个或多个节点位于链表的头部时，事情会变得复杂。
# 可以通过哨兵节点去解决它，哨兵节点广泛应用于树和链表中，如伪头、伪尾、标记等，它们是纯功能的，通常不保存任何数据，其主要目的是使链表标准化，如使链表永不为空、永不无头、简化插入和删除。
# 在这里哨兵节点将被用于伪头。

# 算法：
# 初始化哨兵节点为 ListNode(0) 且设置 sentinel.next = head。
# 初始化两个指针 curr 和 prev 指向当前节点和前继节点。
# 当 curr != nullptr：
# 比较当前节点和要删除的节点：
# 若当前节点就是要删除的节点：则 prev.next = curr.next。
# 否则设 prve = curr。
# 遍历下一个元素：curr = curr.next。
# 返回 sentinel.next。

class Solution:
    def removeElements(self, head: ListNode, val: int) -> ListNode:
        sentinel = ListNode(0)
        sentinel.next = head
        prev, curr = sentinel, head
        
        while curr:
            if curr.val == val:
                prev.next = curr.next
            else:
                prev = curr
            
            curr = curr.next
        
        return sentinel.next