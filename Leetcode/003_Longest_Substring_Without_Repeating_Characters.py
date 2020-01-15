'''
@Description: In User Settings Edit
@Author: Yazhuo
@Date: 2019-10-18 15:03:58
@LastEditTime: 2019-10-30 22:20:09
@LastEditors: Please set LastEditors
'''
# TODO: 理解代码含义
# 给定一个字符串，请你找出其中不含有重复字符的 最长子串 的长度。
class Solution(object):
    def lengthOfLongestSubstring(self, s: str) -> int:
        charmap = {}
        
        for i in range(256):
            charmap[i] = -1
        ls = len(s)
        i = max_len = 0
        
        for j in range(ls):
            # print(charmap[ord(s[j])])
            if charmap[ord(s[j])] >= i:
                i = charmap[ord(s[j])]  + 1
                print(i)
            charmap[ord(s[j])] = j
            max_len = max(max_len, j-i+1)
        # print(charmap)    
        return max_len
        
s = Solution()
result = s.lengthOfLongestSubstring("abcdc")
print(result)

