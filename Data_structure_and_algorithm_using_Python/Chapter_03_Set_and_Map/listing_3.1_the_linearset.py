'''
@Description: In User Settings Edit
@Author: your name
@Date: 2019-10-09 08:46:21
@LastEditTime: 2019-10-09 11:26:49
@LastEditors: Please set LastEditors
'''

class Set:
    def __init__(self):
        super().__init__()
        self._theElements = list()
        
    def __len__(self):
        return len(self.theElements)
    
    def __contains(self):
        return element in self._theElements
    
    # Adds a new unique element to the set.
    def add(self, element):
        if element not in self:  # first ensure the supplied element is not in the list.
            self._theElements.append(element)
    
    def remove(self, element):
        assert element in self, "The element must be in the set."
        self._theElements.remove(item)
    
    # Determines if two sets are equal.    
    def __eq__(self, setB):
        if len(self) != len(setB):
            return False
        else:
            return self.isSubsetOf(setB)
        
    def isSubsetOf(self, setB):
        for element in self:
            if element not in setB:
                return False
        return True
    
    def union(self, setB):
        newSet = Set()
        newSet._theElements.extend(self._theElements)
        for element in setB:
            if element not in self:
                newSet._theElements.append(element)
        return newSet
    
    def interset(self, setB):
        newSet = Set()
        for element in setB:
            if element in self:
                newSet.add(element)
        if newSet:
            return newSet
        else:
            return "There's no intersection."
        
    def difference(self, setB):
        newSet = Set()
        for element in setB:
            if element not in self:
                newSet.add(element)
        if newSet:
            return newSet
        else:
            return "There's no difference."
        
    def __iter__(self):
        return _SetIterator(self._theElements)
    
    
smith = Set()
smith.add("CSCI-112")
smith.add("MATH-121")
smith.add("HIST-340")
smith.add("ECON-101")

roberts = Set()
roberts.add("POL-101")
roberts.add("ANTH-230")
roberts.add("CSCI-112")
roberts.add("ECON-101")

if smith == roberts:
    print('Smith and Roberts are taking same courses.')

else:
    sameCourse = smith.intersection(roberts)
    if sameCourse.isEmpty():
        print('Smith and Roberts are not taking any of the same courses.')
    
    else:
        print("Smith and Roberts are taking some of the same courses:")
        for courses in sameCourse:
            print(courses)