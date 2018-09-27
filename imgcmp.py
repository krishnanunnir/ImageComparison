# import the necessary packages
from skimage.measure import compare_ssim
import sys
import imutils
import cv2
import Image

def disparray(data):
	img = Image.fromarray(data)
	img.show()
img_name_one = raw_input("Enter the name of the first image?\n")
img_name_two = raw_input("Enter the name of second image?\n")
# load the two input images
imageA = cv2.imread(img_name_one)
imageB = cv2.imread(img_name_two)
# convert the images to grayscale
grayA = cv2.cvtColor(imageA, cv2.COLOR_BGR2GRAY)
grayB = cv2.cvtColor(imageB, cv2.COLOR_BGR2GRAY)
(score, diff) = compare_ssim(grayA, grayB, full=True)
diff = (diff * 255).astype("uint8")

 


thresh = cv2.threshold(diff, 0, 255, cv2.THRESH_BINARY_INV | cv2.THRESH_OTSU)[1]
cnts = cv2.findContours(thresh.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
cnts = cnts[0] if imutils.is_cv2() else cnts[1]
for c in cnts:
	# compute the bounding box of the contour and then draw the
	# bounding box on both input images to represent where the two
	# images differ
	(x, y, w, h) = cv2.boundingRect(c)
	cv2.rectangle(imageA, (x, y), (x + w, y + h), (0, 0, 255), 2)
	cv2.rectangle(imageB, (x, y), (x + w, y + h), (0, 0, 255), 2)
 
# show the output images
disparray(imageA)
disparray(imageB)

cv2.waitKey(0)


