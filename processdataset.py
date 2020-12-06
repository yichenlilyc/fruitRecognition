import cv2
import numpy as np
import os
import random

dirs=os.listdir("dataset/archive")


#change the brightness and contrast of the image
def imageProcess(img, lighter):
    al = random.randint(-2,2)
    alpha = al*0.1 #contrast
    beta = random.randint(3, 10) #brightness
    resImg = np.uint8(np.clip((alpha*img+beta*lighter), 0, 255))
    return resImg


for dir in dirs:
    subdir = os.path.join('dataset', 'archive', dir)
    print(subdir)
    id = 0

    for imgdir in os.listdir(subdir):
        print(imgdir)
        newImgDir = os.path.join(subdir, imgdir)
        print(newImgDir)
        img = cv2.imread(newImgDir)
        img = cv2.resize(img, (224,224))
        imgRotate = cv2.rotate(img, cv2.ROTATE_90_CLOCKWISE)
        imgLighter = imageProcess(img, 1)
        imgDarker = imageProcess(img, -1)

        cv2.imwrite(os.path.join(subdir,'generate',str(id)+".jpg"), img)
        id += 1
        cv2.imwrite(os.path.join(subdir,'generate',str(id)+".jpg"), imgRotate)
        id += 1
        cv2.imwrite(os.path.join(subdir,'generate',str(id)+".jpg"), imgLighter)
        id += 1
        cv2.imwrite(os.path.join(subdir,'generate',str(id)+".jpg"), imgDarker)
        id += 1





