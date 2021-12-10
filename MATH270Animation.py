"""
Project: Mathematics 270 - Starter Code for 2d Animations
File: 2dAnimationStartCodeExample.py
Description: For creating objects and performing the animations.  
             The linear transformations must be defined in the module "AnimationClassStudents.py" 
Author: Dr. Greg Rainwater
"""
import matplotlib.pyplot as plt
import numpy as np
import math

class AnimationObject:
    def __init__(self, matrix):
        self.matrix = matrix
        onesRow = np.ones(self.matrix.shape[1])
        self.matrix = np.vstack((self.matrix, onesRow))

    def rotate(self, radians,about='origin'):
        cos_t = math.cos(radians)
        sin_t = math.sin(radians)
        if about == 'origin':
            self.matrix = np.matrix(' %s %s  0;'
                                    ' %s %s  0;'
                                    '  0  0  1' % (cos_t, -sin_t, sin_t, cos_t)) * self.matrix
        elif about == 'point':
            xpoint = self.matrix[0,0]
            ypoint = self.matrix[1,0]
            self.translate(-xpoint,-ypoint)
            self.matrix = np.matrix(' %s %s  0;'
                                    ' %s %s  0;'
                                    '  0  0  1' % (cos_t, -sin_t, sin_t, cos_t)) * self.matrix
            self.translate(xpoint,ypoint)

        elif about == 'center':
            xpoint = np.mean(self.matrix[0,:])
            ypoint = np.mean(self.matrix[1,:])
            self.translate(-xpoint,-ypoint)
            self.matrix = np.matrix(' %s %s  0;'
                                    ' %s %s  0;'
                                    '  0  0  1' % (cos_t, -sin_t, sin_t, cos_t)) * self.matrix
            self.translate(xpoint,ypoint)
    def translate(self, dx=0, dy=0):
        self.matrix = np.matrix(' 1  0 %s;'
                                ' 0  1 %s;'
                                ' 0  0  1' % (dx, dy)) * self.matrix

    def scale(self, dx=1, dy=1):
        self.matrix = np.matrix('%s  0  0;'
                                ' 0 %s  0;'
                                ' 0  0  1' % (dx, dy)) * self.matrix

    def reflect(self, axis='x',about='origin'):
        if about == 'point':
            xpoint = self.matrix[0,0]
            ypoint = self.matrix[1,0]
        else:
            xpoint = 0
            ypoint = 0
        self.translate(-xpoint,-ypoint)
        if axis == 'x':
            self.matrix = np.matrix(' 1  0  0; '
                                    ' 0 -1  0; '
                                    ' 0  0  1') * self.matrix
        elif axis == 'y':
            self.matrix = np.matrix('-1  0  0; '
                                    ' 0  1  0; '
                                    ' 0  0  1') * self.matrix
        elif axis == 'xy':
            self.matrix = np.matrix(' 0  1  0; '
                                    ' 1  0  0; '
                                    ' 0  0  1') * self.matrix
        elif axis == 'nxy':
            self.matrix = np.matrix('-1  0  0; '
                                    ' 0 -1  0; '
                                    ' 0  0  1') * self.matrix

        self.translate(xpoint,ypoint)

    def shear(self, dx=0, dy=0):
        self.matrix = np.matrix(' 1 %s  0; '
                                '%s  1  0; '
                                ' 0  0  1' % (dx, dy)) * self.matrix
    def putOrigin(self):
        xpoint = self.matrix[0,0]
        ypoint = self.matrix[1,0]
        self.translate(-xpoint,-ypoint)
#    def plot(self, clrfig=1,xMin=-5,xMax=30,yMin=-5,yMax=30):   
    def plot(self, clrfig=1,xMin=-20,xMax=20,yMin=-20,yMax=20,tcolor=''): 
        if clrfig == 1:
            plt.gcf().clear()
        if tcolor == '':
            plt.plot(np.transpose(self.matrix[0, :]), np.transpose(self.matrix[1, :]))
        else:
            plt.plot(np.transpose(self.matrix[0, :]), np.transpose(self.matrix[1, :]),color=tcolor)
        plt.xlim(xMin, xMax)       
        plt.ylim(yMin, yMax)
        plt.show()
    def plot2(self, clrfig=1,pxlim=100,pylim=100,tcolor=''):
        if clrfig == 1:
            plt.gcf().clear()
        # plt.gcf().clear()
        if tcolor == '':
            plt.plot(np.transpose(self.matrix[0, :]), np.transpose(self.matrix[1, :]))
        else:
            plt.plot(np.transpose(self.matrix[0, :]), np.transpose(self.matrix[1, :]),color=tcolor)
        plt.xlim(0,pxlim)
        plt.ylim(0,pylim)
        plt.show()

if __name__ == "__main__":
    """
# ------------------------------------------------------
# Create Your Object(s)
#    - Store the vertices of the object in a 2 x n matrix where the x coordinates of the vertices are stored in first row and the y coordinates in the second row.
#    Each successsive pair of points is connected by a straight line.
# ---
#  EXAMPLE: 
# --- 
# Consider the parallelogram formed by the vertices (2,0), (1,2), (2,4) and (3,2) .
#    Form Object matrix using vertices as columns and adding starting vector (2,0) onto tail/end (otherwise we would be missing a line) is M=( 2 1 2 3 2; 0, 2, 4, 2 0) 
#  M=np.matrix('2 1 2 3 2; 0, 2, 4, 2 0')
#  Obj1= Ani.Matrix(M)
# ------------------------------------------------------
    """

    # !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
    # !!!! INSERT OBJECT CREATION CODE HERE!!
    # !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
sun = AnimationObject(np.matrix("5 6 6 5 5; 10 10 9 9 10"))
bee = AnimationObject(np.matrix("7 6 6 8 8 7 6 7 8 7; 8 8 6 6 8 8 9 8 9 8"))
bee2 = AnimationObject(np.matrix("9 8 8 10 10 9 8 9 10 9; 8 8 6 6 8 8 9 8 9 8"))
bird1 = AnimationObject(np.matrix("0 1 2 1 0; 4 3 4 3 4"))
bird2 = AnimationObject(np.matrix("2 3 4 3 2; 6 5 6 5 6"))
boat = AnimationObject(np.matrix('0 1 4 5 4 2.5 2.5 2 2.5 2.5 1 0; 1 0 0 1 0 0 3 2 1 0 0 1'))
tree = AnimationObject(np.matrix("1 2 2 1 1 1 0 1 2 3 2 1; 0 0 2 2 0 2 3 4 4 3 2 2"))
tree2 = AnimationObject(np.matrix("4 5 5 4 4 4 3 4 5 6 5 4; 0 0 2 2 0 2 3 4 4 3 2 2"))


plt.title("Gabrielle Lake's Animation")
plt.ion()  # Initialize plot (keep this...it is important)
plt.xlim([0, 10])
plt.ylim([0, 10])

print("Gabrielle Lake")
"""
# ------------------------------------------------------
# Begin Animations! (If you need help then come see me or the TA)
# ------------------------------------------------------
"""
# !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
# !!!! INSERT ANIMATION CODE HERE  !!!!!!
# !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!


for i in range(0, 15):
	# Sun rotating in the sky while a bird flys by
	sun.plot(tcolor="yellow")
	bird1.plot(0, tcolor="blue")

	bird1.reflect("x", "origin") # Reflect over the x-axis
	sun.rotate(np.pi/4,'center') # Rotation about the object

	bird1.translate(0.5, 1) # Translation
	bird1.scale(1.2, 1.2)
	
	plt.pause(.2)

for i in range(0, 10):
	# Bird flying by while a boat gets closer
	bird2.plot(tcolor="green")
	boat.plot(0, tcolor="orange")

	bird2.reflect("x", "origin")

	bird2.translate(0.5, 1)
	boat.translate(0.2, 0)

	boat.scale(1.2, 1.2) # Scaling
	bird2.scale(1.2, 1.2)
	
	plt.pause(.2)

for i in range(0, 10):
	# Two trees swaying in the wind
	tree.plot(tcolor="brown")
	tree2.plot(0, tcolor="green")
	tree.shear(0.1) # Shearing
	tree2.shear(0.1)
	plt.pause(.2)

for i in range(0, 11):
	# Two trees swaying in the wind
	tree.plot(tcolor="brown")
	tree2.plot(0, tcolor="green")
	tree.shear(-0.1)
	tree2.shear(-0.1)
	plt.pause(.2)

for i in range(0, 10):
	# Two trees swaying in the wind
	tree.plot(tcolor="brown")
	tree2.plot(0, tcolor="green")
	tree.shear(0.1)
	tree2.shear(-0.1)
	plt.pause(.2)

for i in range(0, 11):
	# Two trees swaying in the wind
	tree.plot(tcolor="brown")
	tree2.plot(0, tcolor="green")
	tree.shear(-0.1)
	tree2.shear(0.1)
	plt.pause(.2)

for i in range(0, 15):
	# Two bees flying around
	bee2.plot(tcolor="blue")
	bee.plot(0, tcolor="red")
	bee2.rotate(60) # Rotation about the origin
	bee.rotate(30)
	plt.pause(.2)

for i in range(0, 15):
	# The 2nd bee flying away
	bee2.plot(tcolor="blue")
	bee.plot(0, tcolor="red")
	bee2.reflect("xy") # Reflect the object over a line
	bee2.translate(1, 1)
	bee.rotate(30)
	plt.pause(.2)