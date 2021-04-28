import cv2
import numpy as np

img = cv2.imread("res/cards.jpeg")
print(img.shape)
width = 500
height = 700

pts1 = np.float32([[796,92],[460,756],[897,962],[1200,300]])
pts2 = np.float32([[0,0],[0,height],[width,height],[width,0]])
matrix = cv2.getPerspectiveTransform(pts1, pts2)

imgOutput = cv2.warpPerspective(img, matrix, (width, height))

cv2.imshow("cards", img)
cv2.imshow("output", imgOutput)

while True:
    if cv2.waitKey(0) & 0xFF == ord("q"):
        break