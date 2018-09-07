import os
from crop_img import crop_img

images_path = os.path.join(os.getcwd(), 'images')
labels_path = os.path.join(os.getcwd(), 'labels')

images = os.listdir(images_path)

for image in images:
    new_img_paths = crop_img(os.path.join(images_path, image), os.path.join(labels_path, image[:-4]+'.txt'))
    with open(os.path.join(os.getcwd(), 'images.txt'), 'a') as outfile:
        for path in new_img_paths:
            outfile.write(path + '\n')
