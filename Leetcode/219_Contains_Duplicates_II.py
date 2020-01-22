'''
@Author: your name
@Date: 2020-01-21 15:15:17
@LastEditTime : 2020-01-22 13:01:21
@LastEditors  : Please set LastEditors
@Description: In User Settings Edit
'''

class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        hash_dict = {}
        for idx, item in enumerate(nums):
            if item not in hash_dict.keys():
                hash_dict[item] = idx
            else:
                prev_idx = hash_dict[item]
                if (idx - prev_idx) <= k:
                    return True
                else:
                    hash_dict[item] = idx
        return False