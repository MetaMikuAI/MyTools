#  Written by Aditya Pokharel
#  adityapokharel97@gmail.com
#  rewitten by MetaMiku
import cv2
import numpy as np
import sys

def output(img, kernel_sharpen ,path):
    output = cv2.filter2D(img, -1, kernel_sharpen)
    cv2.imwrite( path,output)

def sharpen(path):
    #reading the image passed thorugh the command line
    img = cv2.imread(path)
    #generating the kernels
    kernel = np.array([[-1,-1,-1], [-1,9,-1], [-1,-1,-1]])
    #process and output the image
    output(img, kernel, path)

if __name__ == "__main__":
    for i in sys.argv:
        if sys.argv[0]==i:
            continue
        sharpen(i)
        print('Sharpen done '+i)
