class Solution(object):
    def maxSubArray(self, nums:list):
        res = 0
        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                res = max(res, sum(nums[i:j]))
        
        return res