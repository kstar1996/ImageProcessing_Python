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


def gamma_correction_darker(image_pass: str):
    parsed = (urlparse(image_pass))
    if parsed.scheme is '':
        im = np.array(Image.open(image_pass))
    else:
        im = get_ext(image_pass)

    fn = image_pass.split(".")[len(image_pass.split(".")) - 2]
    filename = fn.split("/")[len(fn.split("/")) - 1]

    im_22 = 255.0 * (im / 255.0) ** 2.2
    pil_gamma_d = Image.fromarray(np.uint8(im_22))
    pil_gamma_d.save(filename+'_gamma_d.jpg')
