'''
@Description: In User Settings Edit
@Author: your name
@Date: 2019-10-14 08:20:50
@LastEditTime: 2019-10-14 11:10:31
@LastEditors: Please set LastEditors
'''
def insertionSort(theSeq):
    n = len(theSeq)
    # Starts with the first item as tha only sorted entry.
    for i in range(1, n):
        print('循环第 {} 次'.format(i))
        value = theSeq[i]
        print('第 {} 次值为： {}'.format(i, value))
        # Find the position where value fits in the ordered part of the list.
        pos = i
        print('位置为：{}'.format(pos))
        while pos > 0 and value < theSeq[pos - 1]:
            theSeq[pos] = theSeq[pos - 1]
            pos -= 1
            print('new pos : {}'.format(pos))
        
        # Put the saved value into the open slot.
        theSeq[pos] = value
        print('位置为：{}'.format(pos))
        print('第 {} 次序列为：{}'.format(i, theSeq))

    return theSeq

sequence = [10, 51, 2, 18, 4, 31, 13, 5, 23, 64, 29]
# sequence = [2, 4, 5, 10, 13, 18, 23, 29, 31, 51, 64]
result = insertionSort(sequence)
print(result)