from picamera import PiCamera
import time
import sys


class Camera:
    
    def __init__(self, localDirectory):
        self.camera = PiCamera()
        self.localDirectory = localDirectory
        
        
    def takePicture(self):
        ret = None
        try:
            self.camera.start_preview()
            time.sleep(5)
            filename = time.strftime("%y%m%d_%H%M%S")
            self.camera.capture(self.localDirectory + filename + ".jpg")
            ret = filename
        except:
            sys.exit()
        finally:
            self.camera.stop_preview()
            return ret
