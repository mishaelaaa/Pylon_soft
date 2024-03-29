import numpy as np
import cv2 as cv
from pypylon import pylon
import time 

#set up for timing loop
start_time = time.time()
#print("enter the seconds : ")
#seconds = input()
seconds = 5

# how img will be saved
num_img_to_save = 5
img = pylon.PylonImage()

# conecting to the first available camera
camera = pylon.InstantCamera(pylon.TlFactory.GetInstance().CreateFirstDevice())

# Grabing Continusely (video) with minimal delay
camera.StartGrabbing(pylon.GrabStrategy_LatestImageOnly) 
converter = pylon.ImageFormatConverter()

# converting to opencv bgr format
converter.OutputPixelFormat = pylon.PixelType_BGR8packed
converter.OutputBitAlignment = pylon.OutputBitAlignment_MsbAligned

#loop for video and shooting
while camera.IsGrabbing():
    grabResult = camera.RetrieveResult(2000, pylon.TimeoutHandling_ThrowException)
    
    #displaying video 
    if grabResult.GrabSucceeded():
        # Access the image data
        image = converter.Convert(grabResult)
        img = image.GetArray()
        cv.namedWindow('title', cv.WINDOW_AUTOSIZE) 
        cv.imshow('title', img)
        
        k=cv.waitKey(1)

        #exit
        if k == 27:
            cv.destroyAllWindows()
            break

        elif k == ord('s'):
            with camera.RetrieveResult(2000) as result:

                for i in range(num_img_to_save):

                    grabResult = camera.RetrieveResult(2000, pylon.TimeoutHandling_ThrowException)

                    image = converter.Convert(grabResult)
                    img = image.GetArray()

                    filename = "../Python/img/saved_pypylon_img_%d.png" % i
                    cv.imwrite(filename, img)
                    cv.destroyAllWindows()
                    time.sleep(seconds)

            exit(1)
# Releasing the resource    
camera.StopGrabbing()
camera.Close()

'''
        #saving
        elif k == ord('s'):
                for i in range(num_img_to_save):
                    with camera.RetrieveResult(2000) as result:
                        # Calling AttachGrabResultBuffer creates another reference to the
                        # grab result buffer. This prevents the buffer's reuse for grabbing.

                        #saving first with delay - 5 seconds
                        while i != num_img_to_save :
                            filename = "../Python/img/saved_pypylon_img_%d.png" % i
                            current_time = time.time()
                            elapsed_time = current_time - start_time
                            if elapsed_time > seconds:
                                cv.imwrite(filename, img)
                                cv.destroyAllWindows()
                                print("Finished iterating in: " + str(int(elapsed_time))  + " seconds")
                                time.sleep(seconds)
                                break    
            exit(1) 
'''