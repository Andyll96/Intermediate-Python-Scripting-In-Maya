from maya import cmds
import ntpath

newDirectory = cmds.fileDialog2(fileMode=3)
newDirectory = newDirectory[0]


textures = cmds.ls(tex=True)
# print(textures)
# print(cmds.listAttr(textures[0]))

for tex in textures:
    filePath = cmds.getAttr(f'{tex}.fileTextureName')
    fileName = ntpath.basename(filePath)
    # print(fileName)
    newPath = f'{newDirectory}/{fileName}'
    cmds.setAttr(f'{tex}.fileTextureName', newPath, type='string')