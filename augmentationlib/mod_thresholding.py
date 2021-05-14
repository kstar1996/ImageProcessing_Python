from PIL import Image
import numpy as np
import requests
from urllib.parse import urlparse
from os.path import splitext


def get_urlext(url: str) -> np:
    parsed = urlparse(url)
    root, ext = splitext(parsed.path)
    if ext == ".png":
        im_png = Image.open(requests.get(url, stream=True).raw)
        im = im_png.convert("RGB")
    else:
        im = Image.open(requests.get(url, stream=True).raw)
    return im


def get_filext(file: str) -> np:
    parsed = urlparse(file)
    root, ext = splitext(parsed.path)
    if ext == ".png":
        im_png = Image.open(file)
        im = im_png.convert("RGB")
    else:
        im = Image.open(file)
    return im


# Method to process the red band
def pixelProcRed(intensity):
    return 0


# Method to process the blue band
def pixelProcBlue(intensity):
    return intensity


# Method to process the green band
def pixelProcGreen(intensity):
    return 0


def thresholding(image_pass: str):
    parsed = (urlparse(image_pass))
    if parsed.scheme is '':
        im = get_filext(image_pass)
    else:
        im = get_urlext(image_pass)

    fn = image_pass.split(".")[len(image_pass.split(".")) - 2]
    filename = fn.split("/")[len(fn.split("/")) - 1]

    # Split the red, green and blue bands from the Image
    multiBands = im.split()

    # Apply point operations that does thresholding on each color band
    redBand = multiBands[0].point(pixelProcRed)
    greenBand = multiBands[1].point(pixelProcGreen)
    blueBand = multiBands[2].point(pixelProcBlue)

    # Create a new image from the thresholded red, green and blue brands
    newImage = Image.merge("RGB", (redBand, greenBand, blueBand))

    newImage.save(filename + '_thresholding.jpg')

