'''
@Description: In User Settings Edit
@Author: your name
@Date: 2019-10-14 08:20:50
@LastEditTime: 2019-10-15 08:53:51
@LastEditors: Please set LastEditors
'''
def mergeSortedLists(listA, listB):
    # Create the new list and initialize the list markers.
    newList = list()
    a = 0
    b = 0
    
    # Merge the two lists together until one is empty.
    while a < len(listA) and b < len(listB):
        if listA[a] < listB[b]:
            newList.append(listA[a])
            a += 1
        else:
            newList.append(listB[b])
            b += 1
            
    
    # If listA contains more items, append them to newList.
    while a < len(listA):
        newList.append(listA[a])
        a += 1
    
    # If listB contains more items, append them to newList.
    while b < len(listB):
        newList.append(listB[b])
        b += 1
        
    return newList

if __name__ == '__main__':
    listA = [2, 8, 15, 23, 37]
    listB = [4, 6, 15, 20]
    
    newList = mergeSortedLists(listA, listB)
    print(newList)