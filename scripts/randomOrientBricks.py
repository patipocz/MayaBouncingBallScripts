'''
Script that allows to randomly turn bricks 
in a way that they face random directions 
which allows to see a different part of the texture.

*brick12 name was changed so it is not turned
'''
import maya.cmds as cmds
import random

bricks = cmds.ls( 'brick*', tr=True)

angles = [0, 90, 180, 270]
#orientation = random.choice(angles) 

for b in bricks:
    cmds.setAttr(b + '.rotateX', random.choice(angles))
    cmds.setAttr(b + '.rotateY', random.choice(angles))
    cmds.setAttr(b + '.rotateZ', random.choice(angles))
