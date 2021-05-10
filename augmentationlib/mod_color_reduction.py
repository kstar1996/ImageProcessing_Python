from PIL import Image
import numpy as np
import requests
from urllib.parse import urlparse
from os.path import splitext


def get_ext(url: str):
    parsed = urlparse(url)
    root, ext = splitext(parsed.path)
    if ext == ".png":
        im_png = Image.open(requests.get(url, stream=True).raw)
        im = np.array(im_png.convert("RGB"))
    else:
        im = np.array(Image.open(requests.get(url, stream=True).raw))
    return im


def color_reduction(image_pass: str):
    parsed = (urlparse(image_pass))
    if parsed.scheme is '':
        im = np.array(Image.open(image_pass))
    else:
        im = get_ext(image_pass)

    im_128 = im // 128 * 128
    pil_reduction = Image.fromarray(im_128)
    pil_reduction.save('pil_reduction.jpg')