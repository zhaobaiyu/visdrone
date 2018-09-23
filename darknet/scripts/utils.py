import sys
import os
import shutil
import csv
import random
import cv2 as cv
from draw_box import draw_box


def crop_and_gen(img_id, source_path, dst_path):
    img_path = os.path.join(source_path, 'images', img_id+'.jpg')
    label_path = os.path.join(source_path, 'labels', img_id+'.txt')

    if not os.path.exists(os.path.join(dst_path, 'images')):
        os.makedirs(os.path.join(dst_path, 'images'))

    if not os.path.exists(os.path.join(dst_path, 'labels')):
        os.makedirs(os.path.join(dst_path, 'labels'))

    img = cv.imread(img_path)
    new_img_h = img.shape[0] // 2
    new_img_w = img.shape[1] // 2

    upper_y = [0, img.shape[0] // 4, img.shape[0] // 2]
    left_x = [0, img.shape[1] // 4, img.shape[1] // 2]
    gen_bbox = lambda y, x: (y, x, y+new_img_h, x+new_img_w)
    bboxes = [gen_bbox(y, x) for y in upper_y for x in left_x]
    crop_img = lambda y1, x1, y2, x2: img[y1:y2, x1:x2]
    img_paths, label_paths = [], []

    # generate small scale
    res_img = cv.resize(img, (img.shape[1]//2, img.shape[0]//2))
    res_img_id = 'gen{:0>2}_{}'.format(0, img_id)
    res_img_path = os.path.join(dst_path, 'images', res_img_id+'.jpg')
    res_label_path = os.path.join(dst_path, 'labels', res_img_id+'.txt')
    img_paths.append(res_img_path)
    label_paths.append(res_label_path)
    cv.imwrite(res_img_path, res_img)
    shutil.copy(label_path, res_label_path)

    labels = list()
    with open(label_path, newline='') as csvfile:
        spamreader = csv.reader(csvfile, delimiter=' ')
        for row in spamreader:
            x = int(float(row[1])*img.shape[1])
            y = int(float(row[2])*img.shape[0])
            old_w = float(row[3])
            old_h = float(row[4])
            w = int(old_w * img.shape[1])
            h = int(old_h * img.shape[0])
            left = x - w // 2
            upper = y - h // 2
            right = x + w // 2
            lower = y + h // 2
            labels.append({'cla': row[0], 'left': left, 'upper': upper, 'right': right, 'lower': lower,
                           'x': x, 'y': y, 'old_w': old_w, 'old_h': old_h})

    for i, bbox in enumerate(bboxes, 1):
        new_img_id = 'gen{:0>2}_{}'.format(i, img_id)
        new_img = crop_img(*bbox)
        img_path = os.path.join(dst_path, 'images', new_img_id+'.jpg')
        label_path = os.path.join(dst_path, 'labels', new_img_id+'.txt')
        img_paths.append(img_path)
        label_paths.append(label_path)
        cv.imwrite(img_path, new_img)
        label_str = ''
        for label in labels:
            if label['left'] >= bbox[1] and label['right'] <= bbox[3] and label['upper'] >= bbox[0] and label['lower'] <= bbox[2]:
                new_x = (label['x'] - bbox[1]) * 1.0 / new_img_w
                new_y = (label['y'] - bbox[0]) * 1.0 / new_img_h
                new_w = label['old_w'] * 2
                new_h = label['old_h'] * 2
                label_str += ' '.join([label['cla'], str(new_x), str(new_y), str(new_w), str(new_h)]) + '\n'
        with open(label_path, 'w') as outfile:
            outfile.write(label_str)

    return img_paths, label_paths


def gen_more_imgs(src_dir, dst_dir):

    img_ids = list(map(lambda x: x[:-4], os.listdir(os.path.join(src_dir, 'images'))))
    for img_id in img_ids:
        crop_and_gen(img_id, src_dir, dst_dir)


def gen_images_txt(dst_dir):
    images_txt_path = os.path.join(dst_dir, 'images.txt')
    images_dir = os.path.join(dst_dir, 'images')
    labels_dir = os.path.join(dst_dir, 'labels')
    images_id = sorted(list(map(lambda x: x[:-4], os.listdir(images_dir))))
    labels_id = sorted(list(map(lambda x: x[:-4], os.listdir(labels_dir))))
    assert images_id == labels_id
    image_paths = [os.path.join(images_dir, image_id+'.jpg') for image_id in images_id]
    for _ in range(5):
        random.shuffle(image_paths)
    txt_str = '\n'.join(image_paths)
    txt_str += '\n'
    with open(images_txt_path, 'w') as outfile:
        outfile.write(txt_str)


def gap_select(src_dir, dst_dir):
    image_files = sorted(os.listdir(os.path.join(src_dir, 'images')))
    selected_image_id = [image_files[i][:-4] for i in range(0, len(image_files), 5)]

    if not os.path.exists(os.path.join(dst_dir, 'images')):
        os.makedirs(os.path.join(dst_dir, 'images'))
    if not os.path.exists(os.path.join(dst_dir, 'labels')):
        os.makedirs(os.path.join(dst_dir, 'labels'))

    for image_id in selected_image_id:
        os.rename(os.path.join(src_dir, 'images', image_id+'.jpg'), os.path.join(dst_dir, 'images', image_id+'.jpg'))
        os.rename(os.path.join(src_dir, 'labels', image_id+'.txt'), os.path.join(dst_dir, 'labels', image_id+'.txt'))
