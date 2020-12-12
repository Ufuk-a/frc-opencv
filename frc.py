import cv2 as cv
import numpy as np
import sys

def main():    
<<<<<<< HEAD
    print(sys.argv[1])
    if len(sys.argv) >= 2:    
        img_bgr = cv.imread(sys.argv[1])
        img = cv.cvtColor(img_bgr, cv.COLOR_BGR2HSV)
=======
    # img_bgr = cv.imread(r"C:\Users\altin\Documents\GitHub\frc-opencv\image_examples\BlueGoal-Far-ProtectedZone.jpg")
    img_bgr = cv.imread("image_examples/BlueGoal-Far-ProtectedZone.jpg")
    img = cv.cvtColor(img_bgr, cv.COLOR_BGR2HSV)
>>>>>>> 36362115e6bac0c9d35cbdd6d93616a709bce964

        while True:    
            min_green = np.array([57, 100, 100])
            max_green = np.array([97, 255, 255])

            mask = cv.inRange(img, min_green, max_green)
            contours, _ = cv.findContours(mask, cv.RETR_TREE, cv.CHAIN_APPROX_SIMPLE)
            for contour in contours:
                #x,y,w,h = cv.boundingRect(contour)
                #cv.rectangle(img_bgr,(x,y),(x+w,y+h),(0,255,0),2)
                rect = cv.minAreaRect(contour)
                box = cv.boxPoints(rect)
                box = np.int0(box)
                cv.drawContours(img_bgr,[box],0,(0,255,0),2)
            
            cv.imshow("img", img_bgr)
            cv.imshow("mask", mask)
        
            if cv.waitKey(1) == ord("q"):
                break
    else:
        print("You need to input a proper image")
        
if __name__ == '__main__':
    main()    