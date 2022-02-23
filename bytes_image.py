import cv2
import numpy
import os

# Make an array of 120,000 random bytes
randomByteArray = bytearray(os.urandom(120000))

flatNumpyArray = numpy.array(randomByteArray)

# Convert the array into 300x400 grayscale image
grayimage = flatNumpyArray.reshape(300, 400)
cv2.imwrite('images/random-gray.png', grayimage)

# Convert the array into 300x400 rgb image
rgbImage = flatNumpyArray.reshape(200, 200, 3) # 3 colours are the 3rd dimension?
cv2.imwrite('images/random-rgb.png', rgbImage)