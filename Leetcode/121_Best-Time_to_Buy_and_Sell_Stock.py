'''
@Author: your name
@Date: 2020-01-17 09:49:02
@LastEditTime : 2020-01-17 15:26:27
@LastEditors  : Please set LastEditors
@Description: In User Settings Edit
'''
# 给定一个数组，它的第 i 个元素是一支给定股票第 i 天的价格。

# 如果你最多只允许完成一笔交易（即买入和卖出一支股票），设计一个算法来计算你所能获取的最大利润。

# 注意你不能在买入股票前卖出股票。

# 示例 1:

# 输入: [7,1,5,3,6,4]
# 输出: 5
# 解释: 在第 2 天（股票价格 = 1）的时候买入，在第 5 天（股票价格 = 6）的时候卖出，最大利润 = 6-1 = 5 。
#      注意利润不能是 7-1 = 6, 因为卖出价格需要大于买入价格。
# 示例 2:

# 输入: [7,6,4,3,1]
# 输出: 0
# 解释: 在这种情况下, 没有交易完成, 所以最大利润为 0。
# class Solution:
#     def maxProfit(self, prices: List[int]) -> int:
#         if not prices:
#             return 0
        
#         cur_max_profit, cur_min = 0, prices[0]  # 初始化记录中最高利润和最小价格
#         for i in range(len(prices) - 1):
#             if prices[i] < cur_min:
#                 cur_min = prices[i]  # 更新记录中最小价格
            
#             cur_profit = prices[i+1] - cur_min  # 当前利润 = 当前价格 - 最小价格
            
#             if cur_profit > cur_max_profit:  #  如果当前利润大于记录中的最高利润
#                 cur_max_profit = cur_profit  # 更新记录中的最高利润
        
#         return cur_max_profit
    
    
import os


test_list = [7, 1, 5, 3, 6, 4]

final_value = 0

if len(test_list) == 0:
    final_value = 0

max_value = 0
min_value = 0
min_value = test_list[0]

for i in range(0, len(test_list)-1):
    if test_list[i] > test_list[i+1]:   ## find min
        min_value = min(min_value, test_list[i+1])
    else:
        max_value = max(max_value, test_list[i+1] - min_value)      ## find max
    print(i, test_list[i], min_value, max_value)
final_value = max_value
print("final_value is ", final_value)