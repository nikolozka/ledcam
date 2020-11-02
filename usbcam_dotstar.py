import time
import random
import board
import numpy as np
import cv2
import opc
import adafruit_dotstar as dotstar

n_dots = 144

dots = dotstar.DotStar(11, 10, n_dots, brightness=1.0, auto_write=False)

#create capture device
#cap = cv2.VideoCapture(0) #might need expirimentation to figure out the argument ls /dev/video* is a starting point
cap = cv2.VideoCapture("../testfiles/test.mp4") #videofile
ADDRESS = 'localhost:7890'

print('press Ctrl+C to quit disposing of resources properly')

for dot in range(n_dots):
    dots[dot] = (0,0,0)
dots.show()


try:
    while(True):
        # make sure the device is open
        if(not cap.isOpened()):
            cap.open()

        #read next frame

        ret, frame = cap.read()

        #do loop if capture returned sensible info
        if(ret):
        #operations on the frame come here if you need high res manipulation
            gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

        #scale down
            dim = (16,9)
            small = cv2.resize(frame, dim, interpolation = cv2.INTER_LINEAR)

        #or here if you want to manipulate on the led scale
            smallgray = cv2.cvtColor(small, cv2.COLOR_BGR2GRAY)

        #convert to RGB (cv2 runs on BGR frames in the backend)
            smallrgb = cv2.cvtColor(small, cv2.COLOR_BGR2RGB)

            pushline = smallrgb[:,0]


        #write to fadecandies
            for i in range(15):
                if(i%2==0):
                    pushline = np.append(pushline,smallrgb[:,i+1], axis=0)
                else:
                    flipline = np.flip(smallrgb[:,i+1], axis=0)
                    pushline = np.append(pushline,flipline, axis=0)

            for dot in range(n_dots):
                dots[dot] = (pushline[dot][0],pushline[dot][1],pushline[dot][2])
            dots.show()
        #display camera preview
            window_name = 'image'
#            cv2.imshow(window_name, frame) #uncomment for preview
            cv2.waitKey(1)

except KeyboardInterrupt:
        print('releasing camera')
        cap.release()
        for dot in range(n_dots):
            dots[dot] = (0,0,0)
        dots.show()

        cv2.destroyAllWindows() 
        exit()

# When everything done, release the capture
