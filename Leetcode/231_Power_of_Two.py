'''
@Author: your name
@Date: 2020-01-16 16:25:50
@LastEditTime : 2020-01-22 11:04:57
@LastEditors  : Please set LastEditors
@Description: In User Settings Edit
'''

# 给定一个整数，编写一个函数来判断它是否是 2 的幂次方。

# 示例 1:

# 输入: 1
# 输出: true
# 解释: 20 = 1
# 示例 2:

# 输入: 16
# 输出: true
# 解释: 24 = 16
# 示例 3:

# 输入: 218
# 输出: false

# 采用位运算
# 解题思路：https://leetcode-cn.com/problems/power-of-two/solution/power-of-two-er-jin-zhi-ji-jian-by-jyd/

class Solution：
    def isPowerOfTwo(self, n: int) -> bool:
        # 如果是 2 的幂，n 与 n-1 的 ‘按位相与’ 的结果是 0
        return n > 0 and n & (n-1) == 0
