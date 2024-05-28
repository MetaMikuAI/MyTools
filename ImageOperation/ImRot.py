import numpy as np
from PIL import Image
import sys
n=0
for arg in sys.argv:
    if n==0:
        n+=1
        continue
    else:
        im=np.rot90(np.array(Image.open(sys.argv[n])),1)
        img=Image.fromarray(im)
        img.save(sys.argv[n])
        n+=1
