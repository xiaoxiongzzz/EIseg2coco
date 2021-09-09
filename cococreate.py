
import cv2
import numpy as np
from matplotlib import pyplot as plt
import os
# 装图片的容器
array_of_img = []
# 定义文件夹名字
directory_name = "mask"
# 类名
title = ['_car_1', '_car_2', '_car_3', '_car_4', '_car_5', '_car_6', '_car_7', '_car_8', '_car_9', '_car_10'
                                                                                                      '_person_11',
            '_person_12', '_person_13', '_person_14', '_person_15', '_person_16', '_person_17', '_person_18',
            '_person_19', '_person_20', 'Gray Image']
def read_directory(directory_name):
   for filename in os.listdir(r"./" + directory_name):
      filenames.append(filename.split('.')[0])
      print(filename)
      img = cv2.imread(directory_name + "/" + filename)
      array_of_img.append(img)
      # print(array_of_img)

while(True):
   filenames = []
   read_directory(directory_name)

   for i in range(len(array_of_img)):
      img = array_of_img[i]
      list= []
      titles = []

      for num in range(0, 20):
         ret, photo1 = cv2.threshold(img, num, 255, cv2.THRESH_BINARY_INV)
         ret, photo2 = cv2.threshold(img, num+1, 255, cv2.THRESH_BINARY_INV)
         list.append(cv2.subtract(photo2, photo1))
         num+1
      for l in range(len(title)):
         titles.append(filenames[i]+title[l])
      for i in range(len(list)):
         plt.subplot(4,5,i+1),plt.imshow(list[i],'gray')
         plt.xticks([]),plt.yticks([])
         cv2.threshold(list[i],0,255,cv2.THRESH_TOZERO_INV)
         if (np.any(list[i])):
            cv2.imwrite(titles[i]+'.png',list[i])
      plt.show()
   break
