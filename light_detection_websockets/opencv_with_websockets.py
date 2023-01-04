import cv2
import numpy as np
import threading
import json
from light_detection import *
from SimpleWebSocketServer import SimpleWebSocketServer, WebSocket

server = None
clients = []


class simple_websocket_server (WebSocket):
    def handleConnected(self):
        clients.append(self)

    def handleClose(self):
        clients.remove(self)


class Coord:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return "Coord: ({self.x}, {self.y})"


def run_server():
    global server
    server = SimpleWebSocketServer(
        '', 9000, simple_websocket_server, selectInterval=(1000.0/15) / 1000)
    server.serveforever()


def remove_front(arr, n):
    arr_len = len(arr)
    if arr_len < n:
        return []
    while n > 0:
        arr.pop(0)
        n -= 1
    return arr


thread = threading.Thread(target=run_server)
thread.start()
thread = 100
w = 640


color = (0, 255, 0)
thickness = 9
frames_tracked = 10
cur_len = 0

vid = cv2.VideoCapture(0)
coords = []

if not vid.isOpened():
    print("Cannot open camera")
    exit()

while (cv2.waitKey(1) & 0xFF != ord('q')):
    # Get current frame
    ret, frame = vid.read()
    if not ret:
        print("Stopped receiving stream. Exiting ...")
        break

    brightest_point = get_brightest_point(frame)
    x = brightest_point['center_x']
    y = brightest_point['center_y']
    c = Coord(x, y)

    coords.append(c)
    cur_len += 1

    frames_exceeded = cur_len - frames_tracked

    if cur_len > frames_tracked:
        remove_front(coords, frames_exceeded)
        cur_len -= frames_exceeded

    print(c)

    for i in range(1, cur_len):
        prev_x = coords[i].x
        prev_y = coords[i].y
        cur_x = coords[i-1].x
        cur_y = coords[i-1].y

        prev_point = (prev_x, prev_y)
        cur_point = (cur_x, cur_y)
        cv2.line(frame, prev_point, cur_point, color, thickness)

    cv2.imshow('frame', frame)

vid.release()
cv2.destroyAllWindows()
server.close()