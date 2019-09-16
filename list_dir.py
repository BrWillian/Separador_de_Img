import os
import shutil


def list_dir(directory):

    for (dirpath, dirnames, filenames) in os.walk(directory):
        for f in filenames:
            f_path = os.path.join(dirpath, f)
            f_size = round(os.path.getsize(f_path) / 1024,1)
            f_prop = os.path.splitext(f)
            try:
                os.makedirs(dirpath+'/Claras')
            except:
                pass
            try:
                os.makedirs(dirpath+'/Escuras')
            except:
                pass
            try:
                os.makedirs(dirpath+'/cache/')
            except:
                pass
            shutil.move(f_path, dirpath+'/cache')
            save_data(directory, dirpath, f_prop[1], f_size, f_prop[0])

def save_data(directory, dir, type, size, name):
    try:
        dir = dir.replace('\\','/')
        archive = open(directory+"/import.sql","a")
        archive.write(f'INSERT INTO images VALUES ("{dir}", "{name}","{type}","{size}Kb")\n')
    finally:
        archive.close()
if __name__ == '__main__':
    list_dir('C:/Users/willianmoreira/Desktop/teste/van/')