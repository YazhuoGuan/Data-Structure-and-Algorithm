'''
@Author: your name
@Date: 2020-01-16 11:15:49
@LastEditTime : 2020-01-16 13:01:39
@LastEditors  : Please set LastEditors
@Description: In User Settings Ed
'''
# 给定一个排序数组和一个目标值，在数组中找到目标值，并返回其索引。
# 如果目标值不存在于数组中，返回它将会被按顺序插入的位置。

# 你可以假设数组中无重复元素。

# 输入: [1,3,5,6], 5
# 输出: 2

class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        left, right = 0, len(nums)-1  # 初始化左右端点位置 
        
        while left <= right:  # 当条件合法时
            mid = left + (left + right) // 2  # 获取中点，如果是偶数取靠左位置
            if nums[mid] == target:  # 找到该数
                return mid  # 直接返回
            elif nums[mid] > target:  # 如果当前位置数比插入值大
                right = mid - 1  # 更新右端点
            elif nums[mid] < target:  # 如果当前位置比插入值小
                left = mid + 1  # 更新左端点
            
            return left  # 返回插入点位置，这里是左端位置

