## Training logs

### 1. 17th August 

dataset: VID

hyperparameter: `batch: 64, subdivisions=8, max_batches: 50200 (stop at )`

Platform: Google Cloud 8 cores, 18G RAM

GPU: [Tesla V100](https://www.nvidia.com/content/PDF/Volta-Datasheet.pdf)

![training815_1344](https://github.com/zhaobaiyu/visdrone/raw/master/doc/training815_1344.png)

```
```

##### 每个batch都会有这样一个输出：

```
1631: 27.562284, 28.765835 avg, 0.001000 rate, 11.283772 seconds, 208768 images
```

- 1631：第几组batch，设置总数50200，训练大约4个小时至1631组，暂时终止。
- 27.562284：总损失
- 28.765835 avg ： 平均损失
- 0.001000 rate：当前的学习率
- 11.283772 seconds： 当前batch训练所花的时间
- 208768 images ： 目前为止参与训练的图片总数 = 1631 * 128

##### 每一个batch包含128张图片，共分成16组，故每组8张图片。每个batch包含16*3条日志，每组包含3条信息，分别是：

``` 
Region 82 Avg IOU: 
Region 94 Avg IOU: 
Region 106 Avg IOU: 
```

三个尺度上预测不同大小的框：

- 82 为最大的预测尺度，使用较大的mask，但是可以预测出较小的物体
- 94 为中间的预测尺度，使用中等的mask
- 106 为最小的预测尺度，使用较小的mask，可以预测出较大的物体

```
Region 94 Avg IOU: 0.775313, Class: 0.775805, Obj: 0.726921, No Obj: 0.002233, .5R: 1.000000, .75R: 0.607143,  count: 28
```

- Region Avg IOU: 表示在当前subdivision内的图片的平均IOU，代表预测的矩形框和真实目标的交集与并集之比. 
- Class: 标注物体分类的正确率，期望该值趋近于1。 
- Obj: 越接近1越好。 
- No Obj: 期望该值越来越小，但不为零。 
- count: 所有的当前subdivision图片（本例中一共8张）中包含正样本的数量。

### 2. 16th August 09:49

Start time: 15th August 16:45

Training time: 17 hours

dataset: VID

hyperparameter: `batch: 64, subdivisions=8, max_batches: 50200 (stop at 13689)`

Platform: Google Cloud 8 cores, 18G RAM

GPU: [Tesla V100](https://www.nvidia.com/content/PDF/Volta-Datasheet.pdf)

![training816_0949](https://github.com/zhaobaiyu/visdrone/raw/master/doc/training816_0949.png)

训练17个小时，用val中数据测试，效果还是很差的，而且`car`都被错分为`van`

![](https://baiyu-public.oss-cn-beijing.aliyuncs.com/visdrone/01.png)

