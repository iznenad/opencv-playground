import cv2

clicked = False

def mouseClicked(event, x, y, flags, param):
	global clicked 
	if event == cv2.EVENT_LBUTTONUP:
		clicked = True


cameraCapture = cv2.VideoCapture(0)

cv2.namedWindow('prozor', cv2.WINDOW_NORMAL)
cv2.setMouseCallback('prozor', mouseClicked)

success, frame = cameraCapture.read()

while success and cv2.waitKey(1) == -1 and not clicked:
	cv2.imshow('prozor', frame)
	success, frame = cameraCapture.read()

cv2.destroyWindow('prozor')