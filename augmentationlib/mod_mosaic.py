from PIL import Image
from urllib.parse import urlparse
import requests
from os.path import splitext
import numpy as np


def get_urlext(url: str) -> np:
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


def mosaic(image_pass1: str, image_pass2: str):
    parsed1 = (urlparse(image_pass1))
    parsed2 = (urlparse(image_pass2))
    if parsed1.scheme is '':
        im1 = get_filext(image_pass1)
    else:
        im1 = get_urlext(image_pass1)

    if parsed2.scheme is '':
        im2 = get_filext(image_pass2)
    else:
        im2 = get_urlext(image_pass2)

    fn = image_pass1.split(".")[len(image_pass1.split(".")) - 2]
    filename1 = fn.split("/")[len(fn.split("/")) - 1]
    fn = image_pass2.split(".")[len(image_pass2.split(".")) - 2]
    filename2 = fn.split("/")[len(fn.split("/")) - 1]

    # match to the bigger image
    height1 = im1.shape[0]
    height2 = im2.shape[0]

    # image mosaic: putting two images together
    if height1 > height2:
        im1_slice = im1[:height2, :]
        im_mosa = np.concatenate((im1_slice, im2), axis=1)

        pil_mosaic = Image.fromarray(im_mosa)
        pil_mosaic.save(filename1+filename2+'_mosaic.jpg')
    elif height1 < height2:
        im2_slice = im2[:height1, :]
        im_mosa = np.concatenate((im1, im2_slice), axis=1)

        pil_mosaic = Image.fromarray(im_mosa)
        pil_mosaic.save(filename1+filename2+'_mosaic.jpg')
    else:
        im_mosa = np.concatenate((im1, im2), axis=1)
        pil_mosaic = Image.fromarray(im_mosa)
        pil_mosaic.save(filename1+filename2+'_mosaic.jpg')
