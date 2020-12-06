import cv2
import numpy as np
import os
import random

'''
Add rotation and brightness to original dataset
'''

dirs = os.listdir("dataset/original")

#change the brightness and contrast of the image
def imageProcess(img, lighter):
    al = random.randint(-1,1)
    alpha = al*0.1 #contrast
    beta = random.randint(50,100) #brightness
    resImg = np.uint8(np.clip((img+beta*lighter), 0, 255))
    return resImg

for dir in dirs:
    subdir = os.path.join('dataset', 'original', dir)
    print(subdir)
    id = 0

    for imgdir in os.listdir(subdir):
        print(imgdir)
        newImgDir = os.path.join(subdir, imgdir)
        img = cv2.imread(newImgDir)
        img = cv2.resize(img, (224,224))
        print("resize"+newImgDir)
        imgRotate = cv2.rotate(img, cv2.ROTATE_90_CLOCKWISE)
        #imgLighter = imageProcess(img, 1)
        imgDarker = imageProcess(img, -1)

        generatedir = os.path.join('dataset', 'archive', dir)
        cv2.imwrite(os.path.join(generatedir, str(id)+".jpg"), img)
        id += 1
        cv2.imwrite(os.path.join(generatedir, str(id)+".jpg"), imgRotate)
        id += 1
        cv2.imwrite(os.path.join(generatedir, str(id)+".jpg"), imgDarker)
        id += 1




