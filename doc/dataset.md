# Directory Structure and Label Format of Dataset

## VisDrone

                                                           Number of snippets
     -------------------------------------------------------------------------------------------------
               Dataset                   Training              Validation            Test-Challenge
     -------------------------------------------------------------------------------------------------
      Object detection in videos         56 clips                7 clips               16 clips
                                       24,201 frames          2,819 frames           6,333 frames
     -------------------------------------------------------------------------------------------------

There is no overlap between the three sets.

### Directory Structure

Extracted from:

- VisDrone2018-VID-train.zip [BaiduYun](https://pan.baidu.com/s/1zVOPr8qcLxmulDSXFE_3QQ) [Google Drive](https://drive.google.com/open?id=12XN6DtLCpOWzxMqoUZjO1oyAaYSQLtFe) [Tencent Cloud](https://share.weiyun.com/5WWlnPy)
- VisDrone2018-VID-val.zip [BaiduYun](https://pan.baidu.com/s/1VAObTYDH1EDbDbmMajwnLg) [Google Drive](https://drive.google.com/open?id=1ELbS9q9qmP4sj5c6uKvATU3nIiUfJ8yc) [Tencent Cloud](https://share.weiyun.com/5H2ipAo)
- VisDrone2018-VID-test-challenge.zip [BaiduYun](https://pan.baidu.com/s/1J7oT-3jInUp4bkpYLtxBog) [Google Drive](https://drive.google.com/open?id=19IMfYZyJGLXqtLre3wg4FrciQSM7pXiG) [Tencent Cloud](https://share.weiyun.com/5Ue6JUa)


```
.
├── VisDrone2018-VID-train 
│   ├── sequences [56 entries]
│   │   ├── uav0000013_00000_v
│   │   │   ├── 0000001.jpg
│   │   │   └── ...
│   │   ├── uav0000013_01073_v
│   │   │   ├── 0000001.jpg
│   │   │   └── ...
│   │   └── ...
│   └── annotations [56 entries]
│       ├── uav0000013_00000_v.txt
│       ├── uav0000013_01073_v.txt
│       └── ...
├── VisDrone2018-VID-val
│   ├── sequences [7 entries]
│   │   ├── uav0000086_00000_v
│   │   │   ├── 0000001.jpg
│   │   │   └── ...
│   │   ├── uav0000117_02622_v
│   │   │   ├── 0000001.jpg
│   │   │   └── ...
│   │   └── ...
│   └── annotations [7 entries]
│       ├── uav0000086_00000_v.txt
│       ├── uav0000117_02622_v.txt
│       └── ...
└── VisDrone2018-VID-test-challenge
    └── sequences [16 entries]
        ├── uav0000006_06900_v
        │   ├── 0000001.jpg
        │   └── ...
        ├── uav0000074_10080_v
        │   ├── 0000001.jpg
        │   └── ...
        └── ...
```

### Label Format

Submission of the results will consist of TXT files with one line per predicted object.It looks as follows:

     <frame_index>,<target_id>,<bbox_left>,<bbox_top>,<bbox_width>,<bbox_height>,<score>,<object_category>,<truncation>,<occlusion>

            Name	                                                      Description
     ----------------------------------------------------------------------------------------------------------------------------------
        <frame_index>     The frame index of the video frame
	
	     <target_id>      In the DETECTION result file, the identity of the target should be set to the constant -1. 
                          In the GROUNDTRUTH file, the identity of the target is used to provide the temporal corresponding 
		              relation of the bounding boxes in different frames.

         <bbox_left>      The x coordinate of the top-left corner of the predicted bounding box

         <bbox_top>	      The y coordinate of the top-left corner of the predicted object bounding box

        <bbox_width>      The width in pixels of the predicted object bounding box
	
	    <bbox_height>     The height in pixels of the predicted object bounding box

          <score>	      The score in the DETECTION file indicates the confidence of the predicted bounding box enclosing 
                          an object instance.
                          The score in GROUNDTRUTH file is set to 1 or 0. 1 indicates the bounding box is considered in 
		              evaluation, while 0 indicates the bounding box will be ignored.

      <object_category>   The object category indicates the type of annotated object, (i.e., ignored regions (0), pedestrian (1), 
                          people (2), bicycle (3), car (4), van (5), truck (6), tricycle (7), awning-tricycle (8), bus (9), motor (10), 
		              others (11))
 
       <truncation>       The score in the DETECTION file should be set to the constant -1.
                          The score in the GROUNDTRUTH file indicates the degree of object parts appears outside a frame 
		              (i.e., no truncation = 0 (truncation ratio 0%), and partial truncation = 1 (truncation ratio 1% °´ 50%)).

        <occlusion>	      The score in the DETECTION file should be set to the constant -1.
                          The score in the GROUNDTRUTH file indicates the fraction of objects being occluded 
		              (i.e., no occlusion = 0 (occlusion ratio 0%), partial occlusion = 1 (occlusion ratio 1% °´ 50%), 
		              and heavy occlusion = 2 (occlusion ratio 50% ~ 100%)).
				 
The detections in the ignored regions and labeled as "others" will be not considered in the evaluation. The sample submission of the detector can be found in our website.

## Pascal VOC

### Directory Structure

##### Pascal VOC 2012

Extracted from [VOCtrainval_11-May-2012.tar](http://host.robots.ox.ac.uk/pascal/VOC/voc2012/VOCtrainval_11-May-2012.tar)

```
VOCdevkit
└── VOC2012
    ├── ImageSets
    │   ├── Action
    │   │   ├── jumping_train.txt
    │   │   ├── jumping_trainval.txt
    │   │   ├── jumping_val.txt
    │   │   ├── phoning_train.txt
    │   │   ├── phoning_trainval.txt
    │   │   ├── phoning_val.txt
    │   │   ├── playinginstrument_train.txt
    │   │   ├── playinginstrument_trainval.txt
    │   │   ├── playinginstrument_val.txt
    │   │   ├── reading_train.txt
    │   │   ├── reading_trainval.txt
    │   │   ├── reading_val.txt
    │   │   ├── ridingbike_train.txt
    │   │   ├── ridingbike_trainval.txt
    │   │   ├── ridingbike_val.txt
    │   │   ├── ridinghorse_train.txt
    │   │   ├── ridinghorse_trainval.txt
    │   │   ├── ridinghorse_val.txt
    │   │   ├── running_train.txt
    │   │   ├── running_trainval.txt
    │   │   ├── running_val.txt
    │   │   ├── takingphoto_train.txt
    │   │   ├── takingphoto_trainval.txt
    │   │   ├── takingphoto_val.txt
    │   │   ├── train.txt
    │   │   ├── trainval.txt
    │   │   ├── usingcomputer_train.txt
    │   │   ├── usingcomputer_trainval.txt
    │   │   ├── usingcomputer_val.txt
    │   │   ├── val.txt
    │   │   ├── walking_train.txt
    │   │   ├── walking_trainval.txt
    │   │   └── walking_val.txt
    │   ├── Layout
    │   │   ├── train.txt
    │   │   ├── trainval.txt
    │   │   └── val.txt
    │   ├── Main
    │   │   ├── aeroplane_train.txt
    │   │   ├── aeroplane_trainval.txt
    │   │   ├── aeroplane_val.txt
    │   │   ├── bicycle_train.txt
    │   │   ├── bicycle_trainval.txt
    │   │   ├── bicycle_val.txt
    │   │   ├── bird_train.txt
    │   │   ├── bird_trainval.txt
    │   │   ├── bird_val.txt
    │   │   ├── boat_train.txt
    │   │   ├── boat_trainval.txt
    │   │   ├── boat_val.txt
    │   │   ├── bottle_train.txt
    │   │   ├── bottle_trainval.txt
    │   │   ├── bottle_val.txt
    │   │   ├── bus_train.txt
    │   │   ├── bus_trainval.txt
    │   │   ├── bus_val.txt
    │   │   ├── car_train.txt
    │   │   ├── car_trainval.txt
    │   │   ├── car_val.txt
    │   │   ├── cat_train.txt
    │   │   ├── cat_trainval.txt
    │   │   ├── cat_val.txt
    │   │   ├── chair_train.txt
    │   │   ├── chair_trainval.txt
    │   │   ├── chair_val.txt
    │   │   ├── cow_train.txt
    │   │   ├── cow_trainval.txt
    │   │   ├── cow_val.txt
    │   │   ├── diningtable_train.txt
    │   │   ├── diningtable_trainval.txt
    │   │   ├── diningtable_val.txt
    │   │   ├── dog_train.txt
    │   │   ├── dog_trainval.txt
    │   │   ├── dog_val.txt
    │   │   ├── horse_train.txt
    │   │   ├── horse_trainval.txt
    │   │   ├── horse_val.txt
    │   │   ├── motorbike_train.txt
    │   │   ├── motorbike_trainval.txt
    │   │   ├── motorbike_val.txt
    │   │   ├── person_train.txt
    │   │   ├── person_trainval.txt
    │   │   ├── person_val.txt
    │   │   ├── pottedplant_train.txt
    │   │   ├── pottedplant_trainval.txt
    │   │   ├── pottedplant_val.txt
    │   │   ├── sheep_train.txt
    │   │   ├── sheep_trainval.txt
    │   │   ├── sheep_val.txt
    │   │   ├── sofa_train.txt
    │   │   ├── sofa_trainval.txt
    │   │   ├── sofa_val.txt
    │   │   ├── train_train.txt
    │   │   ├── train_trainval.txt
    │   │   ├── train.txt
    │   │   ├── train_val.txt
    │   │   ├── trainval.txt
    │   │   ├── tvmonitor_train.txt
    │   │   ├── tvmonitor_trainval.txt
    │   │   ├── tvmonitor_val.txt
    │   │   └── val.txt
    │   └── Segmentation
    │       ├── train.txt
    │       ├── trainval.txt
    │       └── val.txt
    ├── Annotations [17125 entries]
    │   ├── 2007_000027.xml
    │   └── ...
    ├── JPEGImages [17125 entries]
    │   ├── 2007_000027.jpg
    │   └── ...        
    ├── SegmentationClass [2913 entries]
    │   ├── 2007_000032.png
    │   └── ...    
    └── SegmentationObject [2913 entries]
        ├── 2007_000032.png
        └── ...    
```

##### Pascal VOC 2007

Extracted from [VOCtrainval_06-Nov-2007.tar](http://host.robots.ox.ac.uk/pascal/VOC/voc2007/VOCtrainval_06-Nov-2007.tar)

```
VOCdevkit
└── VOC2007
    ├── ImageSets
    │   ├── Layout
    │   │   ├── train.txt
    │   │   ├── trainval.txt
    │   │   └── val.txt
    │   ├── Main
    │   │   ├── aeroplane_train.txt
    │   │   ├── aeroplane_trainval.txt
    │   │   ├── aeroplane_val.txt
    │   │   ├── bicycle_train.txt
    │   │   ├── bicycle_trainval.txt
    │   │   ├── bicycle_val.txt
    │   │   ├── bird_train.txt
    │   │   ├── bird_trainval.txt
    │   │   ├── bird_val.txt
    │   │   ├── boat_train.txt
    │   │   ├── boat_trainval.txt
    │   │   ├── boat_val.txt
    │   │   ├── bottle_train.txt
    │   │   ├── bottle_trainval.txt
    │   │   ├── bottle_val.txt
    │   │   ├── bus_train.txt
    │   │   ├── bus_trainval.txt
    │   │   ├── bus_val.txt
    │   │   ├── car_train.txt
    │   │   ├── car_trainval.txt
    │   │   ├── car_val.txt
    │   │   ├── cat_train.txt
    │   │   ├── cat_trainval.txt
    │   │   ├── cat_val.txt
    │   │   ├── chair_train.txt
    │   │   ├── chair_trainval.txt
    │   │   ├── chair_val.txt
    │   │   ├── cow_train.txt
    │   │   ├── cow_trainval.txt
    │   │   ├── cow_val.txt
    │   │   ├── diningtable_train.txt
    │   │   ├── diningtable_trainval.txt
    │   │   ├── diningtable_val.txt
    │   │   ├── dog_train.txt
    │   │   ├── dog_trainval.txt
    │   │   ├── dog_val.txt
    │   │   ├── horse_train.txt
    │   │   ├── horse_trainval.txt
    │   │   ├── horse_val.txt
    │   │   ├── motorbike_train.txt
    │   │   ├── motorbike_trainval.txt
    │   │   ├── motorbike_val.txt
    │   │   ├── person_train.txt
    │   │   ├── person_trainval.txt
    │   │   ├── person_val.txt
    │   │   ├── pottedplant_train.txt
    │   │   ├── pottedplant_trainval.txt
    │   │   ├── pottedplant_val.txt
    │   │   ├── sheep_train.txt
    │   │   ├── sheep_trainval.txt
    │   │   ├── sheep_val.txt
    │   │   ├── sofa_train.txt
    │   │   ├── sofa_trainval.txt
    │   │   ├── sofa_val.txt
    │   │   ├── train_train.txt
    │   │   ├── train_trainval.txt
    │   │   ├── train.txt
    │   │   ├── train_val.txt
    │   │   ├── trainval.txt
    │   │   ├── tvmonitor_train.txt
    │   │   ├── tvmonitor_trainval.txt
    │   │   ├── tvmonitor_val.txt
    │   │   └── val.txt
    │   └── Segmentation
    │       ├── train.txt
    │       ├── trainval.txt
    │       └── val.txt
    ├── Annotations [5011 entries] 
    │   ├── 000005.xml
    │   └── ...    
    ├── JPEGImages [5011 entries]
    │   ├── 000005.jpg
    │   └── ...
    ├── SegmentationClass [422 entries]
    │   ├── 000032.png
    │   └── ...
    └── SegmentationObject [422 entries]
        ├── 000032.png
        └── ...

```

### Label Format


## MS COCO



## Yolo v3 with Darknet framework requires:



### Label Format

`<object-class> <x> <y> <width> <height>`


