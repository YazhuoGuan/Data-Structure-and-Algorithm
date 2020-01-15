'''
@Description: In User Settings Edit
@Author: your name
@Date: 2019-10-18 15:03:58
@LastEditTime: 2019-10-18 15:23:00
@LastEditors: Please set LastEditors
'''
# 判断一个整数是否是回文数。回文数是指正序（从左向右）和倒序（从右向左）读都是一样的整数。
# 我的实现方法：双指针，前后双向遍历，判断是否相同，不相同直接返回false，相同继续循环，知道循环结束。
class Solution(object):
    def is_palindrome(self, x):
        if x < 0: # -121 反过来是 121-，正反是不一样的
            return False
        else:
            list_x = list(str(x))
            front = 0
            tail = len(list_x)-1
            
            while front < tail:
                if list_x[front] != list_x[tail]:
                    return False
                else:
                    front += 1
                    tail -= 1
            return True
             
if __name__ == '__main__':
    # begin
    s = Solution()
    print(s.is_palindrome(10))