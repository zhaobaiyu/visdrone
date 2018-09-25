cmd = './darknet detector test cfg/visdrone.data cfg/yolov3-visdrone.cfg backup/{}.weights val_samples/uav_{:0>2}{:0>2}.jpg\n'
mv_cmd = 'mv predictions.png val_samples/uav_{:0>2}{:0>2}_{}.png\n'

weights = ['0907', '0913_60k', '0913_90k', '0913_13xk', '0924_30k', '0924_3xk']
uav_n = list(range(1, 8))
img_n = list(range(1, 4))

ans_str = '#!/bin/bash\n\n'

for weight in weights:
    for i in uav_n:
        for j in img_n:
            ans_str += cmd.format(weight, i, j) + mv_cmd.format(i, j, weight)

with open('val_pred.sh', 'w') as outfile:
    outfile.write(ans_str)