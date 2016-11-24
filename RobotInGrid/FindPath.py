'''
Created on Nov 24, 2016

@author: amangupta
'''
import sys
import RobotInGrid.Grid as g

offLimits = []
myPath = []

def move(currenti, currentj , desti, destj, myGrid, myPath):
    
    for candidate in myGrid.getCandidates(currenti, currentj):
        if [candidate[0],candidate[1]] in myPath:
            continue
        
        myPath.append([candidate[0], candidate[1]])
        if desti == candidate[0] and destj == candidate[1] :
            return myPath
        
        myPath = move(candidate[0], candidate[1], desti, destj, myGrid, myPath)
        if myPath[-1][0] == desti and myPath[-1][1] == destj:
            return myPath
        
        
    myPath = myPath[0:-1]
    return myPath

if __name__ == '__main__':
    sys.setrecursionlimit(1500)
    if len(sys.argv) < 2:
        print("Usage : FindPath.py inputfile.txt")
    numOfRows = int(raw_input("Enter the number of rows"))
    numOfColumns = int(raw_input("Enter the number of columns"))
    with open(sys.argv[1], "r") as offLimitsFile:
        for line in offLimitsFile:
            offLimits.append(line)
            
    myGrid = g.Grid([numOfRows, numOfColumns, offLimits])
    myPath = []
    myPath.append([0, 0])
    myPath = move(0, 0, numOfRows - 1, numOfColumns - 1, myGrid , myPath)
    print("The path that can be followed is:", myPath)