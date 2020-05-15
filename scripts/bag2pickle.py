#!/usr/bin/python
# -*- coding: utf-8 -*-
import rospy
import rosbag
import pickle
import numpy as np
import sys
import sensor_msgs.point_cloud2 as pc2

def convertBag(fn, topic):
    out_fn = fn.replace('.bag', '.pickle')
    print('writing out to ' + out_fn)
    bag = rosbag.Bag(fn)

    pcs = []
    for topic, msg, time in bag.read_messages(topics=[topic]):
        data = np.asarray(list(pc2.read_points(msg, field_names=['x', 'y', 'z'], skip_nans=True)))
        pcs.append(data)
    
    with open(out_fn, 'wb') as out_f:
        pickle.dump(pcs, out_f)
    
    print('Done')

if __name__ == '__main__':
    rospy.init_node('bag2pickle', anonymous=True)

    myargv = rospy.myargv(argv=sys.argv)

    fn = myargv[2]
    topic = myargv[1]
    convertBag(fn = fn, topic = topic)