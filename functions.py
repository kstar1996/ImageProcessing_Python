import numpy as np
from PIL import Image


def invert_pixel(im):
    im_i = 255 - im
    return im_i


def color_reduction(im):
    # im_32 = im // 32 * 32
    im_128 = im // 128 * 128

    return im_128


def mosaic(im1, im2):
    # match to the bigger image
    height1 = im1.shape[0]
    height2 = im2.shape[0]

    if height1>height2:
        im1_slice = im1[:height2, :]
        im_mosa = np.concatenate((im1_slice, im2), axis=1)

        return im_mosa
    elif height1<height2:
        im2_slice = im2[:height1, :]
        im_mosa = np.concatenate((im1, im2_slice), axis=1)

        return im_mosa
    else:
        im_mosa = np.concatenate((im1, im2), axis=1)
        return im_mosa

def gamma_correction_brighter(im):
    im_1_22 = 255.0 * (im / 255.0) ** (1 / 2.2)
    return np.uint8(im_1_22)


def gamma_correction_darker(im):
    im_22 = 255.0 * (im / 255.0) ** 2.2
    return np.uint8(im_22)


def trimming(im, h1, h2, w1, w2):
    print(im.shape)
    # (512, 512, 3)

    im_trim = im[h1:h2, w1:w2]

    return im_trim











