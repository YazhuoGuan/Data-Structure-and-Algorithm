'''
@Description: In User Settings Edit
@Author: your name
@Date: 2019-10-14 08:20:50
@LastEditTime: 2019-10-14 08:20:50
@LastEditors: your name
'''
def linearSearch(theValues, target):
    n = len(theValues)
    for i in range(n):
        if theValues[i] == target:
            return True
        
    return False