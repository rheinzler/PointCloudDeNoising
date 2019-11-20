# PointCloudDeNoisingBenchmark

<img src="./doc/cyclist.gif" width="1000">
## Color Coding

|input|segmentation|output|
|--|--|--|
|![#9F1924](https://placehold.it/15/9F1924/000000?text=+) raw point-cloud |![#9E9E9E](https://placehold.it/15/9E9E9E/000000?text=+) valid/clear |![#6EA046](https://placehold.it/15/6EA046/000000?text=+) de-noised| 
|| ![#7300E6](https://placehold.it/15/7300E6/000000?text=+)  fog | 
|| ![#009999](https://placehold.it/15/009999/000000?text=+) rain | 

Data will be available soon.

## Abstract
Lidar sensors are frequently used in environment perception for autonomous vehicles and mobile robotics to complement camera, radar, and ultrasonic sensors. Adverse weather conditions are significantly impacting the performance of lidar-based scene understanding by causing undesired measurement points that in turn effect missing detections and false positives. 
In heavy rain or dense fog, water drops could be misinterpreted as objects in front of the vehicle which brings a mobile robot to a full stop. 
In this paper, we present the first CNN-based approach to understand and filter out such adverse weather effects in point cloud data. Using a large data set obtained in controlled weather environments, we demonstrate a significant performance improvement of our method over state-of-the-art involving geometric filtering. 

## Getting Started

Clone the benchmark repository.
```
git clone https://github.com/rheinzler/PointCloudDeNoisingBenchmark.git
cd PointCloudDeNoisingBenchmark
```
Download the benchmark data





## Reference
If you find our work on benchmarking lidar point-cloud de-noising useful in your research, please consider citing our paper:


## Acknowledgements
This work has received funding from the European Union under the H2020 ECSEL Programme as part of the DENSE project, contract number 692449.
