import matplotlib.pyplot as plt
import numpy as np
import sys
from PyQt5.QtWidgets import QApplication

# colors 
guna_dark   = '#161C23'
nord_blue   = '#5e81ac'
nord_red    = '#bf616a'
nord_green  = '#8fbcbb'

# find DPI of your screen 
def getDPI(): 
	app = QApplication(sys.argv)
	screen = app.screens()[0]
	dpi = screen.physicalDotsPerInch()
	app.quit()
	return dpi  


# return 3 distinct contour values at random 
def randomContour(P): 
	# 3 random contour values
	# contour values must be distinct  
	randArray = [-1, -1, -1] 
	while randArray[0] == randArray[1] or randArray[1] == randArray[2] or randArray[0] == randArray[2]: 
		randArray[0] = np.random.randint(P)
		randArray[1] = np.random.randint(P)
		randArray[2] = np.random.randint(P)
	# contour values must be sorted
	randArray = np.sort(randArray)
	return randArray 


# setting guna background for matplotlib 
plt.rcParams['axes.facecolor']    = guna_dark
plt.rcParams['axes.edgecolor']    = guna_dark
plt.rcParams['savefig.edgecolor'] = guna_dark
plt.rcParams['savefig.facecolor'] = guna_dark

# step 
delta = .025
# Moduli 
P = np.random.randint(7, 40)
# screen dpi 
my_dpi = getDPI()

# x and y values 
xrange = np.arange(1, P, delta)
yrange = np.arange(1, P, delta)
X, Y = np.meshgrid(xrange,yrange)


# F is one side of the equation, G is the other
F = np.mod(np.floor(X)**2, P) 
G = np.mod(-np.floor(Y)**2, P)

# 3 distinct contour values
randArray = randomContour(P)
print(randArray)

# plot contour values 
plt.contour((F - G), randArray, colors = [nord_blue, nord_red, nord_green])
# remove x and y axis from plot 
plt.xticks([])
plt.yticks([])

# save image with screen resolution to fit wallpaper 
plt.savefig('fermat_prime.png', dpi = my_dpi)
plt.show()







