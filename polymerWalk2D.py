#Drew Boyette
#Computational Physics
#5/27/15
#boyette_polymerWalk2D.py

from visual import *
from visual.graph import* 
import random
import math

##This program will create a 2D lattice square of a certain side length.
##This program simulates a polymer chain forming using a random self-avoiding walk,
##a random walk that cannot repeat its previous path. Once the program runs, the user will be asked the size of the grid. The user must input
##an integer greater than zero that will be the side length of the grid displayed. A grid of points will be displayed in a separate window.
##Once the window is clicked, the random walk will start. The path taken is shown by a curve that connects all the points. Once there are no
##adjacent sites that haven't visited, the program stops.

#Note: Recommended grid sizes: 3 <= N <= 150. The grid with 150**2 points will be difficult to load and is unnecessary.
################################################################
#Pseudocode

#Setup display

#Create grid
##Create an array of points
##Use a for loop to create a square with a certain side length
###for i in length of grid :
####for j in length of grid :
#####points.append(pos=(i,j))

#Create a curve that will visually connect the points

#Create a function that outputs a point's adjacent points that haven't been visited
##if the point is not on a certain side of the square
###Append the path that leads in the direction of that side (as long as the path doesn't lead to an already visited site)

#while (there are still possible paths to take) :
##Output the possible paths for a certain point
##Randomly pick one of these paths
##Append this path to the curve

#################################################

#Display setup
scene = display(width=800, height=800,title='2D Square Lattice - Random Walk')
scene.userzoom = False
scene.background=(1,1,1)
sizeGrid = int(input("Size?: ")) #This integer is a side length of the grid created 
while sizeGrid <= 1:
    print("Invalid input. Try again.")
    sizeGrid = int(input("Size?: "))
scene.range=round(1.41421*(sizeGrid/2),0)

#Grid Setup
pointsArray = points(size=100/sizeGrid, shape="round", color=(0,0,1)) #creates an array of points
usedList = [] #This list will contain every site that has been visited, ensuring that the curve never crosses itself
stuck = False #Boolean for when the polymer chain is no longer able to form chains without overlapping
L = label(text="N = 0", pos=(sizeGrid/2,sizeGrid/2),color=color.black,height=20, border=6, linecolor=color.black) #Creates a label with the current number of steps

for i in range(sizeGrid) : #Creates a square of points with a side length of sizeGrid
    for j in range(sizeGrid):
        pointsArray.append(pos=(i-sizeGrid/2,j-sizeGrid/2)) #This ensures that the origin is the center of the square

#This creates a curve which will consist of all the lattice sites visited throughout the run. The initial point is at the center of the square. 
c = curve(pos=(0,0),radius=.03, color=(1,0,0))

#Increases the radius of the curve as the length of the grid increases
if sizeGrid >= 40 and sizeGrid <= 150:
    c.radius= .001*sizeGrid
    
usedList.append([0,0]) 

#This function takes a position of a point as input, and outputs
#all the adjacent points that have not been visited. 
def adjacentPoints(coord) :
    result=[]
    if sizeGrid%2==0 : #If the side length is even, this code will run. The difference is the boundaries of the square. 
        b=sizeGrid/2
        if coord[0]!=b-1 and [coord[0]+1,coord[1]] not in usedList : #If the point is not on the far right side and the point directly right of this point hasn't
            result.append([coord[0]+1,coord[1]])                     #been visited, then this a possible path. 
        if coord[0]!=-b and [coord[0]-1,coord[1]] not in usedList:
            result.append([coord[0]-1,coord[1]])
        if coord[1]!=b-1 and [coord[0],coord[1]+1] not in usedList:
            result.append([coord[0],coord[1]+1])
        if coord[1]!=-b and [coord[0],coord[1]-1] not in usedList:
            result.append([coord[0],coord[1]-1])
    else : #If the side length is odd, this code will run. 
        b=(sizeGrid-1)/2
        if coord[0]!=b and [coord[0]+1,coord[1]] not in usedList :
            result.append([coord[0]+1,coord[1]])
        if coord[0]!=-b and [coord[0]-1,coord[1]] not in usedList:
            result.append([coord[0]-1,coord[1]])
        if coord[1]!=b and [coord[0],coord[1]+1] not in usedList:
            result.append([coord[0],coord[1]+1])
        if coord[1]!=-b and [coord[0],coord[1]-1] not in usedList:
            result.append([coord[0],coord[1]-1])
    return result


i=0
scene.waitfor('click') #Program doesn't start until the window is clicked

while stuck==False : #Runs until there are no adjacent points that haven't been visited. 
    rate(20) #Slows the program down
    adjacent=adjacentPoints(c.pos[i])
    num=len(adjacent)
    if num == 0:
        stuck=True
    else :
        path=random.randrange(0,num) #Chooses a random path out of the available paths to take
        c.append(adjacent[path]) #Appends the chosen path to the curve
        usedList.append(adjacent[path]) #Appends point to the used list
        i+=1
        L.text= "N = %d" % (i) #Updates the label every iteration
        
print("End of Walk")
print("Steps: %d" %(i))


