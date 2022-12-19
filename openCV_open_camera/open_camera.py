import cv2

# create video capturing
vid = cv2.VideoCapture(0)

while(True):
    ret, frame = vid.read()
    cv2.imshow('frame', frame)

    # press q to exit the video
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# release the video 
vid.release()
cv2.destroyAllWindows()