'''
@Author: your name
@Date: 2020-01-16 16:25:50
@LastEditTime : 2020-01-17 09:31:56
@LastEditors  : Please set LastEditors
@Description: In User Settings Edit
'''

# 假设你正在爬楼梯。需要 n 阶你才能到达楼顶。

# 每次你可以爬 1 或 2 个台阶。你有多少种不同的方法可以爬到楼顶呢？

# 注意：给定 n 是一个正整数。

# 示例 1：

# 输入： 2
# 输出： 2
# 解释： 有两种方法可以爬到楼顶。
# 1.  1 阶 + 1 阶
# 2.  2 阶


# 题目的本质是个斐波那契数列，当前数值是前两个数值的和
# 动态规划
class Solution:
    def climbStairs(self, n: int) -> int:
        dp = [0] * (n+1)
        dp[1] = 1
        
        if n < 2:
            return dp[n]
        
        dp[2] = 2
        for i in range(3, n+1):
            dp[i] = dp[i-1] + dp[i-2]
            
        return dp[n]