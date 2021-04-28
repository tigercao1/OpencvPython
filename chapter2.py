import cv2
import numpy as np

img = cv2.imread("res/tiger.jpg")

kernel = np.ones((5, 5), np.uint8)

img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
img_blur = cv2.GaussianBlur(img_gray, (7, 7), 0)
img_canny = cv2.Canny(img, 150, 200)
img_dilation = cv2.dilate(img_canny, kernel, iterations=1)
img_eroded = cv2.erode(img_dilation, kernel, iterations=1)

cv2.imshow("Gray img", img_gray)
cv2.imshow("Blur img", img_blur)
cv2.imshow("Canny img", img_canny)
cv2.imshow("Dilation img", img_dilation)
cv2.imshow("erotion img", img_eroded)


while True:
    if cv2.waitKey(0) & 0xFF == ord("q"):
        break