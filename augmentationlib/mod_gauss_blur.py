from PIL import Image
import numpy as np
import requests
from urllib.parse import urlparse
from os.path import splitext
from scipy.ndimage.filters import gaussian_filter


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


def blur(image_pass: str):
    parsed = (urlparse(image_pass))
    if parsed.scheme is '':
        im = get_filext(image_pass)
    else:
        im = get_urlext(image_pass)

    fn = image_pass.split(".")[len(image_pass.split(".")) - 2]
    filename = fn.split("/")[len(fn.split("/")) - 1]

    # gaussian blur for 3 dimensional image
    blurred_im = gaussian_filter(im, sigma=(5, 5, 0))

    pil_blur = Image.fromarray(blurred_im)
    pil_blur.save(filename+'_blur.jpg')
