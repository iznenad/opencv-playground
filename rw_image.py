# Python program to explain cv2.imwrite() method
  
# importing cv2 
import cv2
  
# importing os module  
import os
  
# Image path
image_path = r'/Users/iznenad/dev/opencv/images/pic.png'
  
# Image directory
directory = r'/Users/iznenad/dev/opencv/images'
  
# Using cv2.imread() method
# to read the image
img = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)
  
# List files and directories  
print("Before saving image:")  
print(os.listdir(directory))  
  
# Filename
filename = 'images/savedImage.jpg'
  
# Using cv2.imwrite() method
# Saving the image
cv2.imwrite(filename, img)
  
# List files and directories 
print("After saving image:")  
print(os.listdir(directory))
  
print('Successfully saved')