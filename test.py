import faroCamera
from picamera import PiCamera
import numpy as np
import time

def preview(camera):
    camera.preview(5)


def takePhoto(camera, location):
    camera.autoCapturePhoto(location)

def takeVideo(camera, location, duration):
    camera.autoCaptureVideo(location, duration)

def analyzePhoto():
    camera = PiCamera()
    h = 640 # change this to anything < 2592 (anything over 2000 will likely get a memory error when plotting
    cam_res = (int(h),int(0.75*h)) # keeping the natural 3/4 resolution of the camera
    cam_res = (int(16*np.floor(cam_res[1]/16)),int(32*np.floor(cam_res[0]/32)))
    
    camera.resolution = (cam_res[1],cam_res[0])
    # camera.framerate = 30
    time.sleep(2) #let the camera settle
    # camera.iso = 100
    # camera.shutter_speed = camera.exposure_speed
    # camera.exposure_mode = 'off'
    # gain_set = camera.awb_gains
    # camera.awb_mode = 'off'
    # camera.awb_gains = gain_set
    
    camData = np.empty((cam_res[0],cam_res[1],3),dtype=np.uint8)
    noise = np.empty((cam_res[0],cam_res[1],3),dtype=np.uint8)

    x,y = np.meshgrid(np.arange(np.shape(camData)[1]),np.arange(0,np.shape(camData)[0]))
    rgb_text = ['Red','Green','Blue'] # array for naming color
    # input("press enter to capture background noise (remove colors)")
    camera.capture(noise,'rgb')
    noise = noise-np.mean(noise) # background 'noise'

    camera.capture(camData,'rgb')

    mean_array,std_array = [],[]
    for ii in range(0,3):
        # calculate mean and STDev and print out for each color
        mean_array.append(np.mean(camData[:,:,ii]-np.mean(camData)-np.mean(noise[:,:,ii])))
        std_array.append(np.std(camData[:,:,ii]-np.mean(camData)-np.mean(noise[:,:,ii])))
        # print('-------------------------')
        # print(rgb_text[ii]+'---mean: {0:2.1f}, stdev: {1:2.1f}'.format(mean_array[ii],std_array[ii]))

    print('The Object is: {}'.format(rgb_text[np.argmax(mean_array)]))
    # camera.autoCapturePhoto(camData)


if __name__=="__main__":
    camera = faroCamera.FaroCamera()
    # preview(camera)
    takePhoto(camera, "/home/pi/camera/camera/photos/test.jpg")
    analyzePhoto()
    # takeVideo(camera, "/home/pi/camera/camera/videos/test.h264", 5)