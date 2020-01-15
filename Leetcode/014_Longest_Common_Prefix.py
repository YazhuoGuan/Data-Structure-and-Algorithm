'''
@Description: In User Settings Edit
@Author: your name
@Date: 2019-10-18 15:03:58
@LastEditTime: 2019-10-21 10:57:36
@LastEditors: Please set LastEditors
'''
# 罗马数字包含以下七种字符: I， V， X， L，C，D 和 M。将罗马数字转换为对应的阿拉伯数字
# 我的实现方法：
class Solution(object):
    def longest_common_prefix(self, str_list: list):
        lengths = [len(item) for item in str_list]
        
        min_length = min(lengths)
        
        common_prefix_list = []
        for i in range(min_length):
            prefix_i = [character[i] for character in str_list]
            print(set(prefix_i))
            if len(set(prefix_i)) == 1:
                common_prefix_list.append(prefix_i[0])
            else:
                break
        
        common_prefix = ''.join(common_prefix_list)
        return common_prefix
                

if __name__ == '__main__':
    # begin
    s = Solution()
    list_str = ["aca","cba"]
    print(s.longest_common_prefix(list_str))
