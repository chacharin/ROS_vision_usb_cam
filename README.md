# ROS_vision_usb_cam
Workshop in RoboCup@HOME-Week3

ROS install camera $ sudo apt install ros-melodic-usb-cam 
Bring up USB CAM  $ roslaunch usb_cam usb_cam-test.launch
defult--Display RGB USB CAM $ rosrun image_view image_view image:=/usb_cam/image_raw
* Image topic = "/camera_top/rgb/image_raw"


