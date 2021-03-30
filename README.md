# [Point Cloud Denoising](https://arxiv.org/abs/1912.03874)
<img src="./doc/cyclist.gif" width="1000">
<img src="./doc/pedestrian.gif" width="1000">


|input|segmentation|output|
|--|--|--|
|![#9F1924](https://placehold.it/15/9F1924/000000?text=+) raw point-cloud |![#9E9E9E](https://placehold.it/15/9E9E9E/000000?text=+) valid/clear      ![#7300E6](https://placehold.it/15/7300E6/000000?text=+) fog  ![#009999](https://placehold.it/15/009999/000000?text=+) rain | ![#6EA046](https://placehold.it/15/6EA046/000000?text=+) de-noised|

## Abstract
Lidar sensors are frequently used in environment perception for autonomous vehicles and mobile robotics to complement camera, radar, and ultrasonic sensors. Adverse weather conditions are significantly impacting the performance of lidar-based scene understanding by causing undesired measurement points that in turn effect missing detections and false positives.
In heavy rain or dense fog, water drops could be misinterpreted as objects in front of the vehicle which brings a mobile robot to a full stop.
In this paper, we present the first CNN-based approach to understand and filter out such adverse weather effects in point cloud data. Using a large data set obtained in controlled weather environments, we demonstrate a significant performance improvement of our method over state-of-the-art involving geometric filtering.

## Download Dataset
Information: Click [here](https://www.uni-ulm.de/index.php?id=101568) for registration and download.

## Getting Started
We provide documented tools for visualization in *python* using ROS. 
Therefore, you need to install [ROS](http://wiki.ros.org/ROS/Installation) and the [rospy](http://wiki.ros.org/rospy) client API first.
* install rospy
 ```bash
 apt install python-rospy  
```
Then start "roscore" and "rviz" in separate terminals.

Afterwards, you can use the visualization tool:
* clone the repository:
```
cd ~/workspace
git clone https://github.com/rheinzler/PointCloudDeNoising.git
cd ~/workspace/PointCloudDeNoising
```
* create a virtual environment:
```bash
mkdir -p ~/workspace/PointCloudDeNoising/venv
virtualenv --no-site-packages -p python3 ~/workspace/PointCloudDeNoising/venv
```
* source virtual env and install dependencies:
```bash
source ~/workspace/PointCloudDeNoising/venv/bin/activate
pip install -r requirements.txt
```
* start visualization:
```bash
cd src
python visu.py
```

Notes: 
* We used the following label mapping for a single lidar point: 0: no label, 100: valid/clear, 101: rain, 102:
 fog
* Before executing the script you should change the input path


## Reference
If you find our work on lidar point-cloud de-noising in adverse weather useful for your research, please consider citing our work.:
```
@article{PointCloudDeNoising2020, 
  author   = {Heinzler, Robin and Piewak, Florian and Schindler, Philipp and Stork, Wilhelm},
  journal  = {IEEE Robotics and Automation Letters}, 
  title    = {CNN-based Lidar Point Cloud De-Noising in Adverse Weather}, 
  year     = {2020}, 
  keywords = {Semantic Scene Understanding;Visual Learning;Computer Vision for Transportation}, 
  doi      = {10.1109/LRA.2020.2972865}, 
  ISSN     = {2377-3774}
}
```

## Acknowledgements
This work has received funding from the European Union under the H2020 ECSEL Programme as part of the DENSE project, contract number 692449. We thank Velodyne Lidar, Inc. for permission to publish this dataset.

## Feedback/Questions/Error reporting
Feedback? Questions? Any problems or errors? Please do not hesitate to contact us!

