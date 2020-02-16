import cv2
import numpy as np
import time
import math

cv2.namedWindow("preview", )
vc = cv2.VideoCapture(1)

if vc.isOpened():  # try to get the first frame
    rval, frame = vc.read()
    print(frame.shape)
else:
    rval = False

screenWidth = 640.0
screenHeight = 480.0
fovX = 50
fovY = 40

averageFaceSize = 13.0
turretX = 0
turretY = 0
turretZ = 0

squarePos = (263/2.0, 428/2.0, 449/2.0, 613/2.0)

distance = 0.0

theta = 0.0
phi = 0.0
alpha = 0.0

first = True

while rval:
    if first:
        x1 = squarePos[0]-320
        y1 = 240-squarePos[1]
        x2 = squarePos[2]-320
        y2 = 240-squarePos[3]
        distance = ((averageFaceSize*screenWidth/2)/(math.tan(fovX*math.pi/360)*(x2-x1))+(averageFaceSize*screenHeight/2)/(math.tan(fovY*math.pi/360)*(y1-y2)))/2
        print(distance)
        Px = distance*(x2-x1)*math.tan(fovX*math.pi/360)/screenWidth
        Py = distance*(y1-y2)*math.tan(fovY*math.pi/360)/screenHeight
        Pz = distance
        print(Px, Py, Pz)

        first = False

    cv2.imshow("preview", frame)
    rval, frame = vc.read()
    key = cv2.waitKey(20)
    if key == 27: # exit on ESC
        break

cv2.destroyWindow("preview")