This package extracts the point cloud data from your rosbag file into a python pickle file
To use the package, clone this repo into source  
run ```catkin_make``` and ```source devel/setup.bash``` and ```roscore```  
then run ```rosrun PCBag2pickle bag2pickle.py <your pointcloud topic> <the absolute path to your bag file>```