import os
import glob
import shutil

def del_file_Iterative_way(path):
    """
    迭代删除一个文件夹中的所有文件，效果比删除所有文件后，再新建文件夹好，新建文件夹方式在文件夹打开事，会出现程序挂掉
    :param path:
    :return:
    """
    for i in os.listdir(path):
        path_file = os.path.join(path, i) # 取文件相对对路径
        if os.path.isfile(path_file):
            os.remove(path_file)
        else:
            del_file_Iterative_way(path_file)

def del_file(path):
    """
    在文件打开时候，会出现程序卡死
    :param path:
    :return:
    """
    shutil.rmtree(path)
    os.mkdir(path)

def find_files_glob(path):
    """
    images = glob.glob('./frame_name/*.png')
    :param path:
    :return:
    """
    images = glob.glob(path)
    return images

def find_files_listdir(path):
    """

    :param path:
    :return:
    """
    files=[]
    for file in os.listdir(path):
        files.append("/".join((path,file)))# 取文件相对对路径
    return files

if __name__=="__main__":
    files=find_files_listdir("../frame_name")
    print(files)