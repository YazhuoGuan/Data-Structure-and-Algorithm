'''
@Description: In User Settings Edit
@Author: your name
@Date: 2019-10-14 08:20:50
@LastEditTime: 2019-10-14 09:16:38
@LastEditors: Please set LastEditors
'''
def binarySearch(theValues, target):
    low = 0
    high = len(theValues)-1
    
    while high >= low:
        mid = (low + high) // 2
        print(mid)
        if theValues[mid] == target:
            return True
        elif theValues[mid] > target:
            high = mid - 1
            print(theValues[low: high])
        else:
            low = mid + 1
            print(theValues[low: high])
    return False

sequence = [2, 4, 5, 10, 13, 18, 23, 29, 31, 51, 64]
target_value = 10
result = binarySearch(sequence, target_value)
print(result)