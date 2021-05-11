from PIL import Image
import numpy as np
import requests
from urllib.parse import urlparse
from os.path import splitext


def get_ext(url: str) -> np:
    """
    :params: url
    Module for checking if image is png or jpeg.
    If image is png, changes the image to jpeg.
    """
    parsed = urlparse(url)
    root, ext = splitext(parsed.path)
    if ext == ".png":
        im_png = Image.open(requests.get(url, stream=True).raw)
        im = np.array(im_png.convert("RGB"))
    else:
        im = np.array(Image.open(requests.get(url, stream=True).raw))
    return im


def color_reduction(image_pass: str):
    """
    :params: image_pass
    Module for reducing color in the image
    """
    parsed = (urlparse(image_pass))
    if parsed.scheme is '':
        im = np.array(Image.open(image_pass))
    else:
        im = get_ext(image_pass)

    fn = image_pass.split(".")[len(image_pass.split(".")) - 2]
    filename = fn.split("/")[len(fn.split("/")) - 1]

    im_128 = im // 128 * 128
    pil_reduction = Image.fromarray(im_128)
    pil_reduction.save(filename+'_reduction.jpg')
