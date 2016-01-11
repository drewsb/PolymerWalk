#Drew Boyette
#Computational Physics
#5/27/15
#polymerWalk3D.py

from visual import *
from visual.controls import *
from visual.graph import* 
import random
import math

#This program is essentially the same as the 2D polymerWalk, with a few additions.
#The program will produce a window diplaying a 3D cube of points, and once clicked, the random walk will start.
#A control window will also appear, with the option to turn the points on or off. Turning the points off
#will make the grid of points disappear, but the curve will still be visible. It is not recommended
#to turn the points on or off while the program is running, as this would cause massive lag and possibly
#crash the program.

#############################################
#Pseudocode is the same for the 2D program, except for extending the dimension to 3D. 


#Note: Recommended grid sizes: 3 <= N <= 150. After a 1000 walk steps, the curve will start to glitch.
#This is because the maximum amount of points a curve can display is a 1000 points. 

#############################################
#Scene setup
scene = display(width=800, height=800,title='3D Cube Lattice - Random Walk')
scene.background=(1,1,1)
sizeGrid = int(input("Size?: "))
while sizeGrid <= 1:
    print("Invalid input. Try again.")
    sizeGrid = int(input("Size?: "))
scene.range=round(1.41421**2*(sizeGrid/2),0)

pointsArray = points(size=100/sizeGrid, shape="round", color=(0,0,1))
usedList = [] #This list contains all lattice sites (points) that the curve has passed through
stuck = False #A boolean for when the polymer has finished forming (no more surrounding lattice sites that haven't been visited)

for i in range(sizeGrid) :
    for j in range(sizeGrid):
        for h in range(sizeGrid) :
            pointsArray.append(pos=(i-sizeGrid/2,j-sizeGrid/2, h-sizeGrid/2)) #Sets up 3D cube of points. Ensures the origin is the center of the cube. 
            

c = curve(pos=(0,0,0),radius=.04, color=(1,0,0)) #Create a curve of points
 
def change(): # Called by controls when button clicked
    if b.text == 'Points: ON':
        b.text = 'Points: OFF'
        pointsArray.visible=False #This makes the lattice sites invisible 
    else:
        b.text = 'Points: ON'
        pointsArray.visible=True #Makes the lattice sites visible again

scene.select()        
b = button( pos=(-sizeGrid/2,sizeGrid/2), width=60, height=60, text='Points: ON', action=lambda: change()) #The URL below is the website that gives code for buttons in vpython
#http://www.vpython.org/contents/docs_vp5/visual/controls.html

#This text box contains the total number of steps and is updated continuously throughout the run
L = label(text="N = 0", pos=(sizeGrid/2,sizeGrid/2),color=color.black,height=20, border=6, linecolor=color.black) 

usedList.append([0,0,0]) #Appends the first point to the used list
    
def adjacentPoints(coord) :
    result=[]
    if sizeGrid%2==0:
        b=sizeGrid/2
        if coord[0]!=b-1 and [coord[0]+1,coord[1], coord[2]] not in usedList : 
            result.append([coord[0]+1,coord[1], coord[2]])
        if coord[0]!=-b and [coord[0]-1,coord[1], coord[2]] not in usedList:
            result.append([coord[0]-1,coord[1], coord[2]])
        if coord[1]!=b-1 and [coord[0],coord[1]+1, coord[2]] not in usedList:
            result.append([coord[0],coord[1]+1, coord[2]])
        if coord[1]!=-b and [coord[0],coord[1]-1, coord[2]] not in usedList:
            result.append([coord[0],coord[1]-1, coord[2]])
        if coord[2]!=b-1 and [coord[0],coord[1], coord[2]+1] not in usedList: #Includes the third dimension
            result.append([coord[0],coord[1], coord[2]+1])
        if coord[2]!=-b and [coord[0],coord[1], coord[2]-1] not in usedList:
            result.append([coord[0],coord[1], coord[2]-1])
    else :
        b=(sizeGrid-1)/2
        if coord[0]!=b and [coord[0]+1,coord[1], coord[2]] not in usedList :
            result.append([coord[0]+1,coord[1], coord[2]])
        if coord[0]!=-b and [coord[0]-1,coord[1], coord[2]] not in usedList:
            result.append([coord[0]-1,coord[1], coord[2]])
        if coord[1]!=b and [coord[0],coord[1]+1, coord[2]] not in usedList:
            result.append([coord[0],coord[1]+1, coord[2]])
        if coord[1]!=-b and [coord[0],coord[1]-1, coord[2]] not in usedList:
            result.append([coord[0],coord[1]-1, coord[2]])
        if coord[2]!=b and [coord[0],coord[1], coord[2]+1] not in usedList:
            result.append([coord[0],coord[1], coord[2]+1])
        if coord[2]!=-b and [coord[0],coord[1], coord[2]-1] not in usedList:
            result.append([coord[0],coord[1], coord[2]-1])
    return result

i=0
scene.waitfor('click')

colorList=[(0,1,0),(0,1,1), (1,1,0),(1,0,1),(.4,1,.4),(1,.4,.4), (.4,.4,1),(1,0,0)] #A list a colors that will be used to change the color of the curve. 
#Colors: Green, Cyan, Yellow, Magenta, Light Green, Light Blue, Light Red, Red

colorVary = True #Colors will vary if this is True. The curve will remain red if False. 

while stuck==False :
    rate(20)
    adjacent=adjacentPoints(c.pos[i])
    num=len(adjacent)
    if num == 0:
        stuck=True
    else :
        
        path=random.randrange(0,num)
        i+=1
        if colorVary == True and i%100==0 : #Switches the color of the curve every 100 steps.
            c.append(pos=adjacent[path],color=colorList[(i%800)/100-1])
        else :
            c.append(pos=adjacent[path])
        usedList.append(adjacent[path])
        L.text= "N = %d" % (i)
print("End of Walk")
print("Steps: %d" %(i))

