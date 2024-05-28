import numpy as np
from PIL import Image
import sys
n=0
for arg in sys.argv:
    if n==0:
        n+=1
        continue
    if n==1:
        im=np.array(Image.open(sys.argv[n]))
        print('reading '+sys.argv[n])
        n+=1
    else:
        print('reading '+sys.argv[n])
        im=np.concatenate((im,np.array(Image.open(sys.argv[n]))),axis=1)
        print('paste done '+sys.argv[n])
        n+=1

img=Image.fromarray(im)
img.save('out.png')