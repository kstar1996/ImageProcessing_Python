import numpy as np
from PIL import Image
import requests


def gamma_correction_brighter(im):
    im_1_22 = 255.0 * (im / 255.0) ** (1 / 2.2)
    return np.uint8(im_1_22)