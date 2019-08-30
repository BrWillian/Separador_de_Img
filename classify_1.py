from os import walk,path,getcwd
from cv2 import imread,cvtColor,threshold
from shutil import move
from numpy import mean,median,sum

index = [96,160,187]

def func_filter_dir(directory):
    try:
        for (dirpath, dirnames, filenames) in walk(directory):
            for f in filenames:
                f_path = path.join(dirpath, f)
                variavel = filter(f_path)
                if variavel < index[0]:
                    move(f_path, directory+'/Escuras/')
                elif variavel >= index[1] and variavel <= index[2]:
                    move(f_path, directory+'/Claras/')
    except:
        return 'Imagens ja processadas!'


def filter(directory):
    img = imread(directory)
    img_gray = cvtColor(img, cv2.COLOR_RGB2GRAY)
    equ_img = equalizeHist(img_gray)
    img_bin = threshold(img_gray, 40, 255, cv2.THRESH_BINARY)[1]
    result = sum(mean(img_bin)+mean(equ_img)) / 2.0

    return result