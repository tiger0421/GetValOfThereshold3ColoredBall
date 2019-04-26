import cv2
import numpy as np

flag = 1
def nothing(x):
	pass

cv2.namedWindow("Blue")
cv2.namedWindow("Red")
cv2.namedWindow("Yellow")

cv2.createTrackbar("H", "Blue", 0, 255, nothing)
cv2.createTrackbar("S", "Blue", 0, 255, nothing)
cv2.createTrackbar("V", "Blue", 0, 255, nothing)
cv2.createTrackbar("H", "Red", 0, 255, nothing)
cv2.createTrackbar("S", "Red", 0, 255, nothing)
cv2.createTrackbar("V", "Red", 0, 255, nothing)
cv2.createTrackbar("H", "Yellow", 0, 255, nothing)
cv2.createTrackbar("S", "Yellow", 0, 255, nothing)
cv2.createTrackbar("V", "Yellow", 0, 255, nothing)

while flag == 1:
	img = cv2.imread('1530255752584.jpg')

	hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
	hsv = cv2.morphologyEx(hsv, cv2.MORPH_OPEN, np.ones((5, 5), np.uint8))

#Blue
	h_blue = cv2.getTrackbarPos("H", "Blue")
	s_blue = cv2.getTrackbarPos("S", "Blue")
	v_blue = cv2.getTrackbarPos("V", "Blue")

	lower_blue = np.array([h_blue, s_blue, v_blue])	#h100 s110 v60?
	upper_blue = np.array([120, 255, 255])
	mask_blue = cv2.inRange(hsv, lower_blue, upper_blue)

#Red
	h_red = cv2.getTrackbarPos("H", "Red")
	s_red = cv2.getTrackbarPos("S", "Red")
	v_red = cv2.getTrackbarPos("V", "Red")

	lower_red = np.array([0, s_red, v_red])#s100 v60
	upper_red = np.array([h_red, 255, 255])
	mask1 = cv2.inRange(hsv, lower_red, upper_red)
	lower_red = np.array([156, 128, 81])
	upper_red = np.array([255, 255, 255])
	mask2 = cv2.inRange(hsv, lower_red, upper_red)
	mask_red = mask1 + mask2

#yellow
	h_yellow = cv2.getTrackbarPos("H", "Yellow")
	s_yellow = cv2.getTrackbarPos("S", "Yellow")
	v_yellow = cv2.getTrackbarPos("V", "Yellow")

	lower_yellow = np.array([h_yellow, s_yellow, v_yellow])#h18 s90 v110
	upper_yellow = np.array([30, 255, 255])
	mask_yellow = cv2.inRange(hsv, lower_yellow, upper_yellow)

	cv2.imshow("Blue", mask_blue)
	cv2.imshow("Red", mask_red)
	cv2.imshow("Yellow", mask_yellow)

	cv2.imshow("image", img)

	if cv2.waitKey(1) == ord('q'):
		flag = 0

