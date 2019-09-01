import os
import cv2
import shutil
import numpy as np

def func_filter_dir(directory):
    try:
        for (dirpath, dirnames, filenames) in os.walk(directory):
            for f in filenames:
                f_path = os.path.join(dirpath, f)
                variable = filter(f_path)
                if variable < 1:
                    shutil.move(f_path, directory+'/Escuras/')
    except:
        return "Imagens já processadas!"


def filter(directory):
    img = cv2.imread(directory)
    img_gray = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)
    img_bin = cv2.threshold(img_gray, 25, 255, cv2.THRESH_BINARY)[1]

    result = np.median(img_bin)

    return result


func_filter_dir('/media/Backup/python/Processamento/ao/')