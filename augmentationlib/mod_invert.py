from PIL import Image
from urllib.parse import urlparse
import requests
from os.path import splitext
import numpy as np


def get_ext(url: str) -> np:
    parsed = urlparse(url)
    root, ext = splitext(parsed.path)
    if ext == ".png":
        im_png = Image.open(requests.get(url, stream=True).raw)
        im = np.array(im_png.convert("RGB"))
    else:
        im = np.array(Image.open(requests.get(url, stream=True).raw))
    return im


def invert_pixel(image_pass: str):
    parsed = (urlparse(image_pass))
    if parsed.scheme is '':
        im = np.array(Image.open(image_pass))
    else:
        im = get_ext(image_pass)

    fn = image_pass.split(".")[len(image_pass.split(".")) - 2]
    filename = fn.split("/")[len(fn.split("/")) - 1]

    # image pixel invert
    im_i = 255 - im

    pil_invert = Image.fromarray(im_i)
    pil_invert.save(filename+'_invert.jpg')
