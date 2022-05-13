import PIL
from PIL import Image
import os
import numpy



"""
																						Menor 256x256 > Delete Image
																					//
PERCORRER CADA PASTA DO DATASET > PERCORRER CADA FOTO > VERIFICAR TAMNAHO (256x256) 
 																					\\	
																						Maior 256x256 > Resize Image
"""

DATASET_DIR = "../Dataset"
TRAIN_FOLDER = "train"

train_directory = os.path.join(DATASET_DIR, TRAIN_FOLDER)

# SIZE WE WANT PICTURE TO BE 
IMAGE_DESIRED_SIZE = 256



def arrange_data():
	# Go through all Folders inside the train Folder
	for folder_name in os.listdir(train_directory):

		dataset_folder_directory = os.path.join(train_directory, folder_name)

		# Go through all Fotos inside each dataset folder
		for count, image_file_name in enumerate(os.listdir(dataset_folder_directory)):

			if image_file_name.endswith(".jpg") or filename.endswith(".png"):
				

				current_image_path = os.path.join(dataset_folder_directory, image_file_name)

				# Load Image
				current_img = PIL.Image.open(current_image_path)
				# fetching the dimensions
				width, height = current_img.size
				
				#Check Image Size
				
				if (width > IMAGE_DESIRED_SIZE and height > IMAGE_DESIRED_SIZE):
					resized_img = current_img.resize((IMAGE_DESIRED_SIZE,IMAGE_DESIRED_SIZE))

					img_format = image_file_name.split(".")[-1]
					new_name = folder_name + "_" + str(count) + f".{img_format}"
					print(new_name)
					resized_img.save(os.path.join(dataset_folder_directory,new_name))

					current_img.close()
					#Delete Image
					os.remove(current_image_path)

				else:
					current_img.close()
					#Delete Image
					os.remove(current_image_path)
			else:		
				os.remove(current_image_path)


arrange_data()
