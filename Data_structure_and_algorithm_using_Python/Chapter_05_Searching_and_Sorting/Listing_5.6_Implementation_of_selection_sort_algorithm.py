'''
@Description: In User Settings Edit
@Author: your name
@Date: 2019-10-14 08:20:50
@LastEditTime: 2019-10-14 10:50:48
@LastEditors: Please set LastEditors
'''
def selectionSort(theSeq):
    n = len(theSeq)
    
    for i in range(n - 1):
        smallNdx = i
        for j in range(i+1, n):
            if theSeq[j] < theSeq[smallNdx]:
                smallNdx = j
        
        # Swap the ith value and smallNdx value only if the smallest value is not already in its proper position.
        # Some implementations omit testing the condition and always swap the two values.
        if smallNdx != i:
            theSeq[i], theSeq[smallNdx] = theSeq[smallNdx], theSeq[i]

    return theSeq

sequence = [10, 51, 2, 18, 4, 31, 13, 5, 23, 64, 29]
# sequence = [2, 4, 5, 10, 13, 18, 23, 29, 31, 51, 64]
result = selectionSort(sequence)
print(result)