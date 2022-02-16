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

    def autoCaptureVideo(self, videoLocation, videoDuration):
        self.camera.resolution = (1280, 720)
        self.camera.start_preview()
        self.camera.start_recording(videoLocation)
        sleep(videoDuration)
        self.camera.stop_recording()
        self.camera.stop_preview()

