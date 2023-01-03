"""

This tool lets you create an army of balls in even rows, 
the number of rows or columns in X,Y and Z can be manipulated 
by changing the ranges in for loops.

*The disadvantage is the tool can be only used once unless you rename the ballsGroup and ball in the created army

"""

import maya.cmds as cmds

# make an empty group to hold the balls
cmds.group( em=True, name='ballsGroup' )

# create the first ball and parent it to the group so it is inside

firstBorn = cmds.polySphere(name = 'ball', sx=8, sy=8, r=1)
cmds.parent ('ball', 'ballsGroup')

# duplicate the ball in Y however many you want, it will be the number of rows in Y
for n in range (0,10):
    cmds.duplicate()
    cmds.move(0,2,0, r=True)

# select the contents of the ballsGroup
babies = cmds.listRelatives('ballsGroup')
cmds.select(babies)

# duplicate the balls in X       
for b in range (0,2):
    cmds.duplicate()
    cmds.move(2,0,0, r=True)
    
moreBabies = cmds.listRelatives('ballsGroup')
cmds.select(moreBabies)  

# duplicate the balls in Z 
for b in range (0,2):
    cmds.duplicate()
    cmds.move(0,0,2, r=True)
    
# select the group of all the balls and freeze transforms
cmds.select('ballsGroup') 
cmds.makeIdentity( apply=True )
    
