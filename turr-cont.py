import cv2
import numpy as np
import time
import math
from detect import *
from dispBox import *

cv2.namedWindow("preview", )
vc = cv2.VideoCapture(0)

if vc.isOpened():  # try to get the first frame
    rval, frame = vc.read()
    #print(frame.shape)
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

squarePos = [0, 0, 0, 0] #[263/2.0, 428/2.0, 449/2.0, 613/2.0]

distance = 0.0

theta = 0.0
phi = 0.0
alpha = 0.0

first = True

name = ""

while rval:
    rval, frame = vc.read()

    if first:
        squarePos[0], squarePos[1], squarePos[2], squarePos[3], name = get_frame_info(frame)
        
        print("sqpos:", squarePos)
        print("name:", name)
        if squarePos[0] != 0 and squarePos[1] != 0 and squarePos[2] != 0 and squarePos[3] != 0:
            x1 = squarePos[0]-320
            y1 = 240-squarePos[1]
            x2 = squarePos[2]-320
            y2 = 240-squarePos[3]
            distance = ((averageFaceSize*screenWidth/2)/(math.tan(fovX*math.pi/360)*(x2-x1))+(averageFaceSize*screenHeight/2)/(math.tan(fovY*math.pi/360)*(y1-y2)))/2
            print("dist:", distance)
            Px = distance*(x2-x1)*math.tan(fovX*math.pi/360)/screenWidth
            Py = distance*(y1-y2)*math.tan(fovY*math.pi/360)/screenHeight
            Pz = distance
            print("x,y,z:", Px, Py, Pz)

    print()
    first = not first

    frame = draw_box(frame, squarePos[0], squarePos[1], squarePos[2], squarePos[3], name)
    cv2.imshow("preview", frame)

    key = cv2.waitKey(20)
    if key == 27: # exit on ESC
        break

cv2.destroyWindow("preview")
