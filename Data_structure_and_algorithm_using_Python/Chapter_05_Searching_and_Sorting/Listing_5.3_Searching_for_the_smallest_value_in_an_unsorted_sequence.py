'''
@Description: In User Settings Edit
@Author: your name
@Date: 2019-10-14 08:20:50
@LastEditTime: 2019-10-14 08:32:23
@LastEditors: Please set LastEditors
'''
def findSmallest(theValues):
    n = len(theValues)
    smallest = theValues[0]
    for i in range(1, n):
        if theValues[i] < smallest:
            smallest = theValues[i]
    return smallest


sequence = [2, 4, 5, 10, 13, 18, 1, 23, 29, 31, 51, 64]

result = findSmallest(sequence)
print(result)