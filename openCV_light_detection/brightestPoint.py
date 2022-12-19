import cv2 
import matplotlib.pyplot as plt
import numpy as np

# read in the images
norman = cv2.imread("/Users/petemango/beatSaberProject/openCV_light_detection/norman.png")
norman_rgb = np.copy(norman)

# convert the image to grey scale
norman_grey = np.copy(norman)
norman_grey = cv2.cvtColor(norman_grey, cv2.COLOR_BGR2GRAY)

# find the max brightness x and y values
max_x = cv2.minMaxLoc(norman_grey)[3][0]
max_y = cv2.minMaxLoc(norman_grey)[3][1]

# make a square of length 50 to display the brightest spot
s = 50
coordinate_left = (max_x - s, max_y - s)
coordinate_right = (max_x + s, max_y + s)
color = (255, 0, 0)
t = 5

brightest_box =np.copy(norman_rgb)
brightest_box = cv2.rectangle(brightest_box, coordinate_left, coordinate_right, color, t)

# show the plot
plt.subplot(1, 1, 1)  
plt.imshow(brightest_box, cmap="gray")  
plt.show()  

