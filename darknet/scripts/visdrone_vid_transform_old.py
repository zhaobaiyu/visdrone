import os
from pathlib import Path
from PIL import Image
import csv
from collections import defaultdict


def convert(size, box):
    dw = 1. / size[0]
    dh = 1. / size[1]
    x = (box[0] + box[2] / 2) * dw
    y = (box[1] + box[3] / 2) * dh
    w = box[2] * dw
    h = box[3] * dh
    return (x, y, w, h)
            
wd = os.getcwd()

if not os.path.exists('labels'):
    os.makedirs('labels')

anns = os.listdir('annotations')

train_file = 'images.txt'
train_file_txt = ''

for ann in anns:
    if ann[:3] != 'uav':
        continue
    os.makedirs(wd + '/labels/' + ann[:-4])
    with Image.open(wd + '/sequences/' + ann[:-4] + '/0000001.jpg') as Img:
        img_size = Img.size
    tmp = defaultdict(str)
    with open(wd + '/annotations/' + ann, newline='') as csvfile:
        spamreader = csv.reader(csvfile)
        for row in spamreader:
            if row[6] == '0':
                continue
            bb = convert(img_size, tuple(map(int, row[2:6])))
            tmp[row[0]] = tmp[row[0]] + row[7] + ' ' + ' '.join(str(a) for a in bb) + '\n'
    for img, value in tmp.items():
        with open(wd + '/labels/' + ann[:-4] + '/{:0>7}.txt'.format(int(img)), 'w') as outfile:
            outfile.write(value)
        train_file_txt = train_file_txt + wd + '/sequences/' + ann[:-4] + '/{:0>7}.jpg'.format(int(img)) + '\n'
            
with open(train_file, 'w') as outfile:
    outfile.write(train_file_txt)
