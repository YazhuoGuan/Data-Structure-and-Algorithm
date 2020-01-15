'''
@Description: In User Settings Edit
@Author: your name
@Date: 2019-10-18 15:03:58
@LastEditTime: 2019-10-18 17:02:38
@LastEditors: Please set LastEditors
'''
# 罗马数字包含以下七种字符: I， V， X， L，C，D 和 M。将罗马数字转换为对应的阿拉伯数字
# 我的实现方法：
class Solution(object):
    def romanToInt(self, s:str):
        roman_num_dict = {'I':1, 'V':5, 'X':10, 'L':50, 'C':100, 'D':500, 'M':1000}
        prev, total = 0, 0
        i = 0
        for character in s:
            i += 1
            curr = roman_num_dict[character]
            total += curr
            if curr > prev:
                total -= 2 * prev
            print('第{}次：curr = {}, prev = {}'.format(i, curr, prev))
            prev = curr
            
        return total
    
if __name__ == '__main__':
    # begin
    s = Solution()
    print(s.romanToInt('MCMXCIV'))
