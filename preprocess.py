import os
from canny import *

dirs = os.listdir("dataset/archive")

for dir in dirs:
    subdir = os.path.join('dataset', 'original', dir)
    print(subdir)
    for imgdir in os.listdir(subdir):
        img = cv2.imread(os.path.join(subdir,imgdir))
        cannyImg = canny(img)
        resdir = os.path.join('dataset','canny',dir)
        cv2.imwrite(os.path.join(resdir,imgdir+".jpg"),cannyImg)