'''
@Author: your name
@Date: 2020-01-16 16:25:50
@LastEditTime : 2020-01-17 09:46:21
@LastEditors  : Please set LastEditors
@Description: In User Settings Edit
'''

# 斐波那契数，通常用 F(n) 表示，形成的序列称为斐波那契数列。该数列由 0 和 1 开始，后面的每一项数字都是前面两项数字的和。也就是：

# F(0) = 0,   F(1) = 1
# F(N) = F(N - 1) + F(N - 2), 其中 N > 1.
# 给定 N，计算 F(N)。

#  

# 示例 1：

# 输入：2
# 输出：1
# 解释：F(2) = F(1) + F(0) = 1 + 0 = 1.


# 
class Solution:
    def fib(self, N: int) -> int:
        fib_array = [0] * (N+1)
        if N == 0:
            return 0
        
        fib_array[1] = 1
        if N == 1:
            return 1
        
        for i in range(2, N+1):
            print(i-1)
            print(i-2)
            fib_array[i] = fib_array[i-1] + fib_array[i-2]
            
        return fib_array[N]
    
    # 别人的做法
    def fib(self, N: int) -> int:
        temp = [0,1]
        if N >= 2:
            for i in range(2,N+1):
                temp[i%2] = temp[0] + temp[1]
        return temp[N%2]

