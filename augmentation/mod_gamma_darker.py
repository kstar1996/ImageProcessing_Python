import numpy as np
from PIL import Image
import requests


def gamma_correction_darker(im):
    im_22 = 255.0 * (im / 255.0) ** 2.2
    return np.uint8(im_22)