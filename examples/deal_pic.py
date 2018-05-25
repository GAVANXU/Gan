# ################################ 将图片按照戴不戴眼镜分为两个集合####################################
import os

import shutil

import math
def labelimg():
    path = '/home/xjh/Downloads/Celeba/Anno/'
    f = open(path + 'list_attr_celeba.txt')
    newTxt = path + "hat.txt"
    newf = open(newTxt, 'a+')
    newNOTxt = path + 'no_hat.txt'
    newNOf = open(newNOTxt, 'a+')

    line = f.readline()
    line = f.readline()
    line = f.readline()
    print(line)
    while line:
        array = line.split()
        if array[0] == '000001.jpg':
            print(array[36])
        if array[36] == '-1':

            new_content = array[0] + '\n'
            newNOf.write(new_content)

        else:
            new_content = array[0] + '\n'
            newf.write(new_content)
        line = f.readline()
    lines = len(newf.readlines())
    print(lines)
    print('there are %d lines in %s ' % (lines, newTxt))
    lines = len(newNOf.readlines())
    print('there are %d lines in %s ' % (lines, newNOf))
    f.close()
    newf.close()
    newNOf.close()

#############################根据上述ＴＸＴ文件将图片存放到两个文件夹中去############################
def move_to():

    path = '/home/xjh/Downloads/Celeba/Anno/'
    path1 = '/home/xjh/Downloads/Celeba/img/img_align_celeba/'

    import os, sys
    import shutil
    import matplotlib.pyplot as plt
    from PIL import Image

    nof = open(path + "no_hat.txt")
    hasf = open(path + "hat.txt")

    noLine = nof.read()

    hasLine = hasf.read()

    list = os.listdir(path1)

    hasGo = True
    noGo = True
    noArray = noLine.split()
    hasArray = hasLine.split()

    for i in range(0, len(list)):

    # for imgName in list:
        imgName = os.path.basename(list[i])
        #print(imgName)

        if (os.path.splitext(imgName)[1] != ".jpg"):
            continue

        if (len(noArray) < 1):
            noGo = False

        if (len(hasArray) < 1):
            hasGo = False
        if (noGo and (imgName in noArray)):
            oldname= path1 + imgName
            newname= path1 + "noHat/" + imgName
            print('..........', newname)
            shutil.move(oldname, newname)
            noLine = nof.readline()
            noArray.remove(imgName)

        if (hasGo and (imgName in hasArray)):
            oldname= path1 + imgName
            newname= path1 + "hasHat/" + imgName
            print('..........', newname)
            shutil.move(oldname, newname)
            hasLine = hasf.readline()
            hasArray.remove(imgName)


    nof.close()
    hasf.close()
# 三个参数分别表示旧地址，新地址，文件格式
def move_top_1500_to_new_path(oldfile, newfile_train, newfile_test, fileformat):
    weblist = os.walk(oldfile)
    # 对上述的两个目录地址进行判断，如不存在则返回不存在信息

    # if os.path.exists(newfile_test) == True and os.path.exists(oldfile) == True or os.path.exists(newfile_train) == True:
    #     newpath = newfile_test
    for path, d, filelist in weblist:
        i = 0
        for filename in filelist:
            if fileformat in filename:
                if i < 1500:
                    # 将文件移动到训练集中
                    full_path = os.path.join(path, filename)  # 旧地址 + 文件名
                    despath = newfile_train + filename  # 新地址 +文件名
                    print('........................', despath)
                    print(shutil.move(full_path, despath), '成功移动文件到train...........')  # 移动文件至新的文件夹
                elif i >= 1500 and i < 2000 :
                    # 将文件移动到测试集中
                    full_path = os.path.join(path, filename)  # 旧地址 + 文件名
                    despath = newfile_test + filename  # 新地址 +文件名
                    print('........................', despath)
                    print(shutil.move(full_path, despath), '成功移动文件到test...........')  # 移动文件至新的文件夹
                else:
                    break



            else:
                print('文件不存在', filename)
            i += 1
            print('===================', i, '................................')


    # else:
    #     print("目录不存在")

def  rename(path, new_path_train, new_path_test):

    count = 1
    for file in os.listdir(path):
        print(file + '...............')

        # os.rename(path + file, path + str(count) + '.jpg')
        if count < 2000:
            shutil.move(path, new_path_train)
        elif count > 2000 and count <2500:
            shutil.move(path, new_path_test)
        count += 1
import numpy as np

def gao_deng_dai_shu():
    A = np.array([[21, 32, 45], [90, 43, 34], [3, 34, 45]])
    # A = np.array([2], [2], [2])
    print(A)
    A = np.linalg.inv(A)
    print('............', A)

# 输入三个点的坐标，返回法向量和 d
def get_point(x1, y1, z1, x2, y2, z2, x3, y3, z3):

    a = ((y2 - y1) * (z3 - z1) - (z2 - z1) * (y3 - y1))
    b = ((z2 - z1) * (x3 - x1) - (x2 - x1) * (z3 - z1))
    c = ((x2 - x1) * (y3 - y1) - (y2 - y1) * (x3 - x1))
    d = (0 - (a * x1 + b * y1 + c * z1))
    # print(d)
    # return a, b, c, d
    print(a, b, c, d)
    er_wei(a, b, c, d, x0=10, y0=3, z0=2)
# 过点A的垂线，并计算点的垂足坐标 ，注意 要在b不为零的情况下才能实现，若刚好为零则赋一个接近0 的数，x0， y0， z0是平面外一点的坐标
def er_wei(a, b, c, d, x0, y0, z0):
    y = ((a + c) * y0 - b * (x0 + z0 + d))/(a + c + b*b)
    x = ((y - y0) * a) / b + x0
    z = ((y - y0) * c) / b + z0
    # 返回垂足坐标
    print(x, y, z)

def to_2D_(a, b, c, x0, y0,z0):
    v = [0, 0, 1]

    cos = (v[-1] * c) / math.sqrt(a * a + b * b + c * c)
    # print(cos)
    # th表示夹角的大小
    th = math.acos(cos)

    l = math.cos(th)
    print(l)









if __name__ == '__main__':
    to_2D_(1,2,2,0,0,0)

    # move_to()
    # oldfile = '~/Downloads/Celeba/img/img_align_celeba/'
    # # path = '/home/xjh/Downloads/Celeba/pth/img/'
    # # # rename(oldfile)
    # #
    # newfile_test = 'test/'
    # newfile_train = 'train/'
    # # rename(oldfile, path + newfile_train, path + newfile_test)
    # move_top_1500_to_new_path(oldfile, oldfile + newfile_train, oldfile + newfile_test, '.jpg')
    #
    # move_to()
    # labelimg()
    # get_point(3, 4, 5, 2, 3, 4, 3, 4, 3)

