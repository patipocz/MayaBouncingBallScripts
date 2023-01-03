'''
Tool that helps assign shaders to a group of objects from the same name family, here geometry objects named ball*

It creates (here Arnold surface) shaders and then iterates through a list and assigns a random shader from the given shaders to the objects. 
'''

import maya.cmds as cmds
import random

# LIST ALL GEOMETRY OBJECTS TO SHADE
ballsToShade = cmds.ls( 'ball*', g=True)

#print(ballsToShade)


#################################################
# CREATE SHADERS AND MATERIAL/SHADER GROUPS

# pink
cmds.sets( name='pinkMaterialGroup', renderable=True, empty=True )
cmds.shadingNode('aiStandardSurface', name='pinkShader', asShader=True)
cmds.setAttr('pinkShader.baseColor', 1, 0.4, 0.7, type='double3')
cmds.setAttr('pinkShader.diffuseRoughness', 1)
cmds.setAttr('pinkShader.specularRoughness', 0.6)
cmds.surfaceShaderList('pinkShader', add='pinkMaterialGroup')
#cmds.sets(ballsToShade, e=True, forceElement = 'pinkMaterialGroup')

# blue
cmds.sets( name='blueMaterialGroup', renderable=True, empty=True )
cmds.shadingNode('aiStandardSurface', name='blueShader', asShader=True)
cmds.setAttr('blueShader.baseColor', 0, 0, 0.3, type='double3')
cmds.setAttr('blueShader.coat', 0.4)
cmds.setAttr('blueShader.coatColor', 0.2, 1, 0.5, type='double3')
cmds.setAttr('blueShader.sheen', 0)
cmds.setAttr('blueShader.sheenColor', 0, 0.3, 0.5, type='double3')
cmds.surfaceShaderList('blueShader', add='blueMaterialGroup')
#cmds.sets(ballsToShade, e=True, forceElement = 'blueMaterialGroup')

#green rubber
cmds.sets( name='greenMaterialGroup', renderable=True, empty=True )
cmds.shadingNode('aiStandardSurface', name='greenShader', asShader=True)
cmds.setAttr('greenShader.base', 1)
cmds.setAttr('greenShader.baseColor', 0.8, 1, 0.1, type='double3')
cmds.setAttr('greenShader.diffuseRoughness', 1)
cmds.setAttr('greenShader.specularRoughness', 0.6)
#cmds.setAttr('greenShader.coat', 0.3)
#cmds.setAttr('greenShader.coatColor', 1, 0.3, 0, type='double3')
#cmds.setAttr('greenShader.sheen', 0.8) 
#cmds.setAttr('greenShader.sheenColor', 0, 1, 1, type='double3')
cmds.surfaceShaderList('greenShader', add='greenMaterialGroup')
#cmds.sets(ballsToShade, e=True, forceElement = 'greenMaterialGroup')

#purple velvet
cmds.sets( name='purpleMaterialGroup', renderable=True, empty=True )
cmds.shadingNode('aiStandardSurface', name='purpleShader', asShader=True)
cmds.setAttr('purpleShader.base', 0.8)
cmds.setAttr('purpleShader.baseColor', 0.2, 0, 0.5, type='double3')
cmds.setAttr('purpleShader.specular',0)
cmds.setAttr('purpleShader.specularColor', 0, 0, 0, type='double3')
cmds.setAttr('purpleShader.specularIOR',0)
cmds.setAttr('purpleShader.specularAnisotropy',0.188)
#cmds.setAttr('purpleShader.coat', 0.5)
#cmds.setAttr('purpleShader.coatColor', 1, 0, 0.5, type='double3')
cmds.setAttr('purpleShader.sheen', 1)
cmds.setAttr('purpleShader.sheenColor', 1, 0, 0.5, type='double3')
cmds.setAttr('purpleShader.sheenRoughness', 0.3)
cmds.surfaceShaderList('purpleShader', add='purpleMaterialGroup')
#cmds.sets(ballsToShade, e=True, forceElement = 'purpleMaterialGroup')

#######################################################################
# ASSIGN SHADERS TO THE OBJECTS
# If you want to just change the look, re-run assigning shaders without creating the shaders again run only the code below


# make a list of shader groups 
# the multipliers give you control over weights so what percentage of given colour you want (try keep the sum to around 100 for ease of use)
myShaderGroups = ['blueMaterialGroup']*25 + ['pinkMaterialGroup'] *25 + ['greenMaterialGroup']*25 + ['purpleMaterialGroup']*25

# for random distribution withou weights run the one below instead
#myShaderGroups = ['blueMaterialGroup', 'pinkMaterialGroup', 'greenMaterialGroup']


#assign the shaders randomly
for b in ballsToShade:
    myChoice = random.choice(myShaderGroups)
    #myChoice = myShaderGroups[0]
    cmds.sets(b, e=True, forceElement = myChoice)


