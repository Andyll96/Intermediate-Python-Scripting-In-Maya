from dataclasses import replace
from turtle import distance
from maya import cmds

def getAvg(vertList):
    avgX = 0
    avgY = 0
    avgZ = 0

    for vert in vertList:
        pos = cmds.pointPosition(vert)
        avgX += pos[0]
        avgY += pos[1]
        avgZ += pos[2]
    avgX = avgX / len(vertList)
    avgY = avgY / len(vertList)
    avgZ = avgZ / len(vertList)
    # print(f'AVG: [{avgX},{avgY},{avgZ}]')
    return [avgX, avgY, avgZ]

def moveAvg(axis, vertList):
    avg = getAvg(vertList)
    
    if(axis == 'x'):
        newPos = avg[0]

        for vert in vertList:
            currentPos = cmds.pointPosition(vert)
            distance = newPos - currentPos[0]
            
            cmds.select(vert, replace=True)
            cmds.move(distance, 0, 0, relative=True)
    elif(axis == 'y'):
        newPos = avg[1]

        for vert in vertList:
            print(vert)
            currentPos = cmds.pointPosition(vert)
            distance = newPos - currentPos[1]
            
            cmds.select(vert, replace=True)
            cmds.move(0, distance, 0, relative=True)
    elif(axis == 'z'):
        newPos = avg[2]

        for vert in vertList:
            currentPos = cmds.pointPosition(vert)
            distance = newPos - currentPos[2]
            
            cmds.select(vert, replace=True)
            cmds.move(0, 0, distance, relative=True)
        

# retruns names of objects in scene, ls = selection, Flattens the returned list of objects so that each component is identified individually.
verts = cmds.ls(sl=True, flatten=True)
moveAvg('y', verts)
