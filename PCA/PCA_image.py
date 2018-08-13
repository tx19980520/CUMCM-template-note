# -*- coding: utf-8 -*-
import matplotlib
import matplotlib.pyplot as plt
import os
import numpy as np
import sklearn.decomposition as sd
from PIL import Image
import scipy
def rgb2gray(rgb):
    return np.dot(rgb[...,:3], [0.299, 0.587, 0.114])
 
# 读取图片
def read_picture(path):
    im = matplotlib.image.imread(path)
    return im

# 读取文件夹图片
def read_folder(path):
    img = np.array()
    root, dirs, files = os.path.walk(path)
    for pic in files:
        img.append(read_picture(root + "/" + pic))
    return img

def main():
    img = read_picture("self.jpg")
    img_r = rgb2gray(img) 
    #img_r = np.reshape(img, (960, 544*3))
    ipca = sd.PCA(64).fit(img_r)
    img_c = ipca.transform(img_r)
    temp = ipca.inverse_transform(img_c)
    temp = np.reshape(temp,(960,544))
    plt.imshow(temp.astype(np.uint8))
    scipy.misc.imsave('meelo.jpg', temp.astype(np.uint8))
if __name__ == '__main__':
    main()