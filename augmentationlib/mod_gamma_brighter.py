import numpy as np
from PIL import Image
from urllib.parse import urlparse
import requests
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


def gamma_correction_brighter(image_pass: str):
    parsed = (urlparse(image_pass))
    if parsed.scheme is '':
        im = np.array(Image.open(image_pass))
    else:
        im = get_ext(image_pass)

    im_1_22 = 255.0 * (im / 255.0) ** (1 / 2.2)

    pil_gamma_b = Image.fromarray(np.uint8(im_1_22))
    pil_gamma_b.save('pil_gamma_b.jpg')
