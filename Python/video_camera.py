# class that handles all the camera functions in a simple way
# fixed with big sur (mac) need to run "pip3 install opencv-python-headless"
import cv2
from datetime import datetime


class VideoCamera:
    # save (*'mp4') fourcc(*'mp4v') these settings work with mac
    # playback speed 10 is normal. lower makes slow mo. fast makes time lapse.
    def __init__(self, camera_port=0, save_format='mp4', fourcc_format='mp4v', playback_speed=10, clip_length_seconds=10):
        """Default constructor for VideoCamera"""
        self.camera_port = camera_port
        self.save_format = save_format
        self.fourcc_format = fourcc_format
        self.playback_speed = playback_speed
        self.clip_length_seconds = (clip_length_seconds * 10)


    def check_for_cameras(self):
        """Returns a list of possible working cameras at their index. For using cv2.VideoCapture(index)"""
        index = 0
        working_cameras_array = []
        max_index_to_search = 4

        while max_index_to_search > 0:
            cap = cv2.VideoCapture(index)
            if cap.read()[0]:
                working_cameras_array.append(index)
                cap.release()
            index += 1
            max_index_to_search -= 1

        return working_cameras_array
    
    def print_working_cameras(self):
        """Prints the array of working cameras found in check_for_cameras() method"""
        cams = self.check_for_cameras()
        print(cams)
    
    def build_time_string(self):
        """Uses datetime to build a string with year, month, day and time. Then that string is used to name the file so all files have a unique name. """
        now = datetime.now()
        # year = now.year
        # month = now.month
        # day = now.day
        weekday = now.strftime("%A")
        timenow = now.strftime("%H-%M-%S") # Hour-Minute-Second
        timestring = f'{weekday}_{timenow}'
        # timestring = f'{year}m{month}d{day}_{timenow}'

        return timestring

    def record_clip(self):
        """Records a video clip. Returns a boolean (if you want to run in a loop).
        Uses time string as name of video.
        Uses seconds to control how long clip is.
        Returns false when esc key is pressed (you need to click on the preview video window before hitting esc, doesn't work headless).
        Headless from terminal ctrl+c will stop program in the middle of the current clip."""
        # flag to keep recording or stop with esc key
        end_clip_flag = False
        # camera properties
        cap = cv2.VideoCapture(self.camera_port)
        width= int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
        height= int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))

        # save parameters
        file_name = f'./{self.build_time_string()}.{self.save_format}'
        fourcc = cv2.VideoWriter_fourcc(*self.fourcc_format)
        playback = self.playback_speed
        # writer.write(frame) saves the collection of frames with the specs written here
        writer = cv2.VideoWriter(file_name, fourcc, playback, (width,height))
        #VideoWriter (const String &filename, int fourcc, double fps, Size frameSize, bool isColor=true)

        # length of time each clip records before saving and starting a new one
        seconds_count = 0

        while seconds_count < self.clip_length_seconds:
            # start record
            ret,frame = cap.read()
            # show window 
            cv2.imshow('Video Sample', frame)
            # save clip
            writer.write(frame)
            
            seconds_count += 1
            # 27 escape key
            if cv2.waitKey(1) & 0xFF == 27:
                # ended return true to stop main loop and quit recording
                end_clip_flag = True
                break

        # Not 100% sure about how these work
        # clears current collection of frames i think
        cap.release()
        # releases the current writer i think
        writer.release()
        # cleans up all open windows i think
        cv2.destroyAllWindows()
        
        return end_clip_flag

    def record_loop(self):
        """Uses record_clip() to record in a continuous loop and saves each clip as a length of self.clip_length_seconds."""
        while True:
            ended = self.record_clip()

            if ended:
                print("Finished Recording")
                break


def main():
    """Main method for video_camera.py"""
    camera = VideoCamera(1, 'mp4', 'mp4v', 10, 20)
    # to check for cameras use print_working_cameras() method
    # camera.print_working_cameras()
    camera.record_loop()
   


if __name__ == '__main__':
    main()