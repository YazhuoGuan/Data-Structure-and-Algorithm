'''
@Description: In User Settings Edit
@Author: your name
@Date: 2019-10-12 15:44:22
@LastEditTime: 2019-10-12 15:54:36
@LastEditors: Please set LastEditors
'''
class SparseMatrix:
    # Create a sparse matrix of size numRows * numCols initialized to 0.
    def __init__(self, numRows, numCols):
        self._numRows = numRows
        self._numCols = numCols
        self._elementList = list()
        
    # Return the number of rows in the matrix.
    def numRows(self):
        return self._numRows
    
    # Return the number of columns in the matrix.
    def numCols(self):
        return self._numCols
    
    # Return the value of element (i, j): x[i, j]
    # TO DO: exercise
    def __getitem__(self, ndxTuple):
        return
    
    # Set the value of element (i, j) to the value s: s[x, j] = s
    def __setitem__(self, ndxTuple, scalar):
        ndx = self._findPosition(ndxTuple[0], ndxTuple[1])
        if ndx is not None