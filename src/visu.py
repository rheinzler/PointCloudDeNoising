#!/usr/bin/python3
PATH = '~/PointCloudDeNoising/test_01/2018-11-29_104141_Static2-FogB/'
COLOR_LABEL_MAPPING = {
    0: [0.0 ,0.0 ,0.0],
    100: [158, 158, 158],
    101: [0.0,153.0,153.0],
    102:  [115.0, 0.0, 230.0],
}
import numpy as np
import glob
import h5py
try:
    import rospy
    from sensor_msgs.msg import PointCloud2
    import sensor_msgs.point_cloud2 as pc2
    from sensor_msgs.msg import PointField
    from std_msgs.msg import Header
except ImportError:
    rospy = None

class RosPublisher:
    def __init__(self, name='ros_publisher', color_label_mapping=COLOR_LABEL_MAPPING):
        # init ros
        self.name = name
        self.cloud_topic_name = "pointcloud"
        rospy.init_node(self.name + self.cloud_topic_name)
        self.rostime = rospy.Time.now()
        self.ros_rate = rospy.Rate(100)

        self.ros_publisher = rospy.Publisher('RosPublisher/{}'.format(name),PointCloud2,queue_size=10)
        self.r = rospy.Rate(100)
        self.channels = ['labels_1', 'distance_m_1', 'intensity_1', 'sensorX_1', 'sensorY_1', 'sensorZ_1']

        self.color_label_mapping = color_label_mapping
        self.sensorX_1 = None
        self.sensorY_1 = None
        self.sensorZ_1 = None
        self.distance_m_1 = None
        self.intensity_1 = None
        self.labels_1 = None


    def get_rgb(self, labels):
        r = g = b = np.zeros_like(labels)
        for label_id, color in self.color_label_mapping.items():
            r = np.where(labels == label_id, color[0] / 255.0, r)
            g = np.where(labels == label_id, color[1] / 255.0, g)
            b = np.where(labels == label_id, color[2] / 255.0, b)
        return r,g,b


    def publish(self, rgb_labels=None):
        header = Header()
        header.stamp = rospy.Time.now()
        header.frame_id = 'base'

        # http://wiki.ros.org/rviz/DisplayTypes/PointCloud
        r, g, b = self.get_rgb(self.labels_1.flatten())
        fields = [
            PointField('x', 0, PointField.FLOAT32, 1),
            PointField('y', 4, PointField.FLOAT32, 1),
            PointField('z', 8, PointField.FLOAT32, 1),
            PointField('distance', 12, PointField.FLOAT32, 1),
            PointField('intensity', 16, PointField.FLOAT32, 1),
            PointField('r', 20, PointField.FLOAT32, 1),
            PointField('g', 24, PointField.FLOAT32, 1),
            PointField('b', 28, PointField.FLOAT32, 1)
        ]

        points = list(zip(
            self.sensorX_1.flatten(),
            self.sensorY_1.flatten(),
            self.sensorZ_1.flatten(),
            self.distance_m_1.flatten(),
            self.intensity_1.flatten(),
            r,g,b
            ))

        cloud = pc2.create_cloud(header, fields, points)
        self.ros_publisher.publish(cloud)


    def load_hdf5_file(self, filename):
        with h5py.File(filename, "r", driver='core') as hdf5:
            # for channel in self.channels:
            self.sensorX_1 = hdf5.get('sensorX_1')[()]
            self.sensorY_1 = hdf5.get('sensorY_1')[()]
            self.sensorZ_1 = hdf5.get('sensorZ_1')[()]
            self.distance_m_1 = hdf5.get('distance_m_1')[()]
            self.intensity_1 = hdf5.get('intensity_1')[()]
            self.labels_1 = hdf5.get('labels_1')[()]


def main(path=PATH):
    pub = RosPublisher()
    files = sorted(glob.glob(path + '*.hdf5'))
    for frame, file in enumerate(files):
        print('{:04d} / {}'.format(frame, file))
        pub.load_hdf5_file(file)
        pub.publish()
        if frame == 200:
            break

if __name__ == "__main__":
    main()
