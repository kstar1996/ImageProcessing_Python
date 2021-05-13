import numpy as np
from PIL import Image
from urllib.parse import urlparse
import requests
from os.path import splitext


def get_urlext(url: str) -> np:
    """
    :params: url
    Module for checking if image is png or jpeg.
    If image is png, changes the image to jpeg.
    """
    parsed = urlparse(url)
    root, ext = splitext(parsed.path)
    # if image is png, change to jpeg format and save as numpy array.
    if ext == ".png":
        im_png = Image.open(requests.get(url, stream=True).raw)
        im = np.array(im_png.convert("RGB"))
    # if image is anything else, just save as numpy array.
    else:
        im = np.array(Image.open(requests.get(url, stream=True).raw))
    return im


def get_filext(file: str) -> np:
    parsed = urlparse(file)
    root, ext = splitext(parsed.path)
    # if image is png, change to jpeg format and save as numpy array.
    if ext == ".png":
        im_png = Image.open(file)
        im = np.array(im_png.convert("RGB"))
    # if image is anything else, just save as numpy array.
    else:
        im = np.array(Image.open(file))
    return im


def gamma_correction_brighter(image_pass: str):
    parsed = (urlparse(image_pass))
    if parsed.scheme is '':
        im = get_filext(image_pass)
    else:
        im = get_urlext(image_pass)

    fn = image_pass.split(".")[len(image_pass.split(".")) - 2]
    filename = fn.split("/")[len(fn.split("/")) - 1]

    # gamma brighter
    im_1_22 = 255.0 * (im / 255.0) ** (1 / 2.2)

    pil_gamma_b = Image.fromarray(np.uint8(im_1_22))
    pil_gamma_b.save(filename+'_gamma_b.jpg')
