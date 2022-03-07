from picamera import PiCamera
from time import sleep


class FaroCamera():
    def __init__(self):
        self.camera = PiCamera()

    def cameraSetup(self):
        pass

    def preview(self, time):
        self.camera.start_preview()
        sleep(time)
        self.camera.stop_preview()

    def autoCapturePhoto(self, imageLocation):
        #TODO add text annotation for timestamps
        #self.camera.annotate_text = timestamp
        # self.camera.capture(imageLocation, format='rgb', bayer=True)
        self.camera.capture(imageLocation)

    def autoCaptureVideo(self, videoLocation, videoDuration):
        self.camera.resolution = (1280, 720)
        self.camera.start_preview()
        self.camera.start_recording(videoLocation, format='h264', level='4.2')
        sleep(videoDuration)
        self.camera.stop_recording()
        self.camera.stop_preview()

