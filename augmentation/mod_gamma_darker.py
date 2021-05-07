import numpy as np
from PIL import Image
import requests


def gamma_correction_darker(im):
    im_22 = 255.0 * (im / 255.0) ** 2.2
    pil_gamma_d = Image.fromarray(np.uint8(im_22))
    pil_gamma_d.save('pil_gamma_d.jpg')