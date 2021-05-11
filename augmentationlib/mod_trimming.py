from PIL import Image
from urllib.parse import urlparse
import requests
from os.path import splitext
import numpy as np


def get_ext(url: str):
    parsed = urlparse(url)
    root, ext = splitext(parsed.path)
    if ext == ".png":
        im_png = Image.open(requests.get(url, stream=True).raw)
        im = np.array(im_png.convert("RGB"))
    else:
        im = np.array(Image.open(requests.get(url, stream=True).raw))
    return im


def trimming(image_pass: str):

    parsed = (urlparse(image_pass))
    if parsed.scheme is '':
        im = np.array(Image.open(image_pass))
    else:
        im = get_ext(image_pass)

    fn = image_pass.split(".")[len(image_pass.split(".")) - 2]
    filename = fn.split("/")[len(fn.split("/")) - 1]

    h, w, c = im.shape

    im_trim1 = im[0:int(2*h/3), 0:int(2*w/3)]
    im_trim2 = im[0:int(2*h/3), int(w/3):w]
    im_trim3 = im[int(h/3):h, int(w/3):w]
    im_trim4 = im[int(h/3):h, 0:int(2*w/3)]
    im_trim5 = im[int(h/6):int(5*h/6), int(w/6):int(5*w/6)]

    pil_trim1 = Image.fromarray(im_trim1)
    pil_trim1.save(filename+'_trim1.jpg')
    pil_trim2 = Image.fromarray(im_trim2)
    pil_trim2.save(filename+'_trim2.jpg')
    pil_trim3 = Image.fromarray(im_trim3)
    pil_trim3.save(filename+'_trim3.jpg')
    pil_trim4 = Image.fromarray(im_trim4)
    pil_trim4.save(filename+'_trim4.jpg')
    pil_trim5 = Image.fromarray(im_trim5)
    pil_trim5.save(filename+'_trim5.jpg')


