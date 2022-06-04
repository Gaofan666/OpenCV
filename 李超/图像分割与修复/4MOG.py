import cv2
import numpy as np

cap = cv2.VideoCapture('../img/vtest.avi')
# mog = cv2.bgsegm.createBackgroundSubtractorMOG()
# mog = cv2.createBackgroundSubtractorMOG2()
mog = cv2.bgsegm.createBackgroundSubtractorGMG(10)

while (True):
    ret, frame = cap.read()
    fgmask = mog.apply(frame)

    cv2.imshow('img', fgmask)

    k = cv2.waitKey(10)
    if k == 113:
        break

cap.release()
cv2.destroyAllWindows()
