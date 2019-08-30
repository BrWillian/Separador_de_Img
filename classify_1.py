from os import walk,path,getcwd
import cv2
from shutil import move
from tempo import tempo
from numpy import mean,median,sum

tipo_imagem = ['.jpg']

index = [96,160,187]

@tempo
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
    img = cv2.imread(directory)
    img_gray = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)
    equ_img = cv2.equalizeHist(img_gray)
    img_bin = cv2.threshold(img_gray, 40, 255, cv2.THRESH_BINARY)[1]
    result = sum(mean(img_bin)+mean(equ_img)) / 2.0

    return result

if __name__ == "__main__":
    func_filter_dir('C:/Users/willianmoreira/Desktop/vuc')