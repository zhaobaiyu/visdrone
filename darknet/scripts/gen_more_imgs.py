import os
from crop_img import crop_img

images_path = os.path.join(os.getcwd(), 'images')
labels_path = os.path.join(os.getcwd(), 'labels')

images = os.listdir(images_path)
output_txt = ''

for image in images:
    new_img_paths = crop_img(os.path.join(images_path, image), os.path.join(labels_path, image[:-4]+'.txt'))
    for path in new_img_paths:
        output_txt += path + '\n'

with open(os.path.join(os.getcwd(), 'images.txt'), 'a') as outfile:
    outfile.write(output_txt)
