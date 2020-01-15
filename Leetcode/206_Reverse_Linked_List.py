    
# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None
        
        
class Solution(object):
    def reverse_list(self, head):
        # simply iteratively without extra space, 要记录当前位置，前一位置，后一位置
        prev, curr = None, head
        
        while curr is not None:
            next_tmp = curr.next  # 存下下一位置
            curr.next = prev  # 当前位置指向前一位置
            prev = curr  # prev 前移一位
            curr = next_tmp  # curr 前移一位
        return prev    

s = Solution()
linked_list = 
