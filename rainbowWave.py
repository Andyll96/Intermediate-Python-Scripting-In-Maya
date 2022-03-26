from audioop import reverse
from turtle import clear
from maya import cmds
import random

"""A script that generates a field of spheres that are offset by their position, size and color to create a wave
"""

def createField(length=1, width=1, height=1):
    deleteExisting()
    for l in range(length):
        for w in range(width):
            for h in range(height):
                sphereName = f'sphere_{l}_{w}_{h}'
                cmds.polySphere(name=f'{sphereName}_geo', r=0.3, sx=8, sy=8)
                cmds.polySoftEdge(angle=180, constructionHistory=0)

                # be careful that your naming objects the same thing, as Maya will automatically renumber it
                cmds.group(name=f'{sphereName}_grp')
                cmds.move(l, h, w)
                cmds.select(f'{sphereName}_geo')
                cmds.move(l + 0.5, h, w)

                # l+w+h is the offset which is different for every circle
                cmds.expression(s=f'{sphereName}_grp.rotateX = (time + {l + w + h}) * 30')
                cmds.expression(s=f'{sphereName}_grp.rotateY = (time + {l + w + h}) * 30')
                cmds.expression(s=f'{sphereName}_grp.rotateZ = (time + {l + w + h}) * 30')

def deleteExisting():
    cmds.select(clear=True)
    objects = cmds.ls(dag=True, long=True)
    print(f'objects:\n{objects}')
    # objects.sort(key=len, reverse=True)
    for obj in objects:
        if('_grp' in obj and '_geo' not in obj):
            cmds.select(obj)
            cmds.delete()
            print(f'Deleted: {obj}')

createField(10,10)