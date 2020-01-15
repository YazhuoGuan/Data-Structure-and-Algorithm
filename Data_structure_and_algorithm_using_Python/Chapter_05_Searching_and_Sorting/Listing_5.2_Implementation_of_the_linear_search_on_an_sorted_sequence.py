'''
@Description: In User Settings Edit
@Author: your name
@Date: 2019-10-14 08:20:50
@LastEditTime: 2019-10-14 08:28:43
@LastEditors: Please set LastEditors
'''
def linearSearch(theValues, target):
    n = len(theValues)
    for i in range(n):
        if theValues[i] == target:
            return True
        elif theValues[i] > target:
            return False
    return False


sequence = [2, 4, 5, 10, 13, 18, 23, 29, 31, 51, 64]
target_value = 8
result = linearSearch(sequence, target_value)