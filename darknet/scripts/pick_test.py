import os
import random
from shutil import copyfile

os.chdir('/home/baiyu/Data/VisDrone/VisDrone2018-VID-val/images')

imgs = os.listdir()

imgs = random.sample(imgs, 10)

for i, img in enumerate(imgs, 1):
    copyfile(img, '/home/baiyu/Projects/src/darknet/test/{:0>2}.jpg'.format(i))

    
