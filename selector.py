#!/usr/bin/python
"""
View and select images to focus on
Copy images selected to different folder by press of button

used for visual selection of appropriate images
"""
import cv2
import glob
import shutil
import os

IMAGE_PATH = '/'
IMG_DIR = '1/'
TO_DIR = 'good/' #Create this folder in the icassava folder
CROP_DIR = 'bad/'
WRONG_CLASS_DIR = 'other/' #Create this folder in icassava folder

def move_file(filepath, from_dir=IMG_DIR, to_dir=TO_DIR):
	"""
	Move files from general directory to other specific class directory
	""" 
	filename = os.path.basename(filepath)
	frompath = os.path.join(IMAGE_PATH, from_dir)
	topath = os.path.join(IMAGE_PATH, to_dir)
	wrongclass = os.path.join(IMAGE_PATH, WRONG_CLASS_DIR)

	try:
		shutil.move(frompath + filename, topath + filename)
		print ("Moving {} to {}".format(filename, to_dir))
		
	except Exception as e:
		print ("Error - File {} {}".format(filename,e))

def mover():
	path_img = os.path.join(IMAGE_PATH,IMG_DIR)
	imagefiles = glob.glob(path_img + '*.jpg')
	# print(imagefiles)
	totalfiles = len(imagefiles)
	num_files = 0
	print ("Total files: ",totalfiles)
	print (path_img)
	print (len(imagefiles))
	print ("\nPress 'm' to move the image to the 'good' folder")
	print ("\nPress 'c' to move the image to the 'bad' folder")
	print ("\nPress 'p' to move the image to the 'other' folder")

	cv2.namedWindow('Displayed Image')

	for imgfile in imagefiles:
		img = cv2.imread(imgfile)
		cv2.imshow('Displayed Image', img)
		k = cv2.waitKey(0)
		if k == 27:
			cv2.destroyAllWindows()
		elif k == ord('m'):
			move_file(imgfile)
		elif k == ord('p'):
			move_file(imgfile, to_dir=WRONG_CLASS_DIR)
		elif k == ord('c'):
			move_file(imgfile, to_dir=CROP_DIR)
		elif k == ord('q'):
			cv2.destroyAllWindows()
		else:
			continue


