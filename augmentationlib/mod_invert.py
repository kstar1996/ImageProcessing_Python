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
   return im


def invert_pixel(url_pass: str):
   im = get_ext(url_pass)

   im_i = 255 - im

   pil_invert = Image.fromarray(im_i)
   pil_invert.save('pil_invert.jpg')