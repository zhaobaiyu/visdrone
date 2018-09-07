import os
import csv

with open('images.txt', newline='') as f:
    image_paths = [line.rstrip() for line in f]

image_paths.sort()
selected_image_paths = [image_paths[i] for i in range(0, len(image_paths), 5)]
images_dir = os.path.split(selected_image_paths[0])[0]
dataset_dir = os.path.split(images_dir)[0]
labels_dir = os.path.join(dataset_dir, 'labels')
selected_label_paths = [os.path.join(labels_dir, os.path.split(path)[1][:-4]+'.txt') for path in selected_image_paths]

os.makedirs('new_selected')
new_selected_dir = os.path.join(dataset_dir, 'new_selected')
new_images_dir = os.path.join(new_selected_dir, 'images')
os.makedirs(new_images_dir)
new_labels_dir = os.path.join(new_selected_dir, 'labels')
os.makedirs(new_labels_dir)

images_txt = ''
for path in selected_image_paths:
    os.rename(path, new_images_dir)
    images_txt += path + '\n'

for path in selected_label_paths:
    os.rename(path, new_labels_dir)

with open(os.path.join(new_selected_dir, 'images.txt'), 'w') as outfile:
    outfile.write(images_txt)
