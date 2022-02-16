import faroCamera

def preview(camera):
    camera.preview(5)


def takePhoto(camera, location):
    camera.autoCapturePhoto(location)


if __name__=="__main__":
    camera = faroCamera.FaroCamera()
    preview(camera)
    takePhoto(camera, "/home/pi/camera/camera/photos/test.jpg")