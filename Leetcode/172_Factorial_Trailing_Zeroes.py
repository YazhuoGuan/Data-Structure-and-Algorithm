'''
@Author: your name
@Date: 2020-01-16 16:25:50
@LastEditTime : 2020-01-21 11:15:15
@LastEditors  : Please set LastEditors
@Description: In User Settings Edit
'''

# 给定一个整数 n，返回 n! 结果尾数中零的数量。

# 示例 1:

# 输入: 3
# 输出: 0
# 解释: 3! = 6, 尾数中没有零。
# 示例 2:

# 输入: 5
# 输出: 1
# 解释: 5! = 120, 尾数中有 1 个零.

class Solution:
    # 有多少个 5，就有多少个 0。每五个数有一个 5，每 25 个数有两个 5，每 125 个数有三个 5 ……
    def trailingZeroes(self, n: int) -> int:
        res = 0
        
        while n > 0:
            n //= 5
            res += n
        
        return res