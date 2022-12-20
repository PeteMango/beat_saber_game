import cv2
import matplotlib.pyplot as plt
import numpy as np

# create video capturing
vid = cv2.VideoCapture(0)

if not vid.isOpened():
    print("Cannot open camera")
    exit()

while (True):
    # Get current frame
    ret, frame = vid.read()
    if not ret:
        print("Stopped receiving stream. Exiting ...")
        break

    #copy pasted from the brightest-point-detection
    image_np = np.array(frame)

    # Display the resulting frame
    cv2.imshow('frame', frame)

    # process the frame
    img_main = frame
    img_rgb = np.copy(img_main)

    # convert the image to grey scale
    img_grey = np.copy(img_main)
    img_grey = cv2.cvtColor(img_grey, cv2.COLOR_BGR2GRAY)

    # find the max brightness x and y values
    max_x = cv2.minMaxLoc(img_grey)[3][0]
    max_y = cv2.minMaxLoc(img_grey)[3][1]

    # make a square of length 50 to display the brightest spot
    s = 50
    coordinate_left = (max_x - s, max_y - s)
    coordinate_right = (max_x + s, max_y + s)
    color = (255, 0, 0)
    t = 5

    brightest_box = np.copy(img_rgb)
    brightest_box = cv2.rectangle(
        brightest_box, coordinate_left, coordinate_right, color, t)

    # show the plot
    plt.subplot(1, 1, 1)
    plt.imshow(brightest_box, cmap="gray")
    plt.show()

    # press q to exit the video
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# release the video
vid.release()
cv2.destroyAllWindows()
