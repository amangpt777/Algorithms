'''
Created on Nov 24, 2016

@author: amangupta
'''

class Grid(object):
    '''
    classdocs
    '''
    _numRows_ = 0
    _numColumns_ = 0
    offLimits = []

    def __init__(self, params):
        '''
        Constructor
        '''
        global offLimits
        global _numRows_
        global _numColumns_ 
        offLimits = []
        _numRows_ = params[0]
        _numColumns_ = params[1]
        offL = params[2]
        for line in offL:
            offLimits.append(list(map(int, line.split(','))))
            
    def getRows(self):
        global _numRows_
        return _numRows_
    
    def getColumns(self):
        global _numColumns_
        return _numColumns_
    
    def getCandidates(self, currenti, currentj):
        
        neighbours = []
        if currenti + 1 < _numRows_ and ([currenti + 1, currentj] not in offLimits):
            neighbours.append([currenti + 1, currentj])
        if currenti - 1 >= 0 and ([currenti - 1, currentj] not in offLimits):
            neighbours.append([currenti - 1, currentj])
            
        if currentj + 1 < _numColumns_ and ([currenti, currentj + 1] not in offLimits):
            neighbours.append([currenti, currentj + 1])
            
        if currentj - 1 >= 0 and ([currenti, currentj - 1] not in offLimits):
            neighbours.append([currenti, currentj - 1])
            
        return neighbours
            
            
            