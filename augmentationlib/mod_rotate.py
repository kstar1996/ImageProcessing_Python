from PIL import Image
import numpy as np
import requests
from urllib.parse import urlparse
from os.path import splitext


def get_urlext(url: str) -> np:
    parsed = urlparse(url)
    root, ext = splitext(parsed.path)
    if ext == ".png":
        im_png = Image.open(requests.get(url, stream=True).raw)
        im = im_png.convert("RGB")
    else:
        im = Image.open(requests.get(url, stream=True).raw)
    return im


def get_filext(file: str) -> np:
    parsed = urlparse(file)
    root, ext = splitext(parsed.path)
    if ext == ".png":
        im_png = Image.open(file)
        im = im_png.convert("RGB")
    else:
        im = Image.open(file)
    return im


def rotate(image_pass: str):
    parsed = (urlparse(image_pass))
    if parsed.scheme is '':
        im = get_filext(image_pass)
    else:
        im = get_urlext(image_pass)

    fn = image_pass.split(".")[len(image_pass.split(".")) - 2]
    filename = fn.split("/")[len(fn.split("/")) - 1]

    # rotate
    rotated_im45 = im.rotate(45)
    rotated_im135 = im.rotate(135)

    rotated_im45.save(filename+'_rotate45.jpg')
    rotated_im135.save(filename + '_rotate135.jpg')
