# Python-Videocamera
###### This is a simplified way to use opencv with python 3

##
##### Raspberry pi
###### Opencv has issues with raspberry pi. It works up to the point where it saves the video. I tested all combos of fourcc and save format but nothing would save after recording.
###### Python has a module called picamera that should work better. I might add a picamera version at a later point.
##

#### Installing
```bash
pip3 install --upgrade pip

pip3 install opencv-python
pip3 install opencv-python-headless

# for raspberry pi trouble 
# when you see cv2 module not found try running this
sudo apt update
sudo apt install python3-opencv
```

#### Running
###### configuring main()
```python
def main():
    # check for cameras use print_working_cameras() method
    camera.print_working_cameras()
```
 ###### then you can use an index from this list as the webcam index in VideoCamera()
```python
def main():
    """
    VideoCamera(    webcam_index, 
                    file_extension, 
                    fourcc, 
                    playback_speed, 
                    seconds_of_recording)
    """
    camera = VideoCamera(1, 'mp4', 'mp4v', 10, 20)
    camera.record_loop()
```

```bash
# after configuring VideoCamera in main()
python3 video_camera.py
```

