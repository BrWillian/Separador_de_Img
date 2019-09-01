import os
import shutil
import cv2
import numpy as np

index = [96,160,187]

def func_filter_dir(directory):
    try:
        for (dirpath, dirnames, filenames) in os.walk(directory):
            for f in filenames:
                f_path = os.path.join(dirpath, f)
                variavel = filter(f_path)
                if variavel < index[0]:
                    shutil.move(f_path, directory+'/Escuras/')
                elif variavel >= index[1] and variavel <= index[2]:
                    shutil.move(f_path, directory+'/Claras/')
    except:
        return 'Imagens ja processadas!'


def filter(directory):
    img = cv2.imread(directory)
    img_gray = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)
    equ_img = cv2.equalizeHist(img_gray)
    img_bin = cv2.threshold(img_gray, 40, 255, cv2.THRESH_BINARY)[1]
    result = np.sum(np.mean(img_bin)+np.mean(equ_img)) / 2.0

    return result

print(filter('/media/Backup/python/Processamento/ao/Claras/ete_208.jpg'))