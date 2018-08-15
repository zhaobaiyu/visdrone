## Training logs

### 15th August 

dataset: DET

hyperparameter: `batch: 128, subdivisions=16, max_batches: 50200 (stop at )`

Platform: Google Cloud 8 cores, 18G RAM

GPU: [Tesla V100](https://www.nvidia.com/content/PDF/Volta-Datasheet.pdf)

max_batches: 50200 (stop at 1631)

![training815_1344](https://github.com/zhaobaiyu/visdrone/raw/master/doc/training815_1344.png)

```
Loaded: 0.000053 seconds
Region 82 Avg IOU: -nan, Class: -nan, Obj: -nan, No Obj: 0.000050, .5R: -nan, .75R: -nan,  count: 0
Region 94 Avg IOU: 0.844023, Class: 0.014283, Obj: 0.086379, No Obj: 0.000145, .5R: 1.000000, .75R: 1.000000,  count: 1
Region 106 Avg IOU: 0.367602, Class: 0.526159, Obj: 0.513706, No Obj: 0.003694, .5R: 0.351682, .75R: 0.149847,  count: 327
Region 82 Avg IOU: 0.785726, Class: 0.496921, Obj: 0.778427, No Obj: 0.000914, .5R: 1.000000, .75R: 1.000000,  count: 2
Region 94 Avg IOU: 0.783323, Class: 0.788832, Obj: 0.717260, No Obj: 0.002602, .5R: 0.970588, .75R: 0.676471,  count: 34
Region 106 Avg IOU: 0.441481, Class: 0.509718, Obj: 0.501781, No Obj: 0.003851, .5R: 0.488000, .75R: 0.140000,  count: 250
Region 82 Avg IOU: 0.772879, Class: 0.310951, Obj: 0.001525, No Obj: 0.000031, .5R: 1.000000, .75R: 1.000000,  count: 1
Region 94 Avg IOU: 0.720423, Class: 0.535640, Obj: 0.602876, No Obj: 0.000787, .5R: 1.000000, .75R: 0.375000,  count: 8
Region 106 Avg IOU: 0.371325, Class: 0.607665, Obj: 0.565498, No Obj: 0.003266, .5R: 0.350694, .75R: 0.079861,  count: 288
Region 82 Avg IOU: 0.733939, Class: 0.853631, Obj: 0.634386, No Obj: 0.000852, .5R: 1.000000, .75R: 0.666667,  count: 3
Region 94 Avg IOU: 0.726614, Class: 0.825041, Obj: 0.592278, No Obj: 0.001396, .5R: 1.000000, .75R: 0.391304,  count: 23
Region 106 Avg IOU: 0.415900, Class: 0.489407, Obj: 0.411726, No Obj: 0.003775, .5R: 0.454811, .75R: 0.113703,  count: 343
Region 82 Avg IOU: -nan, Class: -nan, Obj: -nan, No Obj: 0.000071, .5R: -nan, .75R: -nan,  count: 0
Region 94 Avg IOU: 0.770279, Class: 0.716002, Obj: 0.618706, No Obj: 0.001074, .5R: 0.933333, .75R: 0.733333,  count: 15
Region 106 Avg IOU: 0.300142, Class: 0.455310, Obj: 0.423971, No Obj: 0.003252, .5R: 0.249344, .75R: 0.057743,  count: 381
Region 82 Avg IOU: 0.619687, Class: 0.921845, Obj: 0.374956, No Obj: 0.000827, .5R: 0.800000, .75R: 0.200000,  count: 5
Region 94 Avg IOU: 0.770005, Class: 0.833168, Obj: 0.637376, No Obj: 0.001826, .5R: 1.000000, .75R: 0.592593,  count: 27
Region 106 Avg IOU: 0.399833, Class: 0.573185, Obj: 0.432783, No Obj: 0.003856, .5R: 0.412607, .75R: 0.103152,  count: 349
Region 82 Avg IOU: -nan, Class: -nan, Obj: -nan, No Obj: 0.000648, .5R: -nan, .75R: -nan,  count: 0
Region 94 Avg IOU: 0.792783, Class: 0.796404, Obj: 0.684222, No Obj: 0.002244, .5R: 1.000000, .75R: 0.777778,  count: 27
Region 106 Avg IOU: 0.476796, Class: 0.484587, Obj: 0.396566, No Obj: 0.004003, .5R: 0.522346, .75R: 0.103352,  count: 358
Region 82 Avg IOU: -nan, Class: -nan, Obj: -nan, No Obj: 0.000045, .5R: -nan, .75R: -nan,  count: 0
Region 94 Avg IOU: 0.828267, Class: 0.831971, Obj: 0.856413, No Obj: 0.001516, .5R: 1.000000, .75R: 0.875000,  count: 16
Region 106 Avg IOU: 0.335433, Class: 0.514497, Obj: 0.482110, No Obj: 0.003543, .5R: 0.269841, .75R: 0.060317,  count: 315
Region 82 Avg IOU: 0.714994, Class: 0.715303, Obj: 0.853698, No Obj: 0.001368, .5R: 1.000000, .75R: 0.600000,  count: 5
Region 94 Avg IOU: 0.749728, Class: 0.494899, Obj: 0.659732, No Obj: 0.002128, .5R: 1.000000, .75R: 0.357143,  count: 14
Region 106 Avg IOU: 0.476017, Class: 0.577869, Obj: 0.416908, No Obj: 0.005333, .5R: 0.496333, .75R: 0.151589,  count: 409
Region 82 Avg IOU: 0.725220, Class: 0.467108, Obj: 0.405009, No Obj: 0.000929, .5R: 1.000000, .75R: 0.000000,  count: 2
Region 94 Avg IOU: 0.722269, Class: 0.706821, Obj: 0.573186, No Obj: 0.003290, .5R: 0.944444, .75R: 0.425926,  count: 54
Region 106 Avg IOU: 0.463274, Class: 0.562589, Obj: 0.459744, No Obj: 0.003471, .5R: 0.533632, .75R: 0.156951,  count: 223
Region 82 Avg IOU: 0.790097, Class: 0.675557, Obj: 0.985818, No Obj: 0.000862, .5R: 1.000000, .75R: 0.500000,  count: 2
Region 94 Avg IOU: 0.814456, Class: 0.575814, Obj: 0.465654, No Obj: 0.000952, .5R: 1.000000, .75R: 0.750000,  count: 8
Region 106 Avg IOU: 0.536043, Class: 0.733527, Obj: 0.496984, No Obj: 0.003518, .5R: 0.578431, .75R: 0.220588,  count: 204
Region 82 Avg IOU: -nan, Class: -nan, Obj: -nan, No Obj: 0.000056, .5R: -nan, .75R: -nan,  count: 0
Region 94 Avg IOU: 0.769213, Class: 0.835515, Obj: 0.699275, No Obj: 0.000854, .5R: 1.000000, .75R: 0.555556,  count: 9
Region 106 Avg IOU: 0.297647, Class: 0.535943, Obj: 0.533517, No Obj: 0.003099, .5R: 0.266423, .75R: 0.080292,  count: 274
Region 82 Avg IOU: 0.615717, Class: 0.934618, Obj: 0.705310, No Obj: 0.000873, .5R: 0.750000, .75R: 0.250000,  count: 4
Region 94 Avg IOU: 0.699560, Class: 0.601584, Obj: 0.337529, No Obj: 0.000826, .5R: 0.933333, .75R: 0.533333,  count: 15
Region 106 Avg IOU: 0.312645, Class: 0.512447, Obj: 0.483945, No Obj: 0.003296, .5R: 0.253676, .75R: 0.014706,  count: 272
Region 82 Avg IOU: -nan, Class: -nan, Obj: -nan, No Obj: 0.000046, .5R: -nan, .75R: -nan,  count: 0
Region 94 Avg IOU: 0.779652, Class: 0.897829, Obj: 0.714492, No Obj: 0.001536, .5R: 0.950000, .75R: 0.650000,  count: 20
Region 106 Avg IOU: 0.305407, Class: 0.496608, Obj: 0.450375, No Obj: 0.003488, .5R: 0.273399, .75R: 0.064039,  count: 406
Region 82 Avg IOU: 0.563528, Class: 0.387302, Obj: 0.599856, No Obj: 0.000386, .5R: 1.000000, .75R: 0.000000,  count: 1
Region 94 Avg IOU: 0.706997, Class: 0.575183, Obj: 0.326585, No Obj: 0.000712, .5R: 0.894737, .75R: 0.526316,  count: 19
Region 106 Avg IOU: 0.413753, Class: 0.496865, Obj: 0.430849, No Obj: 0.003124, .5R: 0.365672, .75R: 0.085821,  count: 268
Region 82 Avg IOU: 0.556632, Class: 0.311474, Obj: 0.000051, No Obj: 0.000422, .5R: 0.500000, .75R: 0.000000,  count: 2
Region 94 Avg IOU: 0.775313, Class: 0.775805, Obj: 0.726921, No Obj: 0.002233, .5R: 1.000000, .75R: 0.607143,  count: 28
Region 106 Avg IOU: 0.472619, Class: 0.617118, Obj: 0.525364, No Obj: 0.003731, .5R: 0.510703, .75R: 0.174312,  count: 327
1631: 27.562284, 28.765835 avg, 0.001000 rate, 11.283772 seconds, 208768 images
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

