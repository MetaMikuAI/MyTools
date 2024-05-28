import numpy as np
from PIL import Image
import PIL.ImageOps 
import sys
n=0
for arg in sys.argv:
    if n==0:
        n+=1
        continue
    else:
        inverted_image = PIL.ImageOps.invert(Image.open(sys.argv[n]))
        inverted_image.save(sys.argv[n])
        n+=1
