'''
@Description: In User Settings Edit
@Author: your name
@Date: 2019-10-09 13:16:12
@LastEditTime: 2019-10-09 14:47:14
@LastEditors: Please set LastEditors
'''
class Map:
    # Creates an empty map instance
    def __init__(self):
        super().__init__()
        self._entryList = list()
        
    # Returns the number of entries in the map
    def __len__(self):
        return len(self._entryList)
    
    # Determines if the map contains the given key
    def __contains__(self, key):
        ndx = self._findPosition(key)
        return ndx is not None
    
    # Adds a new entry to the map if the key does exist. Otherwise, the new value replaces the current value associated with the key.
    def add(self, key, value):
        ndx = self._findPosition(key)
        if ndx is not None:
            self._entryList[ndx].value = value
            return False
        else:
            entry = _MapEntry(key, value)
            self._entryList.append(entry)
            return True
        
    # Returns the value associated with the key
    def valueOf(self, key):
        ndx = self._findPosition(key)
        assert ndx is not None, "Invalid map key"
        return self._entryList[ndx].value
    
    # Removes the entry associated with the key
    def remove(self, key):
        ndx = self._findPosition(key)
        assert ndx is not None, "Invalid map key."
        self._entryList.pop(ndx)
        
    # Returns an iterator for traversing the keys in the map
    def __iter__(self):
        return _MapIterator(self._entryList)
        
    def _findPosition(self, key):  
        for i in range(len(self)):
            if self._entryList[i].key == key:
                return i
            return None
            
class _MapEntry:
    def __init__(self, key, value):
        self.key = key
        self.value = value
            
class _MapIterator:
    def __init__(self, theList):
        self._mapItems = theList
        self._curItem = 0 
        
    def __iter__(self):
        return self
    
    def __next__(self):
        if self._curItem < len(self._mapItems):
            item = self._mapItems[self._curItem]
            self._curItem += 1
            return item
        else:
            raise StopIteration