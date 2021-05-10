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


def trimming(url_pass: str, h1: int, h2: int, w1: int, w2: int):
   im = get_ext(url_pass)

   im_trim = im[h1:h2, w1:w2]

   pil_trim = Image.fromarray(im_trim)
   print(pil_trim)
   pil_trim.save('pil_trim.jpg')