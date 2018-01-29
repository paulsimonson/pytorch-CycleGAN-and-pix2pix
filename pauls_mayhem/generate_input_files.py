import numpy as np

import skimage.io as sio
import os

def ensure_dir(file_path):
    directory = os.path.dirname(file_path)
    if not os.path.exists(directory):
        os.makedirs(directory)

def write_subimage(file_path, image, x = 0, y = 0, subimage_size = 256):
    ensure_dir(file_path)
    subimage = image[x:x+subimage_size:1, y:y+subimage_size:1, 0::1]
    sio.imsave(file_path, subimage)

       
fnameA = "../../RawData/DogBox/DogBox.tif"
imageA = sio.imread(fnameA)

fnameB = "../../RawData/DogBox/DogBoxEdges.tif"
imageB = sio.imread(fnameB)

subimage_size = 256

height = imageA.shape[0]
width = imageA.shape[1]
print("imageA ndim: ", imageA.ndim)
print("imageA shape:", imageA.shape)
print("imageA height:", height)
print("imageA width:", width)

i_max = 0.5 * (height/subimage_size)
j_max = width/subimage_size

output_directoryA = "../datasets/dogbox/trainA/"
output_directoryB = "../datasets/dogbox/trainB/"
file_name_increment = 1
file_name_baseA = "_A.jpg"
file_name_baseB = "_B.jpg"

i = 0
j = 0
while i < i_max:
    while j < j_max:
        file_pathA = output_directoryA + str(file_name_increment) + file_name_baseA
        write_subimage(file_pathA, imageA, i*subimage_size, j*subimage_size, subimage_size)
        
        file_pathB = output_directoryB + str(file_name_increment) + file_name_baseB
        write_subimage(file_pathB, imageB, i*subimage_size, j*subimage_size, subimage_size)
        
        file_name_increment += 1
        j += 1
    j = 0
    i += 1


