import cv2

cameraCapture = cv2.VideoCapture(0)
fps = 30 # a guess
width = cameraCapture.get(cv2.CAP_PROP_FRAME_WIDTH)
height = cameraCapture.get(cv2.CAP_PROP_FRAME_HEIGHT)
size = int(width), int(height)

videoWriter = cv2.VideoWriter('videos/camera-capture.ogg', cv2.VideoWriter.fourcc('T', 'H', 'E', 'O'), fps, size)

videoLength = fps * 10 # 10 seconds

success, frame = cameraCapture.read()

while success and videoLength > 0:
	videoLength -= 1 # a second of video was taken
	videoWriter.write(frame)
	success, frame = cameraCapture.read()
	
