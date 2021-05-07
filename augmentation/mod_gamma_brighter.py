import numpy as np
from PIL import Image
import requests


def gamma_correction_brighter(im):
    im_1_22 = 255.0 * (im / 255.0) ** (1 / 2.2)

    pil_gamma_b = Image.fromarray(np.uint8(im_1_22))
    pil_gamma_b.save('pil_gamma_b.jpg')