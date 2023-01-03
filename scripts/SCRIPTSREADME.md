

To run the scripts please copy paste their contents into the maya script editor Python tab and press run or press ctrl + A and small enter. Alternatively in the script editor open the script you want from this scripts folder location then run it.



You can find more instructions, explanations and more about the tools is in the description and comments in each script, but here is a brief overview:

BALLS PILE GENERATION AND SHADING SCRIPTS
.........................................

ballsArmy.py
- This script lets you duplicate a lot of balls into even rows, however many you want, in all directions.


ballsDrop.py
- This script creates a bowl shaped pile of balls, which can be used as a gumball machine or candy jar filling.


colourBalls.py
- This script let's you create a few Arnold shaders and assign them randomly to all objects in the scene starting with a certain name. You can also manipulate the weights of how big percentage of objects should be assigned each shader. 



BRICKS STAIRCASE SCRIPTS
.........................................

colourBricks.py
- This script let's you randomly assign earlier created shaders (with textures) to the cubes used to create the staircase. It could be also used for other objects, it is just another version of the colourBalls.py script.

randomOrientBricks.py
- This script let's you rotate the cubes in a way that they face different direction showing another side and therefore a different texture.  


................................................................................................
................................................................................................

* I recommend running the balls scripts in a separate clean new maya scene first and then importing to a project scene as the simulation and amount of geometry can get heavy and if you input a lot of balls to simulate it it will take a long time and sometimes Maya can crash as she likes to be a moody software. 


* Bricks scripts so colourBricks.py and randomOrientBricks.py can be tested using stairsinpieces.ma scene shaders that are included there and the textures that are located in sourceimages folder
