import os
import numpy as np
import cv2
import shutil

def func_filter_dir(directory):
    
    for (dirpath, dirnames, filenames) in os.walk(directory):
        for f in filenames:
            f_path = os.path.join(dirpath, f)
            print(f_path)

func_filter_dir('/home/willian')