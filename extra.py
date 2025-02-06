import os
from PIL import Image, ImageEnhance
import shutil
import random

def random_rotate(image):
    """
    Randomly rotate the given image.
    """
    ROTATIONS = [30, 45, 60, 120, 180, 270]
    
    degrees = random.choice(ROTATIONS)
    return image.rotate(degrees)

def random_hue(image):
    """
    Randomly change the hue of the given image.
    """
    enhancer = ImageEnhance.Color(image)
    factor = random.uniform(0.5, 1.5)  # Adjust this range as needed
    return enhancer.enhance(factor)




# list of extensions to process
EXTENSIONS = ['.jpg', '.png', '.bmp']

INPUT_DIR = './public/dataset/leg'
OUT_DIR = './public/out'

# recreate the output folder
if os.path.exists(OUT_DIR):
	shutil.rmtree(OUT_DIR)
os.mkdir(OUT_DIR)			

def process_image(filename):

    img = Image.open(filename)

    # apply rotation
    img = random_rotate(img)

    #apply hue
    img = random_hue(img)


    # save output image
    img.save(os.path.join(OUT_DIR, file))


# iterate all images in folder and process them
for files in os.walk(INPUT_DIR):
	for file in files[2]:
		if os.path.splitext(file)[1].lower() in EXTENSIONS:
			print(file)
			process_image(file)