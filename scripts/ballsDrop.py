"""
This Tool allows for a creation of a realistic pile of balls inside of a spherical shape. 
First it creates a number of balls then drops them into a spherical object using rigid bodies simulation. At the end it freezes the simulation and cleans it up from history and unnecessary geometry. 

It is a simulation and it is not perfect, so you might still have to realign from where the balls drop, number of them, or change some settings like active rigid body mass or gravity and rerun to check if this fits your needs. After everything some balls might still bounce outside of the sphere or not fully fall down so please delete anything you don't like. 


The tool is designed to help create full jars of candy, gumball machines etc. and to speed up the process of manually allocating the balls/candy and/or the simulation settings. It can be repurposed for different shapes different numbers and sizes or shapes of the filling objects. It could also be adjusted and used in an animated version. 


........


This tool first creates an army of balls in even rows, 
the number of rows or columns in X,Y and Z can be manipulated 
by changing the ranges in for loops.


I strongly recommend adding rows only in Y not X and Z 
as those two seem to need more adjusting in order to not to fall out of the bowl of the current size

(there is a possiblitity to make the newly created pile a passive rigid body and use for next simulation so it is faster)




*The disadvantage is the tool can be only used once unless you rename the ballsGroup and ball in the created army


* It is highly recommended to run this script in a separate maya file and then export it and import it into your scene once you are happy with the results as the whole proces might be a bit heavy on the geometry and simultion and it will also take some time


"""


import maya.cmds as cmds
from maya.cmds import *

# make an empty group to hold the balls
cmds.group( em=True, name='ballsGroup' )

# create the first ball and parent it to the group so it is inside

firstBorn = cmds.polySphere(name = 'ball', sx=8, sy=8, r=2.0)
cmds.parent ('ball', 'ballsGroup')

# duplicate the ball in Y however many you want, it will be the number of rows in Y
for n in range (0,7):
    cmds.duplicate()
    cmds.move(0,4,0, r=True)

# select the contents of the ballsGroup
babies = cmds.listRelatives('ballsGroup')
cmds.select(babies)

# duplicate the balls in X       
for b in range (0,2):
    cmds.duplicate()
    cmds.move(4,0,0, r=True)
    
moreBabies = cmds.listRelatives('ballsGroup')
cmds.select(moreBabies)  

# duplicate the balls in Z 
for b in range (0,2):
    cmds.duplicate()
    cmds.move(0,0,4, r=True)
    
    
# select the group of all the balls and freeze transforms
cmds.select('ballsGroup') 
cmds.makeIdentity( apply=True )


# select the balls themselves not as a group and move them up (moving in x and z exists only to center them)
allBalls = cmds.listRelatives('ballsGroup')
cmds.select(allBalls)
# y value indicates from what hight the balls are dropped
cmds.move(-4,6,-4)



#assign active Rigid body and gravity and connect the dynamics - you can manipulate active rigid body values here if needed
cmds.select(allBalls)
# m was originally 10, b was 0.6
cmds.rigidBody(active=True, m=45, dp=0, sf=0.2, df=0.2, b=0.1, l=0, tf=200, iv=(0, 0, 0), iav=(0, 0, 0), c=0, pc=0, i=(0, 0, 0), imp= (0, 0, 0), si=(0, 0, 0), sio='none')
cmds.select(allBalls)
cmds.gravity(pos = (0, 0, 0), m = 9.8, att=0, dx=0, dy=-1, dz=0,  mxd = -1,  vsh='none', vex=False, vof= (0, 0, 0), vsw=360, tsr=0.5)
cmds.connectDynamic(allBalls, f='gravityField1')

# create a bowl at origin point, reverse the faces to face inwards delete history and freeze transforms, radius was 10
cmds.polySphere(name = 'bowl',sx=16,sy=16, r=10)
facesToDelete = ['bowl.f[192:223]','bowl.f[240:255]', 'bowl.f[176:191]' ]
cmds.select(facesToDelete)
cmds.delete()
cmds.select('bowl')
cmds.polyNormal('bowl', normalMode=0,userNormalMode=0, ch=1)
cmds.delete('bowl', constructionHistory = True)
cmds.makeIdentity( apply=True )

# visibility off
cmds.setAttr('bowl.visibility', 0)

# make the bowl a passive rigid body
cmds.rigidBody('bowl', passive=True)

# optional inside orb to save on geo that is not going to be visible ans speed up the sim

# create orb with smaller radius than the bowl and less divisions, delete history, freeze transforms
cmds.polySphere(name = 'orb',sx=8,sy=8, r=1)
cmds.move(0,-1, 0)
cmds.delete('orb', constructionHistory = True)
cmds.makeIdentity( apply=True )
# visibility off
cmds.setAttr('orb.visibility', 0)

# make the orb a passive rigid body
cmds.rigidBody('orb', passive=True)



# simulate, make the balls drop and get the frame when they fell here 150 
# (I think it might also be slider range dependadnt)
cmds.currentTime(1, edit=True)
cmds.play(forward=True, wait=True)
cmds.currentTime( 150, edit=True )



# IF MAYA ACTS WEIRD RUN THE PART BELOW SEPARATELY TO THE PART ABOVE
# cleanup phase

cmds.select('ballsGroup','bowl', 'orb')
# delete all rigid bodies
# select shapes with name rigidBody* and delete them
rigidBodiesShapes = cmds.listRelatives('ballsGroup','bowl','orb', ad=True)
cmds.select(rigidBodiesShapes)
bodiesToDelete = cmds.ls( 'rigidBody*', sl=True, shapes=True )
cmds.delete(bodiesToDelete)

# select bowl, orb and balls and delete historyand freeze transformations
cmds.select('ballsGroup','bowl', 'orb')
cmds.delete('ballsGroup', 'bowl', 'orb', constructionHistory = True)
cmds.makeIdentity( apply=True )

# if gravity field still exists delete it ???
cmds.delete('gravityField1')

#delete bowl and orb
cmds.delete('bowl', 'orb')

# center pivot on the balls group
cmds.select('ballsGroup')
cmds.xform(cp=True)


#here you have your pile of baby balls, enjoy, you can move it anywhere now
