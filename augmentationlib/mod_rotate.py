from PIL import Image
import numpy as np
import requests
from urllib.parse import urlparse
from os.path import splitext


def get_ext(url: str) -> np:
    parsed = urlparse(url)
    root, ext = splitext(parsed.path)
    if ext == ".png":
        im_png = Image.open(requests.get(url, stream=True).raw)
        im = im_png.convert("RGB")
    else:
        im = Image.open(requests.get(url, stream=True).raw)
    return im


def rotate(image_pass: str):
    parsed = (urlparse(image_pass))
    if parsed.scheme is '':
        im = Image.open(image_pass)
    else:
        im = get_ext(image_pass)

    fn = image_pass.split(".")[len(image_pass.split(".")) - 2]
    filename = fn.split("/")[len(fn.split("/")) - 1]

    # rotate by 45 degrees
    rotated_im = im.rotate(45)

    rotated_im.save(filename+'_rotate45.jpg')
