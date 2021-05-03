from PIL import Image
import numpy as np
import os, glob
from functions import *

# read an image file as ndarray
im1 = np.array(Image.open('sunflower.jpg'))
im2 = np.array(Image.open('cat.jpg'))

pil_invert = Image.fromarray(invert_pixel(im1))
pil_invert.save('pil_inverse.jpg')

pil_reduction = Image.fromarray(color_reduction(im1))
pil_reduction.save('pil_reduction.jpg')

pil_mosaic = Image.fromarray(mosaic(im1, im2))
pil_mosaic.save('pil_mosaic.jpg')

pil_gamma_b = Image.fromarray((gamma_correction_brighter(im1)))
pil_gamma_b.save('pil_gamma_b.jpg')

pil_gamma_d = Image.fromarray((gamma_correction_darker(im1)))
pil_gamma_d.save('pil_gamma_d.jpg')

height = im1.shape[0]
width = im1.shape[1]
pil_trim = Image.fromarray((trimming(im1, 0, 500, 0, 2000)))
pil_trim.save('pil_trim.jpg')


# get the pixel values of image
#for i in range(height):
    #for j in range(width):
        #print(im[i, j])
# result is (R, G, B)









