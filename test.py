import faroCamera

def preview(camera):
    camera.preview(5)


def takePhoto(camera, location):
    camera.autoCapturePhoto(location)

def takeVideo(camera, location, duration):
    camera.autoCaptureVideo(location, duration)


if __name__=="__main__":
    camera = faroCamera.FaroCamera()
    preview(camera)
    takePhoto(camera, "/home/pi/camera/camera/photos/test.jpg")
    takeVideo(camera, "/home/pi/camera/camera/videos/test.h264", 5)