from PIL import Image
import requests


def invert_pixel(im):
    im_i = 255 - im

    pil_invert = Image.fromarray(im_i)
    pil_invert.save('pil_invert.jpg')
    #return im_i

