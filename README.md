# PointCloudDeNoising
<img src="./doc/cyclist.gif" width="1000">
<img src="./doc/pedestrian.gif" width="1000">


|input|segmentation|output|
|--|--|--|
|![#9F1924](https://placehold.it/15/9F1924/000000?text=+) raw point-cloud |![#9E9E9E](https://placehold.it/15/9E9E9E/000000?text=+) valid/clear      ![#7300E6](https://placehold.it/15/7300E6/000000?text=+) fog  ![#009999](https://placehold.it/15/009999/000000?text=+) rain | ![#6EA046](https://placehold.it/15/6EA046/000000?text=+) de-noised|

Data will be available soon.

## Abstract
Lidar sensors are frequently used in environment perception for autonomous vehicles and mobile robotics to complement camera, radar, and ultrasonic sensors. Adverse weather conditions are significantly impacting the performance of lidar-based scene understanding by causing undesired measurement points that in turn effect missing detections and false positives. 
In heavy rain or dense fog, water drops could be misinterpreted as objects in front of the vehicle which brings a mobile robot to a full stop. 
In this paper, we present the first CNN-based approach to understand and filter out such adverse weather effects in point cloud data. Using a large data set obtained in controlled weather environments, we demonstrate a significant performance improvement of our method over state-of-the-art involving geometric filtering. 

## Getting Started

Clone the repository.
```
git clone https://github.com/rheinzler/PointCloudDeNoising.git
cd PointCloudDeNoising
```

## Reference
If you find our work on lidar point-cloud de-noising in adverse weather useful for your research, please consider citing our work.:
```
@inproceedings{PointCloudDeNoising2019,
  title     = {CNN-based Lidar Point Cloud De-Noising in Adverse Weather},
  author    = {Heinzler, Robin and Piewak, Florian and Schindler, Philipp and Stork, Wilhelm},
  booktitle = {},
  year      = {2019}
}
```

## Acknowledgements
This work has received funding from the European Union under the H2020 ECSEL Programme as part of the DENSE project, contract number 692449. We thank Velodyne Lidar, Inc. for permission to publish this dataset.  
