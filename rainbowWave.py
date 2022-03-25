from maya import cmds
import random

"""A script that generates a field of spheres that are offset by their position, size and color to create a wave
"""

def createField(length=1, width=1, height=1):
    for l in range(length):
        for w in range(width):
            for h in range(height):
                sphereName = f'sphere_{l}_{w}_{h}'
                # deleteExisting(sphereName)
                cmds.polySphere(name=sphereName, r=0.3, sx=8, sy=8)
                cmds.polySoftEdge(angle=180, constructionHistory=0)

                # be careful that your naming objects the same thing, as Maya will automatically renumber it
                cmds.group(name=f'{sphereName}_grp')
                cmds.move(l, h, w)
                cmds.select(sphereName)
                cmds.move(l + 0.5, h, w)

                cmds.expression(s=f'{sphereName}_grp.rotateX = (time + {l + w + h}) * 30')
                cmds.expression(s=f'{sphereName}_grp.rotateY = (time + {l + w + h}) * 30')
                cmds.expression(s=f'{sphereName}_grp.rotateZ = (time + {l + w + h}) * 30')

# TODO: FIX DELETE EXISTING 
def deleteExisting(sphereName):
    if(cmds.objExists(f'{sphereName}_grp')):
        cmds.select(f'{sphereName}_grp', r=True)
        cmds.delete()

createField(10,10)