import os
import sys
import random
from collections import defaultdict
from shutil import copyfile


def pick_val(valdata_dir, output_dir):
    img_dir = os.path.join(valdata_dir, 'images')
    label_dir = os.path.join(valdata_dir, 'labels')
    imgs = os.listdir(img_dir)
    imgs_in_uavs = defaultdict(list)
    for img in imgs:
        imgs_in_uavs[img[:18]].append(img[18:])
    for i, uav in enumerate(sorted(imgs_in_uavs), 1):
        imgs_in_uavs[uav].sort()
        len_uav = len(imgs_in_uavs[uav])
        indexes = [len_uav // 4, len_uav // 2, len_uav * 3 // 4]
        for j, index in enumerate(indexes, 1):
            img_src_path = os.path.join(img_dir, uav+imgs_in_uavs[uav][index])
            img_dst_path = os.path.join(output_dir, 'uav_{:0>2}{:0>2}.jpg'.format(i, j))
            label_src_path = os.path.join(label_dir, uav+imgs_in_uavs[uav][index][:-4]+'.txt')
            label_dst_path = os.path.join(output_dir, 'uav_{:0>2}{:0>2}.txt'.format(i, j))
            copyfile(img_src_path, img_dst_path)
            copyfile(label_src_path, label_dst_path)


if __name__ == "__main__":
    valdata_dir = sys.argv[1]
    output_dir = sys.argv[2]
    if not os.path.exists(output_dir):
        os.mkdir(output_dir)
    pick_val(valdata_dir, output_dir)
