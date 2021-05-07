from PIL import Image
import requests


def trimming(im, h1, h2, w1, w2):
    print(im.shape)
    # (512, 512, 3)

    im_trim = im[h1:h2, w1:w2]

    return im_trim
