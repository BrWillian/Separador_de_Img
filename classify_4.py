import cv2
import numpy as np
import os
import shutil

def func_filter_dir(directory):
    try:
        for (dirpath, dirnames, filenames) in os.walk(directory + '/cache'):
            for f in filenames:
                f_path = os.path.join(dirpath, f)
                variable = filter(f_path)
                if variable:
                    shutil.move(f_path, directory+'/Escuras/')
                else:
                    shutil.move(f_path, directory+'/Claras/')
    except NameError as erro:
        print(erro)


def filter(directory):

    img = cv2.imread(directory)

    b,g,r = cv2.split(img)

    b = np.sum(b)
    g = np.sum(g)
    r = np.sum(r)

    if b == g == r:
        return True
    else:
        return False

if __name__ == "__main__":
    func_filter_dir('C:/Users/willianmoreira/Desktop/teste/van/')