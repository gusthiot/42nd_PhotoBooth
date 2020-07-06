from picamera import PiCamera, Color
from PIL import Image
import time


class Camera:
    
    def __init__(self, localDirectory, mainDirectory):
        self.camera = PiCamera()
        self.localDirectory = localDirectory
        
    def takePicture(self):
        ret = None
    
        self.camera.start_preview()
        # self.camera.annotate_background = Color('black')
        self.camera.annotate_foreground = Color('white')
        self.camera.annotate_text_size = 100
        self.camera.annotate_text = "\n\n 5 "
        time.sleep(1)
        self.camera.annotate_text = "\n\n 4 "
        time.sleep(1)
        self.camera.annotate_text = "\n\n 3 "
        time.sleep(1)
        self.camera.annotate_text = "\n\n 2 "
        time.sleep(1)
        self.camera.annotate_text = "\n\n 1 "
        time.sleep(1)
        self.camera.annotate_text = ""
        time.sleep(1)
        filename = time.strftime("%y%m%d_%H%M%S")
        self.camera.capture(self.localDirectory + filename + ".jpg")
        ret = filename
            
        self.camera.stop_preview()
        return ret
