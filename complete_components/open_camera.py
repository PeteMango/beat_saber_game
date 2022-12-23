import cv2
import numpy as np
from detect_light import *
color = (0, 255, 0)
thickness = 9

# create video capturing
vid = cv2.VideoCapture(0)
x_coord = []
y_coord = []

if not vid.isOpened():
    print("Cannot open camera")
    exit()

while (True):
    # Get current frame
    ret, frame = vid.read()
    if not ret:
        print("Stopped receiving stream. Exiting ...")
        break

    # Call image processing function
    result = get_brightest_point(frame)

    brightest_point = get_brightest_point_coordinates(frame)
    x = brightest_point['center_x']
    y = brightest_point['center_y']

    x_coord.append(x)
    y_coord.append(y)

    array_length = len(x_coord)
    for i in range (1, array_length):
        prev_x = x_coord[i]
        prev_y = y_coord[i]
        cur_x = x_coord[i-1]
        cur_y = y_coord[i-1]
        # print(prev_x, prev_y, cur_x, cur_y)

        prev_point = (prev_x, prev_y)
        cur_point = (cur_x, cur_y)
        cv2.line(frame, prev_point, cur_point, color, thickness)

    # Display the resulting frame
    cv2.imshow('frame', frame)


    # press q to exit the video
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# release the video
vid.release()
cv2.destroyAllWindows()

for x in x_coord:
    print(x)

for y in y_coord:
    print(y)
