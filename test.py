import numpy as np
import sys
sys.path.append('/usr/local/lib/python2.7/site-packages')
import cv2

class PIC:
    def __init__(
        self,
        pic_name = "",
        drawing = False,
        ix = -1,
        iy = -1,
    ):
        self.x_start = []
        self.x_end = []
        self.y_start = []
        self.y_end = []

#drawing = False
#ix,iy = -1,-1

def draw_circle(event,x,y,flags,param):
    pic = PIC
    #global ix,iy,drawing
    if event == cv2.EVENT_LBUTTONDOWN:
        print 'Push'
        pic.drawing = True
        pic.ix,pic.iy = x,y
        pic.x_start = np.append(pic.x_start, x)
        pic.y_start = np.append(pic.y_start, y)

    elif event == cv2.EVENT_MOUSEMOVE:
        if pic.drawing == True:
            print 'Drawing...'
        else:
            pass
    elif event == cv2.EVENT_LBUTTONUP:
        print 'Up'
        pic.drawing = False
        cv2.rectangle(img,(pic.ix,pic.iy),(x,y),(0,255,0),1)
        pic.x_end = np.append(pic.x_end, x)
        pic.y_end = np.append(pic.y_end, y)

img = cv2.imread( "/Users/royroy55/Desktop/a.png")
cv2.namedWindow('image')
cv2.setMouseCallback('image',draw_circle)

while(1):
    cv2.imshow('image',img)
    k = cv2.waitKey(1) & 0xFF
    if k == 27:
        break

cv2.destroyAllWindows()
