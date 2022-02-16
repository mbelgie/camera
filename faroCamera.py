from picamera import PiCamera
from time import sleep


class FaroCamera():
    def __init__(self):
        self.camera = PiCamera()

    def preview(self, time):
        self.camera.start_preview()
        sleep(time)
        self.camera.stop_preview()

    def autoCapturePhoto(self, imageLocation):
        self.camera.capture(imageLocation)

    
