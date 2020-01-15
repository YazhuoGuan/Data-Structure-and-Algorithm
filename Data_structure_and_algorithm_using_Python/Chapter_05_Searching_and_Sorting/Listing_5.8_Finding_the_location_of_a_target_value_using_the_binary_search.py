'''
@Description: In User Settings Edit
@Author: your name
@Date: 2019-10-14 08:20:50
@LastEditTime: 2019-10-15 08:40:10
@LastEditors: Please set LastEditors
'''
def findOrderedPosition(theList, target):
    low = 0
    high = len(theList) - 1

    while low <= high:
        mid = (high + low) // 2
        if theList[mid] == target:
            return mid
        elif theList[mid] > target:
            high = mid - 1
        else:
            low = mid + 1
    
    return low
    
sequence = [2, 4, 5, 10, 13, 18, 23, 29, 31, 51, 64]
print(sequence)
target = 29
target_position = findOrderedPosition(sequence, target)
sequence.insert(target_position, target)
print(sequence)