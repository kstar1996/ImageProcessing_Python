from PIL import Image
from urllib.parse import urlparse
import requests
from os.path import splitext
import numpy as np


def get_ext(url: str):
    parsed = urlparse(url)
    root, ext = splitext(parsed.path)
    if ext == ".png":
        im_png = Image.open(requests.get(url, stream=True).raw)
        im = np.array(im_png.convert("RGB"))
    else:
        im = np.array(Image.open(requests.get(url, stream=True).raw))
    return im  # or ext[1:] if you don't want the leading '.'


def mosaic(image_pass1: str, image_pass2: str):
    parsed = (urlparse(image_pass1))
    if parsed.scheme is '':
        im1 = np.array(Image.open(image_pass1))
        im2 = np.array(Image.open(image_pass2))
    else:
        im1 = get_ext(image_pass1)
        im2 = get_ext(image_pass2)

    # match to the bigger image
    height1 = im1.shape[0]
    height2 = im2.shape[0]

    if height1 > height2:
        im1_slice = im1[:height2, :]
        im_mosa = np.concatenate((im1_slice, im2), axis=1)

        pil_mosaic = Image.fromarray(im_mosa)
        pil_mosaic.save('pil_mosaic.jpg')
    elif height1 < height2:
        im2_slice = im2[:height1, :]
        im_mosa = np.concatenate((im1, im2_slice), axis=1)

        pil_mosaic = Image.fromarray(im_mosa)
        pil_mosaic.save('pil_mosaic.jpg')
    else:
        im_mosa = np.concatenate((im1, im2), axis=1)
        pil_mosaic = Image.fromarray(im_mosa)
        pil_mosaic.save('pil_mosaic.jpg')