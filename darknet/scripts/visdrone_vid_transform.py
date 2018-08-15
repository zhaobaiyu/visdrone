import os
from pathlib import Path
from PIL import Image
import csv
import random
from collections import defaultdict


def convert(size, box):
    dw = 1. / size[0]
    dh = 1. / size[1]
    x = (box[0] + box[2] / 2) * dw
    y = (box[1] + box[3] / 2) * dh
    w = box[2] * dw
    h = box[3] * dh
    return (x, y, w, h)


def convert_annotation(seq):
    path = wd + '/annotations/' + seq + '.txt'
    tmp = defaultdict(str)
    with open(path, newline='') as csvfile:
        spamreader = csv.reader(csvfile)
        for row in spamreader:
            if row[6] == '0':
                continue
            bb = convert(seqs_size[seq], tuple(map(int, row[2:6])))
            tmp[row[0]] = tmp[row[0]] + row[7] + ' ' + ' '.join(str(a) for a in bb) + '\n'
    for img, value in tmp.items():
        with open(wd + '/labels/{}_{:0>7}.txt'.format(seq, int(img)), 'w') as outfile:
            outfile.write(value)
    return

            
wd = os.getcwd()
if not os.path.exists('images'):
    os.makedirs('images')
if not os.path.exists('labels'):
    os.makedirs('labels')

# below images not have labels in training set
os.chdir(wd + '/sequences/')
if not os.path.exists('uav0000281_00460_v/0000023.jpg'):
    os.remove(wd + '/images/uav0000281_00460_v/0000023.jpg')

if not os.path.exists('uav0000281_00460_v/0000024.jpg'):
    os.remove(wd + '/images/uav0000281_00460_v/0000024.jpg')

if not os.path.exists('uav0000281_00460_v/0000025.jpg'):
    os.remove(wd + '/images/uav0000281_00460_v/0000025.jpg')


    
train_file = wd + '/images.txt'
train_file_list = []
    
seqs_size = dict()

os.chdir('sequences')
seqs = os.listdir()
for seq in seqs:
    if seq[:3] != 'uav':
        continue
    os.chdir(seq)
    imgs = os.listdir()
    for img in imgs:
        if img[-3:] != 'jpg':
            continue
        dst = wd + '/images/{}_{:0>7}.jpg'.format(seq, int(img[:-4]))
        os.rename(img, dst)
        train_file_list.append(dst + '\n')
    os.chdir('..')
    os.rmdir(seq)
    with Image.open(wd + '/images/{}_0000001.jpg'.format(seq)) as Img:
        seqs_size[seq] = Img.size
    convert_annotation(seq)


random.shuffle(train_file_list)

train_file_str = ''

for i in train_file_list:
    train_file_str = train_file_str + i

with open(train_file, 'w') as outfile:
    outfile.write(train_file_str)
