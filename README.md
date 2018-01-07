Polymer Walk

Physical System

For my final project, I decided to investigate self-avoiding random walks in space, particularly in the system of long chain polymers. There are two types of models for polymer chains: “ideal” models, and “real” models. This project covers the “real” aspect of polymer chains, which follows that polymer segments cannot occupy the same space at the same time, an interaction commonly referred to as the excluded volume interaction. A model that satisfies the excluded volume interaction is the self-avoiding random walk, a random walk that cannot repeat its previous path. A path of this walk in three dimensions represents a conformation of a polymer, with the excluded volume interaction. Two models will be created, one in (second dimension) and the other in  (third dimension). These models will be able to compute the average number of monomers given any lattice square/cube,  and visually simulate a polymer chain forming. 
Theory

The first goal of this project is to compute the number of self-avoiding walks (SAW) in any given lattice. However, there is currently no general formula for determining the number of self-avoiding walks. One of the programs for this project will produce graphs displaying the average number of steps taken for a certain grid size in either 2D or 3D. A statistical analysis can be done on the data, which will give us a model for determining the number of random self-avoiding walks for a certain square grid size.

Method

The first program I created is a model of a 2D square lattice of monomers. This program takes the side length of the lattice square as input, and displays a square of points with the inputted integer as its side length, and then simulates a self-avoiding random walk starting at the center of the square. The program records the number of steps it takes to stop. The second program I created is a model of a 3D cube lattice of monomers. This program is almost identical to the 2D program, with a few additions. The program will display a 3D cube of points, and once clicked, the random walk will start. A control window will also appear, with the option to turn the points on or off. Turning the points off will make the grid of points disappear, but the curve will still be visible. This is useful if the user wants a clearer view of the curve. The curve will also change color every 100 steps. The heart of these programs is outputting possible paths when given a point in the grid. The program first tests whether the point is on a side in the grid. If so, then the point won’t have a possible path in the direction of that side. The path also cannot be a path that the walk has already taken. The program checks all sides of the point, and then randomly chooses a path out of the available paths to take. 
The third program I created is the graph program. This programs uses code from the previous two programs to generate data for the graphs, but does not include a visual simulation of a polymer chain forming.  This program will generate graphs for a random walk simulation in either 2D or 3D or both. The user has the option to either generate a histogram of a single grid size over a certain sample size, or a scatter plot of of many grid sizes over a certain sample size. 

Verification

For the 2D and 3D polymer simulations, I ensured that the inputted size had to be an integer greater than 1. This was done by adding a while statement, which looped until the user gave a value greater than 1. I also ensured that the programs would run for any odd or even side length. This part was a little complicated because for any grid of points with an even side length, there really is no center point. The program generates the grid by making the center of the grid the origin. In the case of an even side length, there is always a center square/cube of points in the grid. In the graph program, I made sure that the inputted variables would comply with the program. As with the other programs, this was done with a while loop, which iterated until a correct value was inputted.  


Critique

This project has given me a better understanding of polymer physics and random walks. I found it very interesting how polymers form in a similar pattern as random self-avoiding walks. Initially, I knew I wanted to focus my project on some sort of random simulation that occurs in the natural world. After researching random occurrences in natural phenomena, I came across polymer formations and random walks. In terms of coding, I learned a lot about the visual aspect of vpython. I was able to create a 2D and 3D grid of points and have a curve run through the points, something that I did not know how to do prior to the project. Besides python and canopy, I also used LoggerPro to analyze the plots.  Overall, this project was a great learning experience and I would be excited to continue the project in the future.
Several things that could be improved about the programs are efficiency and runtime and the curve glitch in the 3D program. In the current version of vpython, the maximum amount of points a curve can store is a thousand. Often with a large grid size, the total number of steps for a 3D simulation will exceed 1000, which will cause the curve to flicker on and off repeatedly. If possible, an improvement could be made to find a way around this limit. Another improvement could be to decrease the runtime and increase the efficiency for the graphing program. As of now, the program takes forever to generate 3D graphs, especially for large sample sizes and grid sizes. There could be a more efficient method of finding the possible paths that the curve could take, and an improvement would be to find this method. 
 
References
http://www.labri.fr/perso/bousquet/Exposes/fpsac-saw.pdf
http://physics.weber.edu/thermal/isingVPython.html
http://en.wikipedia.org/wiki/Polymer_physics
http://ww2.odu.edu/~agodunov/teaching/phys420/projects.html
http://en.wikipedia.org/wiki/Self-avoiding_walk































