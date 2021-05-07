from PIL import Image
import numpy as np
import requests


def trimming(im, h1, h2, w1, w2):
    print(im.shape)
    # (512, 512, 3)

    im_trim = im[h1:h2, w1:w2]

    pil_trim = Image.fromarray(im_trim)
    print(pil_trim)
    pil_trim.save('pil_trim.jpg')
