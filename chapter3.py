import cv2
import numpy as np

img = cv2.imread("res/lambo.jpeg")
print(img.shape)

resize_img = cv2.resize(img, (2000,1600))
print(resize_img.shape)

cropped_img = img[200:600, 200:500]

cv2.imshow("img", img)
cv2.imshow("resized img", resize_img)
cv2.imshow("cropped img", cropped_img)

while True:
    if cv2.waitKey(0) & 0xFF == ord("q"):
        break