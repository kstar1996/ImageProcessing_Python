from PIL import Image
import numpy as np
import requests
from urllib.parse import urlparse
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


def color_reduction(image_pass: str):
    """
    :params: image_pass
    Module for reducing color in the image
    """
    parsed = (urlparse(image_pass))
    # if parsed.scheme is '', meaning that the image is given as a file, open image and save as numpy array
    if parsed.scheme is '':
        im = get_filext(image_pass)
    # if parsed.scheme exists, it means that a url was given
    # put the url in the get_urlext function
    else:
        im = get_urlext(image_pass)
    # split the file name or url to get the name of image
    fn = image_pass.split(".")[len(image_pass.split(".")) - 2]
    filename = fn.split("/")[len(fn.split("/")) - 1]

    # color reduction
    im_128 = im // 128 * 128

    # save image
    pil_reduction = Image.fromarray(im_128)
    pil_reduction.save(filename+'_reduction.jpg')
