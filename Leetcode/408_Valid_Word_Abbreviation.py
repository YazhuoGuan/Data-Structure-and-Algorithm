'''
@Description: In User Settings Edit
@Author: your name
@Date: 2019-10-18 15:03:58
@LastEditTime: 2019-10-21 13:31:14
@LastEditors: Please set LastEditors
'''
# 罗马数字包含以下七种字符: I， V， X， L，C，D 和 M。将罗马数字转换为对应的阿拉伯数字
# 我的实现方法：
class Solution(object):
    def valid_word_abbr(self, word:str, abbr:str):
        pos, curr = 0, 0
        for i in range(len(abbr)):
            try:
                num = int(abbr[i])
                if num == 0 and curr == 0:
                    return False
                curr = curr * 10 + num
                print(num)
            except ValueError:
                pos += curr
                # print(pos)
                curr = 0
                if pos >= len(word):
                    return False
                if word[pos] != abbr[i]:
                    return False
                pos += 1
                
        pos += curr
        if pos == len(word):
            return True
        return False

if __name__ == '__main__':
    # begin
    s = Solution()
    print(s.valid_word_abbr("internationalization", "i12iz4n"))
