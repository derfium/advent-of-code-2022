import numpy as np

def task_1():
    
    with open("resources/inputFiles/input8.txt") as f:
        lines = f.read().splitlines()
        treeLines = [list(map(int, line)) for line in lines]
        print(type(treeLines[0][1]))
        
        treeCount = 0
        
        fromLeft = isTreeVisibleFromOutside(treeLines)
                
        
        return fromLeft

    
    return None

def isTreeVisibleFromOutside(trees):
    treeCounter = 0
    visibility = [[False for i in trees[0]] for j in trees]
    
    for i in range(len(trees)):
        lineHeight = -1
        for j in range(len(trees[0])):
            currentHeight = int(trees[i][j])
            if currentHeight > lineHeight:
                visibility[i][j] = True
                lineHeight = currentHeight
     
    for i in range(len(trees[0])):
        lineHeight = -1
        for j in range(len(trees)):
            currentHeight = int(trees[j][i])
            if currentHeight > lineHeight:
                visibility[j][i] = True
                lineHeight = currentHeight 
                
    for i in reversed(range(len(trees))):
        lineHeight = -1
        for j in reversed(range(len(trees[0]))):
            currentHeight = int(trees[i][j])
            if currentHeight > lineHeight:
                visibility[i][j] = True
                lineHeight = currentHeight
                
    for i in reversed(range(len(trees[0]))):
        lineHeight = -1
        for j in reversed(range(len(trees))):
            currentHeight = int(trees[j][i])
            if currentHeight > lineHeight:
                visibility[j][i] = True
                lineHeight = currentHeight     
    

    for line in visibility:
        for j in line:
            if j:
                treeCounter += 1
                
    return treeCounter

def calculateVisibility(iTree, jTree, trees):
    treeHeight = int(trees[iTree][jTree])
    overallTrees = 0
    #visibility = [[0 for i in trees[0]] for j in trees]
    visibileTrees = 0
    for i in reversed(range(0, iTree)):
        currentHeight = int(trees[i][jTree])
        visibileTrees += 1
        #visibility[i][jTree] = 1
        if currentHeight >= treeHeight:
            break
            
    overallTrees = visibileTrees
    visibileTrees = 0

    for i in range(iTree + 1, len(trees[0])):
        currentHeight = int(trees[i][jTree])
        print(currentHeight)
        visibileTrees += 1
        #visibility[i][jTree] = 2
        if currentHeight >= treeHeight:
            break
            
    overallTrees *= visibileTrees
    visibileTrees = 0
            
    for j in reversed(range(0, jTree)):
        currentHeight = int(trees[iTree][j])
        visibileTrees += 1
        #visibility[iTree][j] = 3
        if currentHeight >= treeHeight:
            break
            
    overallTrees *= visibileTrees
    visibileTrees = 0

    for j in range(jTree + 1, len(trees)):
        currentHeight = int(trees[iTree][j])
        visibileTrees += 1
        #visibility[iTree][j] = 4
        if currentHeight >= treeHeight:
            break
            
    overallTrees *= visibileTrees
    
    #visibility[iTree][jTree] = 9


    return overallTrees
    
            
def countVisibleTrees(visibilityChart):
    visibleCounter = 0
    for row in visibilityChart:
        for column in row:
            if column:
                visibleCounter += 1
                
    return visibleCounter
            
            



def task_2():
    with open("resources/inputFiles/input8.txt") as f:
        lines = f.read().splitlines()
        
        maxTrees = 0
        for i in range(len(lines)):
            for j in range(len(lines[0])):
                currentTrees = calculateVisibility(i, j, lines)
                #print(currentTrees)
                if currentTrees > maxTrees:
                    maxTrees = currentTrees
                    
        return maxTrees
        
#print("Task 1:", task_1())
print("Task 2:", task_2())