import cv2
import numpy as np
import csv
from scipy.spatial import distance

def cal_sim(box1, box2):
    # the metric could be cosine, euclidean, mahalanobis, correlation, canberra
    #return distance.cosine(box1.flatten(), box2.flatten())
    return abs(np.sum(box1)-np.sum(box2))


def search_bbox(current_frame, future_frame, bbox):
    # n is related to the scaled search region
    n = 2
    # stride pixel of the sliding window
    stride = 5

    y, x = current_frame.shape[:2]
    upper, lower, left, right = bbox
    obj = current_frame[upper:lower, left:right]
    obj_h = lower - upper
    obj_w = right - left
    r_upper = max(upper - n * obj_h, 0)
    r_lower = min(lower + n * obj_h, y)
    r_left = max(left - n * obj_w, 0)
    r_right = min(right + n * obj_w, x)

    min_dist = 2 ** 32
    min_dist_bbox = bbox

    for s_upper in range(r_upper, r_lower - obj_h, stride):
        for s_left in range(r_left, r_right - obj_w, stride):
            dist = cal_sim(obj, future_frame[s_upper:s_upper+obj_h, s_left:s_left+obj_w])
            if dist < min_dist:
                min_dist = dist
                min_dist_bbox = (s_upper, s_upper+obj_h, s_left, s_left+obj_w)
    # print(min_dist)
    return min_dist_bbox


def search_frame(img_path, label_path, future_path):
    current_frame = cv2.imread(img_path)
    future_frame = cv2.imread(future_path)
    y, x = current_frame.shape[:2]
    targets = []
    original_targets = []

    flag = 0 ##############
    with open(label_path, newline='') as csvfile:
        spamreader = csv.reader(csvfile, delimiter=' ')
        for str_row in spamreader:
            flag += 1 ##############
            print(flag) ############
            row = [float(a) for a in str_row]
            obj_x, obj_y, obj_w, obj_h = [int(a) for a in [x*row[1], y*row[2], x*row[3], y*row[4]]]
            upper = obj_y - obj_h // 2
            lower = obj_y + obj_h // 2
            left = obj_x - obj_w // 2
            right = obj_x + obj_w // 2
            original_targets.append((upper, lower, left, right))
            targets.append(search_bbox(current_frame, future_frame, (upper, lower, left, right)))

    return targets, original_targets


def draw_targets(img, targets):
    for upper, lower, left, right in targets:
        cv2.rectangle(img, (left, upper), (right, lower), (0, 255, 0), 3)
    return img


if __name__ == '__main__':
    img_path = '/Users/baiyu/Temp/fs/uav0000124_00944_v_0000028.jpg'
    label_path = '/Users/baiyu/Temp/fs/uav0000124_00944_v_0000028.txt'
    future_path = '/Users/baiyu/Temp/fs/uav0000124_00944_v_0000033.jpg'
    img = cv2.imread(future_path)
    original_img = cv2.imread(img_path)
    targets, original_targets = search_frame(img_path, label_path, future_path)
    output = draw_targets(img, targets)
    original_output = draw_targets(original_img, original_targets)
    cv2.imwrite('/Users/baiyu/Temp/fs/new.png', output)
    cv2.imwrite('/Users/baiyu/Temp/fs/old.png', original_output)