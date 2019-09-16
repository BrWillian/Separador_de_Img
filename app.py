import os
import classify_1
import classify_2
import classify_3
import classify_4
import list_dir

directory = input('Digite o caminho do diretorio: ')
directory = directory.replace('\\','/')
list_dir.list_dir(directory)
classify_1.func_filter_dir(directory)
classify_2.func_filter_dir(directory)
classify_3.func_filter_dir(directory)
classify_4.func_filter_dir(directory)

os.removedirs(directory+'/cache/')