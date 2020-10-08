
import numpy as np
import cv2
import opc

#create capture device
cap = cv2.VideoCapture(0) #might need expirimentation to figure out the argument ls /dev/video* is a starting point
ADDRESS = 'localhost:7890'

# Create a client object
client = opc.Client(ADDRESS)

# Test if it can connect
if client.can_connect():
    print ('connected to %s' % ADDRESS)
else:
    # We could exit here, but instead let's just print a warning
    # and then keep trying to send pixels in case the server
    # appears later
    print ('WARNING: could not connect to %s' % ADDRESS)


print('press Ctrl+C to quit disposing of resources properly')
try:
    while(True):
        # make sure the device is open
        if(not cap.isOpened()):
            cap.open()

        #read next frame

        ret, frame = cap.read()

        #print(frame.shape) #debug leftovers

        #do loop if capture returned sensible info
        if(ret):
        #display camera preview
            window_name = 'image'
            cv2.imshow(window_name, image)     
        #operations on the frame come here if you need high res manipulation
            gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

        #scale down
            dim = (16,21)
            small = cv2.resize(frame, dim, interpolation = cv2.INTER_AREA)

            #print(small.shape) #debug leftovers
            #cv2.imwrite('color_img.jpg', small)

        #or here if you want to manipulate on the led scale
            smallgray = cv2.cvtColor(small, cv2.COLOR_BGR2GRAY)

        #convert to RGB (cv2 runs on BGR frames in the backend)
            smallrgb = cv2.cvtColor(small, cv2.COLOR_BGR2RGB)

        #write to fadecandies
            for i in range(16):
                pushline = smallrgb[:,i]

                #print(pushline.shape) #debug leftovers
                #print(pushline)

                if client.put_pixels(pushline, channel=i):
                    print ('sent')
                else:
                    print ('not connected')

    # Display the resulting frame
#    c = cv2.waitKey(25) & 0xFF
#    if c == ord('q'):
#        break

except KeyboardInterrupt:
        print('releasing camera')
        cap.release()
        cv2.destroyAllWindows()
        exit()

# When everything done, release the capture
