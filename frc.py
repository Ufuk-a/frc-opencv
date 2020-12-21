import cv2 as cv
import numpy as np
import sys

def main():    
    if len(sys.argv) >= 2:    
        img_bgr = cv.imread(sys.argv[1])
        img = cv.cvtColor(img_bgr, cv.COLOR_BGR2HSV)
        min_green = np.array([57, 100, 100])
        max_green = np.array([97, 255, 255])
        kernel = cv.getStructuringElement(cv.MORPH_ELLIPSE,(2,2))
        
        while True:    

            
            mask = cv.inRange(img, min_green, max_green)
            mask = cv.morphologyEx(mask, cv.MORPH_OPEN, kernel)
            mask = cv.morphologyEx(mask, cv.MORPH_CLOSE, kernel)
            contours, _ = cv.findContours(mask, cv.RETR_TREE, cv.CHAIN_APPROX_SIMPLE)
            for contour in contours:
                #x,y,w,h = cv.boundingRect(contour)
                #cv.rectangle(img_bgr,(x,y),(x+w,y+h),(0,255,0),2)
                rect = cv.minAreaRect(contour)
                box = cv.boxPoints(rect)
                box = np.int0(box)
                cv.drawContours(img_bgr,[box],0,(0,255,0),2)
                left = box[2][1]
                right = box[0][1]
                top = box[1][0]
                bot = box[3][0]
                height = bot + top
                width = right + left
                middle = (int(height/2), int(width/2))
                cv.circle(img_bgr, middle, 5, (255, 0, 0), 5)
                
            cv.imshow("img", img_bgr)
            cv.imshow("mask", mask)
        
            if cv.waitKey(1) == ord("q"):
                break
    else:
        print("You need to input a proper image")
        
if __name__ == '__main__':
    main()    
    
    
    
    
    
