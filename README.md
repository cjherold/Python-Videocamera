# Python-Videocamera
###### This is a simplified way to use opencv with python 3

##
##### Raspberry pi
###### Opencv has issues with raspberry pi. It works up to the point where it saves the video. I tested all combos of fourcc and save format but nothing would save after recording.
###### Python has a module called picamera that should work better. I might add a picamera version at a later point.
##

##### Installing
```bash
pip3 install --upgrade pip

pip3 install opencv-python
pip3 install opencv-python-headless

# for raspberry pi trouble 
# when you see cv2 module not found try running this
sudo apt update
sudo apt install python3-opencv
```

##### Running
```bash
# after configuring VideoCamera in main()
python3 video_camera.py
```

