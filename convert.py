######################################
## X-RAY DICOM TO PNG CONVERTER     ##
## By : DJRUMALA                    ##
######################################
from genericpath import isfile
import pydicom
import os
import pandas as pd
import os.path
import matplotlib.pyplot as plt
import cv2
import ipyvolume
import sys
import numpy as np
import shutil

def master(parent,type):
    # iterate over all the files in directory 'parent'
    parent = parent.replace("\\","/")
    parent = parent.replace("'","")
    parent = parent.replace("\"","")
    for file_name in os.listdir(parent):
        checkFile = os.path.join(parent, file_name).replace("\\","/")
        isFile = os.path.isfile(checkFile)
        if isFile == True:
            ds = pydicom.dcmread(checkFile)
            img_array = ds.pixel_array

            if type == "hitam" or type == "putih":
                if type == "hitam":
                    output = (img_array/img_array.max() * 255).astype(np.uint8)
                    output = np.invert(output)
                elif type == "putih":
                    output = img_array

                file_name = file_name.replace(".dcm","")
                out_name = "./png/"+file_name+".png"
                print(out_name)
                cv2.imwrite(out_name, output)
            else:
                print("Input tipe gambar salah")
        else:
            current_path = "".join((parent, "/", file_name))
            if os.path.isdir(current_path):
                master(current_path,type)

if __name__ == "__main__":
    path = "./png"
    if os.path.exists(path):
        shutil.rmtree(path)
    os.makedirs(path) 
    master(sys.argv[1],sys.argv[2])
    print("Data DICOM berhasil di-convert ke PNG")
    print("more info: https://github.com/djrumala/simpledicom2png/")