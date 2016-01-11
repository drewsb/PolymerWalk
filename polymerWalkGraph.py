#Drew Boyette
#Computational Physics
#5/27/15
#polymerWalkGraph.py

from random import randrange
from pylab import *

###NOTE: THIS MUST BE RUN IN CANOPY

#This program will generate graphs for a random walk simulation in either 2D or 3D
#or both. The user has the option to either generate a histogram of a single 
#grid size for a certain sample size, or a scatter plot of of many grid sizes for a certain sample
#size. 

dimension = raw_input("2D or 3D or both?: ") #User can choose either 2D, 3D, or both.
while dimension != "2D" and dimension !="3D" and dimension != "both" :
    print 'Invalid Input. Try Again.'
    if dimension == '' :
        break
    dimension = raw_input("2D or 3D or both?: ")

plotting = int(input("Plot a specific grid size,or a range of grid sizes? (0 or 1): ")) #User can choose to either graph one grid size, or multiple
while plotting!= 0 and 1 :
    print 'Invalid Input. Try Again.'
    plotting = int(input("Plot a specific grid size,or a range of grid sizes? (0 or 1): "))

n = int(input("Sample Size?: "))
while n<=1:
    print 'Invalid Input. Try Again.'
    n = int(input("Sample Size?: "))
if plotting == 0:
    size = int(input("Grid size?: "))
    while size<=1:
        print 'Invalid Input. Try Again.'
        size = int(input("Grid size?: "))

#This function is essentially the polymer walk program in 2D without the visual aspect. 
def polymerWalk2D(sizeGrid) : 
    pointsArray = []
    usedList = []
    stuck = False
    for i in range(sizeGrid) :
        for j in range(sizeGrid):
            pointsArray.append([i-sizeGrid/2,j-sizeGrid/2])
            
    usedList.append([0,0])

    def adjacentPoints(coord) :
        result=[]
        if sizeGrid%2==0 :
            b=sizeGrid/2
            if coord[0]!=b-1 and [coord[0]+1,coord[1]] not in usedList :
                result.append([coord[0]+1,coord[1]])
            if coord[0]!=-b and [coord[0]-1,coord[1]] not in usedList:
                result.append([coord[0]-1,coord[1]])
            if coord[1]!=b-1 and [coord[0],coord[1]+1] not in usedList:
                result.append([coord[0],coord[1]+1])
            if coord[1]!=-b and [coord[0],coord[1]-1] not in usedList:
                result.append([coord[0],coord[1]-1])
        else :
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
    while stuck==False :
        adjacent=adjacentPoints(usedList[i])
        num=len(adjacent)
        if num == 0:
            stuck=True
        else :
            path=int(randrange(0,num))
            usedList.append(adjacent[path])
            i+=1
    return i

#This function is essentially the polymer walk program in 3D without the visual aspect. 
def polymerWalk3D(sizeGrid) :
    pointsArray = []
    usedList = []
    stuck = False
    for i in range(sizeGrid) :
        for j in range(sizeGrid) :
            for h in range(sizeGrid) :
                pointsArray.append([i-sizeGrid/2,j-sizeGrid/2, h-sizeGrid/2])
            
    usedList.append([0,0,0])

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
            if coord[2]!=b-1 and [coord[0],coord[1], coord[2]+1] not in usedList:
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
    while stuck==False :
        adjacent=adjacentPoints(usedList[i])
        num=len(adjacent)
        if num == 0:
            stuck=True
        else :
            path=int(randrange(0,num))
            usedList.append(adjacent[path])
            i+=1
    return i

if plotting == 0:
    resultList2D = [] #This list will hold values taken from many iterations of random walks in 2D
    resultList3D = []
    for i in range(n) :
        if dimension != '3D' : #If the dimension variable is either '2D' or 'both', a random walk in 2D will run and its N steps will be appended to the list
            resultList2D.append(polymerWalk2D(size))
        if dimension !='2D' :  #If the dimension variable is either '3D' or 'both', a random walk in 3D will run and its N steps will be appended to the list
            resultList3D.append(polymerWalk3D(size))       
    if dimension == '2D' :
        hist(resultList2D)  #Creates a histogram of the distribution of polymer chain lengths in 2D
        title("Distribution of Polymer Chain Length in 2D (Grid Size: %d, Sample Size: %d)" % (size,n), loc='center')  
        xlabel("Monomers"); plt.ylabel("Frequency")  
        show()
    if dimension == '3D' :
        hist(resultList3D)  #Creates a histogram of the distribution of polymer chain lengths in 3D
        title("Distribution of Polymer Chain Length in 3D (Grid Size: %d, Sample Size: %d)" % (size,n), loc='center')  
        xlabel("Monomers"); plt.ylabel("Frequency")  
        show()
    if dimension == 'both' :
        subplot(2,1,1)
        hist(resultList2D) 
        title("Distribution of Polymer Chain Length in 2D (Grid Size: %d, Sample Size: %d)" % (size,n), loc='center')  
        xlabel("Monomers"); plt.ylabel("Frequency")  
        tight_layout()
        subplot(2,1,2)
        hist(resultList3D)  
        title("Distribution of Polymer Chain Length in 3D", loc='center')  
        xlabel("Monomers"); plt.ylabel("Frequency")  
        tight_layout()
        show()
    
if plotting == 1: 
    gridList = [ 6, 8, 10, 12, 16, 20, 25, 30, 35, 40, 50, 60, 80, 100] #This is the list of grid sizes that will run
    stepList2D = []
    stepList3D = []
    resultList2D = []
    resultList3D = []
    datax=[]
    datay=[]
    datax2D=[]
    datay2D=[]
    datax3D=[]
    datay3D=[]
    
    for each in gridList :
        for i in range(n):
            if dimension != '3D' :
                stepList2D.append(polymerWalk2D(each)) #Runs the simulation for a certain amount of times and records the number of steps taken for each
            if dimension != '2D' :
                stepList3D.append(polymerWalk3D(each)) 
        if dimension != '3D' : #If the dimension is either '2D' or both '2D' and '3D'
            avg2D=float(sum(stepList2D))/len(stepList2D) #Average number of steps for a certain grid size
            resultList2D.append([each,avg2D]) #The average value is stored in a list
        if dimension != '2D' :
            avg3D=float(sum(stepList3D))/len(stepList3D)
            resultList3D.append([each,avg3D])
        print(each)
    if dimension == '2D' :
        for each in resultList2D: #Sorts the grid sizes and lattice sites visited into their respective lists
            datax.append(each[0])
            datay.append(each[1])
        scatter(datax, datay) #Graphs a scatter plot of the grid size and the average number of steps taken for that grid size
        title("Scatter Plot of N Steps for Various Grid Sizes in 2D (Sample Size: %d)" % (n), loc='center')  
        xlabel("Grid Size"); plt.ylabel("Lattice Sites Visited")  
        show()
    if dimension == '3D' :
        for each in resultList3D:
            datax.append(each[0])
            datay.append(each[1])
        scatter(datax,datay)  
        title("Scatter Plot of N Steps for Various Grid Sizes in 3D (Sample Size: %d)" % (n), loc='center')  
        xlabel("Grid Size"); plt.ylabel("Lattice Sites Visited")
        show()
    if dimension == 'both' :
        for each in resultList2D:
            datax2D.append(each[0])
            datay2D.append(each[1])
        for each in resultList3D:
            datax3D.append(each[0])
            datay3D.append(each[1])
        subplot(2,1,1) #Creates a subplot for this scatter plot
        scatter(datax2D, datay2D) 
        title("Scatter Plot of N Steps for Various Grid Sizes in 2D (Sample Size: %d)" % (n), loc='center')  
        xlabel("Grid Size"); plt.ylabel("Lattice Sites Visited")  
        tight_layout()
        subplot(2,1,2)
        scatter(datax3D, datay3D)  
        title("Scatter Plot of N Steps for Various Grid Sizes in 3D (Sample Size: %d)" % (n), loc='center')  
        xlabel("Grid Size"); plt.ylabel("Lattice Sites Visited")  
        tight_layout()
        show()
    print(resultList2D)
    print(resultList3D)

    
    
