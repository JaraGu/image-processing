import os
import sys

from PIL import Image 

# grab first and second argument
IMAGE_FOLDER = sys.argv[1]
OUTPUT_FOLDER = sys.argv[2]

print(IMAGE_FOLDER,OUTPUT_FOLDER)
# check if new exists, if not create it
if not os.path.exists(OUTPUT_FOLDER):
    os.makedirs(OUTPUT_FOLDER)

for filename in os.listdir(IMAGE_FOLDER):
    img=Image.open(f'{IMAGE_FOLDER}{filename}')
    clean_name=os.path.splitext(filename)[0]
    img.save(f'{OUTPUT_FOLDER}{clean_name}.png','png')
    print('all done !!!')

# loop throught the image folder
# covert images to png
# save to the new folder
