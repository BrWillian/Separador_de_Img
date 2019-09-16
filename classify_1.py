import os
import shutil
import cv2
import numpy as np
import classify_4

index = [96,160,187]

def func_filter_dir(directory):
    try:
        for (dirpath, dirnames, filenames) in os.walk(directory + '/cache'):
            for f in filenames:
                f_path = os.path.join(dirpath, f)
                filter_1 = filter(f_path)
                filter_2 = classify_4.filter(f_path)
                if filter_1 < index[0] and filter_2:
                    shutil.move(f_path, directory+'/Escuras/')
                elif filter_1 >= index[1] and filter_1 <= index[2] and not filter_2:
                    shutil.move(f_path, directory+'/Claras/')
    except NameError as erro:
        print(erro)


def filter(directory):

    img = cv2.imread(directory)
    img_gray = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)
    equ_img = cv2.equalizeHist(img_gray)
    img_bin = cv2.threshold(img_gray, 40, 255, cv2.THRESH_BINARY)[1]
    result = np.sum(np.mean(img_bin)+np.mean(equ_img)) / 2.0

    return result

if __name__ == "__main__":
    func_filter_dir('C:/Users/willianmoreira/Desktop/teste/van/')