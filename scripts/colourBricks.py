'''
This script is repurposed colourBalls.py script. 

It allows to randomly assign ABC bricks shaders to the bricks.

(I manually created the shaders earlier with connected textures
and renamed shading groups, 
I listed shading groups with a MEL command:
ls -type "shadingEngine"
and copied the resulting shaders to this script for randomisation)

'''

import maya.cmds as cmds
import random

# LIST ALL GEOMETRY OBJECTS TO SHADE
bricksToShade = cmds.ls( 'brick*', g=True)



# ASSIGN SHADERS TO THE OBJECTS
# If you want to just change the look, re-run assigning shaders without creating the shaders again run only the code below

# make a list of shader groups 
# the multipliers give you control over weights so what percentage of given colour you want (try keep the sum to around 100 for ease of use)
# myShaderGroups = ['blueMaterialGroup']*25 + ['pinkMaterialGroup'] *25 + ['greenMaterialGroup']*25 + ['purpleMaterialGroup']*25


# for random distribution withou weights run the one below instead

myShaderGroups = [
    'pasted__AFourTulipSunSG', 
    'pasted__ASharkStarHedgehogSG', 
    'pasted__BSharkBeeHedgehogSG', 
    'pasted__BTwoBeeDuckSG', 
    'pasted__CCastleAndBoatSG', 
    'pasted__CTreeFiveSunSG',
    'pasted__DCastleAndHedgehogSG', 
    'pasted__DRocketEightDuckSG', 
    'pasted__EThreeFiveSunSG', 
    'pasted__FRocketElephantOneSG', 
    'pasted__FStrawberryHouseBoatSG', 
    'pasted__GRocketStarDuckSG', 
    'pasted__GSharkSwanHedgehogSG', 
    'pasted__HSharkSwanHedgehogSG', 
    'pasted__HStrawberryHouseButterflySG'
]



#assign the shaders randomly
for b in bricksToShade:
    myChoice = random.choice(myShaderGroups)
    #myChoice = myShaderGroups[0]
    cmds.sets(b, e=True, forceElement = myChoice)

