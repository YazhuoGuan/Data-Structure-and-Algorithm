'''
@Author: your name
@Date: 2020-01-21 15:15:17
@LastEditTime : 2020-01-21 17:13:04
@LastEditors  : Please set LastEditors
@Description: In User Settings Edit
'''
# 统计所有小于非负整数 n 的质数的数量。

# 示例:

# 输入: 10
# 输出: 4
# 解释: 小于 10 的质数一共有 4 个, 它们是 2, 3, 5, 7 。

# 不明白，时间长
class Solution:
    def countPrimes(self, n: int) -> int:
        if n < 2: return 0
        is_primes = [1] * n
        is_primes[0] = is_primes[1] = 0
        
        for i in range(2, int(n**0.5)+1):
            is_primes[i*i:n:i] = [0] * len(is_primes[i*i:n:i])
        return sum(is_primes)
