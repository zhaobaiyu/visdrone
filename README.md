# VisDrone

Include PyTorch and Darknet implementation for [VisDrone](http://www.aiskyeye.com/) dataset.

```
git clone https://github.com/zhaobaiyu/visdrone.git <path-to-repository>
```

## doc

[yolo.md](https://github.com/zhaobaiyu/visdrone/blob/master/doc/yolo.md) 包含yolo的一些资料

[dataset.md](https://github.com/zhaobaiyu/visdrone/blob/master/doc/dataset.md) 关于pascal VOC、MS COCO以及VisDrone数据集的结构和格式

## darknet

[Yolo v3 with darknet](https://pjreddie.com/darknet/yolo/)

### install darknet framework

[Installing Darknet](https://pjreddie.com/darknet/install/)

```
git clone https://github.com/pjreddie/darknet.git <path-to-darknet>
cd <path-to-darknet>
wget https://pjreddie.com/media/files/yolov3.weights
wget https://pjreddie.com/media/files/yolov3-tiny.weights
# cuda or opencv option needs to modify Makefile, see the website above
make
```

### scripts for dataset transform

[visdrone\_vid\_transform.py](https://github.com/zhaobaiyu/visdrone/blob/master/darknet/scripts/visdrone_vid_transform.py) 对于VisDrone中的视频目标检测问题，该脚本将数据转换为Yolov3 Darknet实现所需格式，目录结构和Pascal VOC相似

[visdrone\_det\_transform.py](https://github.com/zhaobaiyu/visdrone/blob/master/darknet/scripts/visdrone_det_transform.py) 对于VisDrone中的图片目标检测问题，该脚本将数据转换为Yolov3 Darknet实现所需格式

run the command below twice, with respect to `VisDrone2018-VID-train` and `VisDrone2018-VID-val`

```
cd <path-to-dataset>
cp <path-to-repository>/darknet/scripts/visdrone_vid_transform.py .
python visdrone_vid_transform.py
```

### prepare config files

```
cd <path-to-darknet>
cp <path-to-repository>/darknet/cfg/visdrone.data cfg/
# visdrone_det.data for detection problem
cp <patn-to-repository>/darknet/cfg/yolov3-visdrone.cfg cfg/
cp <path-to-repository>/darknet/data/visdrone.names
```

modify`<path-to-darknet>/cfg/visdrone.data`：

```
classes= 10
train  = <path-to-visdrone-train-dataset>/images.txt
valid  = <path-to-visdrone-val-dataset>/images.txt
names = data/voc.names
backup = backup
```

### modify training hyperparameter

modify`<path-to-darknet>/cfg/yolov3-visdrone.cfg`

```
[net]
# Testing
# batch=1
# subdivisions=1
# Training
batch=64
subdivisions=8
....
```

### training

```
cd <path-to-darknet>
./darknet detector train cfg/visdrone.data cfg/yolov3-visdrone.cfg darknet53.conv.74
```

## PyTorch

PyTorch implementation from scratch

代码暂未写完。

