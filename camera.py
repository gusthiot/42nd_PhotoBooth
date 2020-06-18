from picamera import PiCamera
from PIL import Image
import time


class Camera:
    
    def __init__(self, localDirectory, mainDirectory):
        self.camera = PiCamera()
        self.localDirectory = localDirectory
        self.numbersDirectory = mainDirectory + "numbers/"
        
        
    def takePicture(self):
        ret = None
    
        self.camera.start_preview()
        #num = 5
        #while num>=0:
        #img = Image.open(self.numbersDirectory + str(num) + ".jpeg")
        #pad = Image.new('RGB', (
        #        ((img.size[0] + 31) // 32) * 32,
        #        ((img.size[1] + 15) // 16) * 16,
        #    ))
        #pad.paste(img, (0, 0))
        #o = self.camera.add_overlay(pad.tobytes(), size=img.size)
        #self.camera.annotate_size = 120
        self.camera.annotate_text = " 5 "
        time.sleep(1)
        self.camera.annotate_text = " 4 "
        time.sleep(1)
        self.camera.annotate_text = " 3 "
        time.sleep(1)
        self.camera.annotate_text = " 2 "
        time.sleep(1)
        self.camera.annotate_text = " 1 "
        time.sleep(1)
        self.camera.annotate_text = "  "
        time.sleep(1)
        #    num -= 1
        filename = time.strftime("%y%m%d_%H%M%S")
        self.camera.capture(self.localDirectory + filename + ".jpg")
        ret = filename
            
        self.camera.stop_preview()
        return ret
