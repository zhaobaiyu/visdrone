import sys
import csv
import os
from PIL import Image, ImageDraw

colors = [(25,202,173),
           (140,199,181),
           (160,238,225),
           (190,231,233),
           (190,237,199),
           (214,213,183),
           (209,186,116),
           (230,206,172),
           (236,173,158),
           (244,96,108)]


def draw_box(img_path, label_path, output_dir=None):
    img_dir, img_name = os.path.split(img_path)
    if output_dir is None:
        output_dir = img_dir
    
    with Image.open(img_path) as im:
        im_size = im.size
        draw = ImageDraw.Draw(im)
        with open(label_path, newline='') as csvfile:
            spamreader = csv.reader(csvfile, delimiter=' ')
            for str_row in spamreader:
                row = [float(a) for a in str_row]
                int_row = [int(a) for a in [row[1]*im_size[0], row[2]*im_size[1], row[3]*im_size[0], row[4]*im_size[1]]]
                box = [int_row[0]-int_row[2]//2, int_row[1]-int_row[3]//2, int_row[0]+int_row[2]//2, int_row[1]+int_row[3]//2]
                draw.rectangle(box, outline=colors[int(row[0])-1])
        im.save(os.path.join(output_dir, 'box_'+img_name), 'PNG')
    return


if __name__ == '__main__':
    draw_box(sys.argv[1], sys.argv[2])
