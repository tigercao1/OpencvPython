import cv2
import numpy as np

img = cv2.imread("res/tiger.jpg")

hor = np.hstack((img, img, img))
ver = np.vstack((img,img))

cv2.imshow("horizontal", hor)
cv2.imshow("vertical", ver)


while True:
    if cv2.waitKey(0) & 0xFF == ord("q"):
        break