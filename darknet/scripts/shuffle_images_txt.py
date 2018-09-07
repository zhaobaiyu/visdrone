import random
import os

with open('images.txt', newline='') as f:
    image_paths = f.readlines()

random.shuffle(image_paths)
image_txt = ''

for path in image_paths:
    image_txt += path

with open('images.txt', 'w') as outfile:
    outfile.write(image_txt)
