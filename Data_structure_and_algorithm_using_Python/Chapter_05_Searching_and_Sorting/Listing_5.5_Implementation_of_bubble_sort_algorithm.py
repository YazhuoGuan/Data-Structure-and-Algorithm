'''
@Description: In User Settings Edit
@Author: your name
@Date: 2019-10-14 08:20:50
@LastEditTime: 2019-10-14 09:50:15
@LastEditors: Please set LastEditors
'''
def bubbleSort(theSeq):
    n = len(theSeq)
    # Perform n-1 bubble operations on the sequence:
    for i in range(n - 1):
        print('循环次数：{}'.format(i+1))
        swap_flag = False
        # Bubble the largest item to the end.
        for j in range(n - i - 1):
            if theSeq[j] > theSeq[j+1]:
                theSeq[j], theSeq[j+1] = theSeq[j+1], theSeq[j]
                swap_flag = True
        if swap_flag == False:
            print('all sorted')
            return theSeq
    return theSeq

# sequence = [10, 51, 2, 18, 4, 31, 13, 5, 23, 64, 29]
sequence = [2, 4, 5, 10, 13, 18, 23, 29, 31, 51, 64]
result = bubbleSort(sequence)
print(result)