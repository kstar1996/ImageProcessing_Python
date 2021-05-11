from PIL import Image
import numpy as np
import requests
from urllib.parse import urlparse
from os.path import splitext
from scipy.ndimage.filters import gaussian_filter


def get_ext(url: str):
    parsed = urlparse(url)
    root, ext = splitext(parsed.path)
    if ext == ".png":
        im_png = Image.open(requests.get(url, stream=True).raw)
        im = np.array(im_png.convert("RGB"))
    else:
        im = np.array(Image.open(requests.get(url, stream=True).raw))
    return im


def blur(image_pass: str):
    parsed = (urlparse(image_pass))
    if parsed.scheme is '':
        im = np.array(Image.open(image_pass))
    else:
        im = get_ext(image_pass)

    fn = image_pass.split(".")[len(image_pass.split(".")) - 2]
    filename = fn.split("/")[len(fn.split("/")) - 1]

    blurred_im = gaussian_filter(im, sigma=(5, 5, 0))
    pil_blur = Image.fromarray(blurred_im)
    pil_blur.save(filename+'_blur.jpg')
