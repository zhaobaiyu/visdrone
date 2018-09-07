import sys
import os
import csv
from PIL import Image, ImageDraw
from draw_box import draw_box



def crop_img(img_path, label_path):
    img_dir, img_name = os.path.split(img_path)
    label_dir, label_name = os.path.split(label_path)

    new_img_paths = []
    with Image.open(img_path) as im:
        im_size = im.size
        new_length = int(min(im_size)*0.8)
        crop_boxes = [(0, 0, new_length, new_length),
                    (im_size[0]-new_length, im_size[1]-new_length, im_size[0], im_size[1]),
                    (int((im_size[0]-new_length)/2), int((im_size[1]-new_length)/2), int((im_size[0]-new_length)/2)+new_length, int((im_size[1]-new_length)/2)+new_length)]

        labels = []
        with open(label_path, newline='') as csvfile:
            spamreader = csv.reader(csvfile, delimiter=' ')
            for row in spamreader:
                x = int(float(row[1])*im_size[0])
                y = int(float(row[2])*im_size[1])
                w = int(float(row[3])*im_size[0])
                h = int(float(row[4])*im_size[1])
                left = x - w // 2
                upper = y - h // 2
                right = x + w // 2
                lower = y + h // 2
                labels.append({'cla':row[0], 'left':left, 'upper':upper, 'right':right, 'lower':lower, 'x':x,'y':y, 'w':w, 'h':h})
                
        
        for i, box in enumerate(crop_boxes):
            new_img_path = os.path.join(img_dir, 'gen{:0>2}_'.format(i+1)+img_name)
            im.crop(box).save(new_img_path, 'JPEG')
            new_img_paths.append(new_img_path)
            ans = ''
            for label in labels:
                if label['left'] >= box[0] and label['upper'] >= box[1] and label['right'] <= box[2] and label['lower'] <= box[3]:
                    new_x = (label['x'] - box[0]) * 1.0 / new_length
                    new_y = (label['y'] - box[1]) * 1.0 / new_length
                    new_w = label['w'] * 1.0 / new_length
                    new_h = label['h'] * 1.0 / new_length
                    ans += ' '.join([label['cla'], str(new_x), str(new_y), str(new_w), str(new_h)]) + '\n'
            with open(os.path.join(label_dir, 'gen{:0>2}_'.format(i+1)+label_name), 'w') as outfile:
                outfile.write(ans)
                
    return new_img_paths




if __name__ == '__main__':
    crop_img(sys.argv[1], sys.argv[2])
    try:
        if sys.argv[3] == 'box':
            img_dir, img_name = os.path.split(sys.argv[1])
            label_dir, label_name = os.path.split(sys.argv[2])
            for i in range(3):
                draw_box(os.path.join(img_dir, 'gen{:0>2}_'.format(i+1)+img_name), os.path.join(label_dir, 'gen{:0>2}_'.format(i+1)+label_name))
    except:
        pass
