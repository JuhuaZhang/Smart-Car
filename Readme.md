#### 2021 全国大学生智能车竞赛 迅飞创意组

##### 0. Environment

ubuntu 18.04, ROS melodic 
aruco.py is uesd for recognize ArUco code, myData is a folder used for training yolov3-tiny neural network 

##### 1. Open Camera

`sudo apt-get install ros-melodic-usb-cam` 

`roslaunch usb_cam usb_cam-test.launch`

##### 2. Recognize Aruco

use OpenCV 3.2.0

```bash
cd ~/
mkdir -p catkin_ws/src
cd catkin_ws/
catkin_make
cd src/
catkin_create_pkg aruco rospy std_msgs sensor_msgs
cd aruco/
mkdir scripts
cd scripts/
touch aruco.py
chmod +x aruco.py 
gedit aruco.py 
cd ~/catkin_ws/
catkin_make
source devel/setup.bash
rosrun aruco aruco.py 
```

##### 3. Recognize Facial Appearance

use [darknet](https://pjreddie.com/darknet/) and [darknet_ros](https://github.com/leggedrobotics/darknet_ros) 

Procedure

```flow
step0=>operation: Install darknet
step1=>operation: Collect data set
step2=>operation: Lable image in voc format
step3=>operation: Change voc to yolo
step4=>operation: Change .data & .cfg
step5=>operation: Put things correctly & train

step0->step1->step2->step3->step4->step5
```

**Collect** own data set:  use *capture.py*

**Lable** image: use [labelImg](https://github.com/tzutalin/labelImg) to lable pictures into voc format: 

	img_voc
		├───Annotations
		├───ImageSets
		│   └───Main
		└───JPEGImages

**Change** voc to yolo: use *create.py* and *trans.py*

```
myData
│   myData.names
│   myData_test.txt
│   myData_train.txt
│   trans.py
├───cfg
│       my_data.data
│       my_yolov3-tiny.cfg
├───img_voc
│   │   classes.txt
│   │   create.py
│   ├───Annotations
│   │       000000.xml
│   │       000001.xml
│   ├───ImageSets
│   │   └───Main
│   │           test.txt
│   │           train.txt
│   │           trainval.txt
│   │           val.txt
│   ├───JPEGImages
│   │       000000.jpg
│   │       000001.jpg
│   └───labels
│           000000.txt
│           000001.txt
├───labels
│       000000.txt
│       000001.txt
└───weights
```

**Change** .data & .cfg: in .cfg $ filters = 3 \times (classes + 5)$

**Train** : `./darknet detector train myData/cfg/my_data.data myData/cfg/my_yolov3-tiny.cfg darknet53.conv.74`

**After Training (obj --> 1, No obj --> 0)**

**darknet_ros**:  modify *.launch* & *.yaml*, add our own *.cfg* & *.weights* to file

`roslaunch darknet_ros darknet_ros.launch`

---

**Appendix**

when install ros and goto the command `rosdep update`

[Solution](https://blog.csdn.net/leida_wt/article/details/115120940) : add `https://ghproxy.com/`

```bash
sudo gedit /usr/lib/python2.7/dist-packages/rosdep2/sources_list.py
sudo gedit /usr/lib/python2.7/dist-packages/rosdistro/__init__.py
sudo gedit /usr/lib/python2.7/dist-packages/rosdep2/gbpdistro_support.py
sudo gedit /usr/lib/python2.7/dist-packages/rosdep2/sources_list.py
sudo gedit /usr/lib/python2.7/dist-packages/rosdep2/rep3.py
sudo gedit /usr/lib/python2.7/dist-packages/rosdistro/manifest_provider/github.py
```



**Reference**

[darknet-yolov3训练自己的数据集（超详细） - AnswerThe - 博客园 (cnblogs.com)](https://www.cnblogs.com/answerThe/p/11481564.html)

[解决ROS系统 rosdep update超时问题的新方法_leida_wt的博客-CSDN博客_rosdep update 超时](https://blog.csdn.net/leida_wt/article/details/115120940)

