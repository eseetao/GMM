'''
ECE276A WI19 HW1
Blue Barrel Detector
'''

import os, cv2
from skimage.measure import label, regionprops

import matplotlib.pyplot as plt 

from DataLoader import DataLoader
from LogisticRegression import LogisticRegression

class BarrelDetector():
	def __init__(self):
		'''
			Initilize your blue barrel detector with the attributes you need
			eg. parameters of your classifier
		'''
		

	def segment_image(self, img):
		'''
			Calculate the segmented image using a classifier
			eg. Single Gaussian, Gaussian Mixture, or Logistic Regression
			call other functions in this class if needed
			
			Inputs:
				img - original image
			Outputs:
				mask_img - a binary image with 1 if the pixel in the original image is blue and 0 otherwise
		'''
		# YOUR CODE HERE
		
		return mask_img

	def get_bounding_box(self, img):
		'''
			Find the bounding box of the blue barrel
			call other functions in this class if needed
			
			Inputs:
				img - original image
			Outputs:
				boxes - a list of lists of bounding boxes. Each nested list is a bounding box in the form of [x1, y1, x2, y2] 
				where (x1, y1) and (x2, y2) are the top left and bottom right coordinate respectively. The order of bounding boxes in the list
				is from left to right in the image.
				
			Our solution uses xy-coordinate instead of rc-coordinate. More information: http://scikit-image.org/docs/dev/user_guide/numpy_images.html#coordinate-conventions
		'''
		# YOUR CODE HERE
		raise NotImplementedError
		return boxes


if __name__ == '__main__':
	folder = "ECE276A_HW1/trainset/"
	DM = DataLoader("ECE276A_HW1/trainset/",0.9,["barrel_blue","non_barrel_blue","rest"])#loads a data handling module to load data
	window_size = 200
	model = LogisticRegression(window_size,num_classes=3)
	model.load_model("trained_models/model2.pickle")
	my_detector = BarrelDetector()
	for filename in os.listdir(folder):
		# read one test image
		img = plt.imread(os.path.join(folder,filename))
		plt.imshow('image', img)
		

		#Display results:
		#(1) Segmented images
		#	 mask_img = my_detector.segment_image(img)
		#(2) Barrel bounding box
		#    boxes = my_detector.get_bounding_box(img)
		#The autograder checks your answers to the functions segment_image() and get_bounding_box()
		#Make sure your code runs as expected on the testset before submitting to Gradescope

